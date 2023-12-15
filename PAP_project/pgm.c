// Angelica Rota SM3201142
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <omp.h>

#include "pgm.h"
#include "complex.h"
#include "mandelbrot.h"

/*
 * Function:  create_image
 * -----------------------
 * Function that creates the file and populates the image struct
 * 
 * image *img: image struct that we want to populate
 * char *filename: name of the file taht we want to create
 * int height: image height
 * int width: image width
 * 
 * return: zero if function was done sucessfully otherwise a specific error
 */
int create_image(image *img, char *filename, int height, int width) {
    // printf("Function create_image called: message in the function\n");
    // printf("Allocating memory for img...\n");
    *img = malloc(sizeof(struct image_pgm));
    if (*img == NULL) {
        perror("Error allocating memory for image");
        return -1;
    }
    // printf("Memory allocated.\n");

    (*img)->filename = filename;
    // printf("Opening file: %s...\n", (*img)->filename);
    (*img)->fd = fopen((*img)->filename, "w+");
    if ((*img)->fd == NULL) {
        perror("Error opening file");
        free(*img);
        return -2;
    }
    // printf("File opened.\n");

    (*img)->height = height;
    // printf("Assigned height.\n");
    (*img)->width = width;
    // printf("Assigned width.\n");
    
    int written = fprintf((*img)->fd, "P5\n%d %d\n255\n", (*img)->width, (*img)->height);
    // printf("Assigned written.\n");
    
    (*img)->size = written + (*img)->height * (*img)->width * sizeof(char);
    // printf("Assigned size.\n");
    
    // printf("Calling ftruncate...\n");
    if (ftruncate(fileno((*img)->fd), (*img)->size) == -1) {
        perror("Error truncating file");
        fclose((*img)->fd);
        free(*img);
        return -3;
    }
    // printf("Ftruncate done successfully.\n");
    
    // printf("Memory mapping...\n");
    char *mem = mmap(NULL, (*img)->size, PROT_READ | PROT_WRITE, MAP_SHARED, fileno((*img)->fd), 0);
    if (mem == MAP_FAILED) {
        perror("Error mapping memory");
        fclose((*img)->fd);
        free(*img);
        return -4;
    }
    // printf("Memory mapped successfully.\n");
    
    (*img)->data = mem;
    // printf("Image structure created successfully.\n");
    
    return 0;
}

/*
 * Function:  insert_pixel
 * -----------------------
 * Function that inserts pixel in the file create previously
 * 
 * image img: image struct that provide the different values
 * int max_iterations: maximum iteration for the mandelbrot computations
 * 
 * return: zero if the function was done successfully otherwise a specific error
 */
int insert_pixel(image img, int max_iterations) {
    // printf("Function insert_pixel called: message in the function\n");
    #pragma omp parallel for collapse(2) schedule(dynamic)
    for (int row = 0; row < img->height; row++) {
        for (int col = 0; col < img->width; col++) {
            // printf("\nProcessing row: %d, col: %d\n", row, col);
            
            // printf("Calling create_complex...\n");
            complex c = create_complex((float)col / img->width * 3 - 2, (float)row / img->height * 2 - 1);
            // printf("Create_complex returned.\n");
            // printf("c = %f +i%f\n", c->real, c->imaginary);

            // printf("Calling mandelbrot.\n");
            int iter = mandelbrot_computations(c, max_iterations);
            // printf("Mandelbrot returned.\n");

            // printf("Calling free_complex.\n");
            free_complex(c);

            int pixel_color;
            if (iter == max_iterations) {
                pixel_color = 255;
            } else {
                pixel_color = (int)floor(255 * log(iter) / log(max_iterations));
            }
            
            img->data[row * img->width + col] = (char)pixel_color;
        }
    }

    if (munmap(img->data, img->size) == -1) {
        perror("Error unmapping memory");
        return -5;
    }
    
    fclose(img->fd);
    free(img);
    
    printf("Image done and saved successfully.\n");
    return 0;
}

