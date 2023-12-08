#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <omp.h>

#include "pgm.h"
#include "complex.h"
#include "mandelbrot.h"

void write_image(char* filename, int height, int width, int max_iterations) {
    printf("Function write_image called.\n");
    printf("Allocating memory for img...\n");
    struct image_pgm *img = malloc(sizeof(struct image_pgm));
    if (img == NULL) {
        perror("Error allocating memory for image");
        // close(fd);
        return;
    }
    
    img->filename = malloc(strlen(filename) + 1); // +1 for the null terminator
    if (img->filename == NULL) {
        perror("Error allocating memory for filename");
        free(img);
        return;
    }
    strcpy(img->filename, filename);

    printf("Opening file: %s...\n", img->filename);
    img->fd = fopen(img->filename,"w+");
    if (img->fd == NULL) {
        perror("Error opening file");
        free(img->filename);
        free(img);
        return;
    }  
    printf("File descriptor: %p\n", (void *)img->fd);
    printf("File opened successfully.\n");
    img->height = height;
    printf("Assigned height.\n");
    img->width = width;
    printf("Assigned width.\n");
    int written = fprintf(img->fd, "P5\n%d %d\n255\n", img->width, img->height);
    printf("Assigned written.\n");

    // img->data = mmap((void *)0, img->size, PROT_READ | PROT_WRITE, MAP_SHARED, fileno(img->fd), 0);
    img->size = written + img->height * img->width * (sizeof(char));
    printf("Assigned size.\n");
    // ftruncate(img->fd, written + img->size);
    
    off_t img_size = written + height * width * sizeof(char);
    if (ftruncate(fileno(img->fd), img_size) == -1) {
        perror("Error truncating file");
        fclose(img->fd);
        free(img->filename);
        free(img);
        return;
    }
    
    printf("Memory mapping...\n");
    char * mem = mmap(NULL, img->size, PROT_READ | PROT_WRITE, MAP_SHARED, fileno(img->fd), 0);
    if (mem == MAP_FAILED) {
        perror("Error mapping memory");
        fclose(img->fd);
        free(img);
        return;
    }    
    // img->data = mem;
    #pragma omp parallel for collapse(2)
    for (int row = 0; row < img->height; row++) {
        for (int col = 0; col < img->width; col++){            
            // complex c = malloc(sizeof(struct num_complex));
            // c->real = ((float)col / img->width) * 3 - 2;
            // c->imaginary = ((float)row / img->height) * 2 - 1;
            // printf("Processing row: %d, col: %d\n", row, col);
            // printf("Calling create_complex...\n");
            complex c = create_complex((float)col / img->width * 3 - 2, (float)row / img->height * 2 - 1);
            // printf("create_complex returned.\n");
            // printf("c = %f +i%f\n", c->real, c->imaginary);
            
            // printf("calling mandelbrot.\n");
            int iter = mandelbrot_computations(c, max_iterations);
            // printf("mandelbrot returned.\n");
            // printf("calling free_complex.\n");
            free_complex(c);
            // printf("free_complex returned.\n");

            int pixel_color;
            if (iter == max_iterations) {
                pixel_color = 255;
            } else {
                pixel_color = (int)floor(255 * log(iter)/log(max_iterations));
            }
            // free(c);
            // fprintf(img->fd, "%c ", (char)pixel_color);
            mem[written + row * img->width + col] = (char)pixel_color;
        }
        
        // fprintf(img->fd, "\n");
    }

    // munmap(img->data, written + img->size);
    if (munmap(mem, img->size) == -1) {
        perror("Error unmapping memory");
    }
    fclose(img->fd);
    free(img);
}

