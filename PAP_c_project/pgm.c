// Angelica Rota SM3201142
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <sys/mman.h>
#include <omp.h>


#include "pgm.h"
#include "complex.h"
#include "mandelbrot.h"

/*
 * Function that creates the file and populates the image struct
 * 
 * @param img: image struct that we want to populate
 * @param filename: name of the file taht we want to create
 * @param height: image height
 * @param width: image width
 * 
 * @returns zero if function was done sucessfully otherwise a specific error
 *
 */
int create_image(image *img, char *filename, int height, int width) {
    
    // allocating memory for image
    *img = malloc(sizeof(struct image_pgm));
    if (*img == NULL) {
        perror("Error allocating memory for image");
        return -1;
    }

    // saving the file name in the struct
    (*img)->filename = filename;
    
    // opening the image and checking if there have been any errors
    (*img)->fd = fopen((*img)->filename, "w+");
    if ((*img)->fd == NULL) {
        perror("Error opening file");
        free(*img);
        return -2;
    }

    // saving height and width in the struct
    (*img)->height = height;
    (*img)->width = width;

    // writing and saving the header of the image file
    int written = fprintf((*img)->fd, "P5\n%d %d\n255\n", (*img)->width, (*img)->height);
    
    // saving the size of the image file
    (*img)->size = written + (*img)->height * (*img)->width * sizeof(char);
    
    // adjusting the file length
    if (ftruncate(fileno((*img)->fd), (*img)->size) == -1) {
        perror("Error truncating file");
        fclose((*img)->fd);
        free(*img);
        return -3;
    }

    // mapping memory for the size of the file
    (*img)->data = mmap(NULL, (*img)->size, PROT_READ | PROT_WRITE, MAP_SHARED, fileno((*img)->fd), 0);
    if ((*img)->data == MAP_FAILED) {
        perror("Error mapping memory");
        fclose((*img)->fd);
        free(*img);
        return -4;
    }    
    
    // if here all done successfully!
    printf("Struct image for %s created successfully.\n", (*img)->filename);
    return 0;
}

/*
 * Function that inserts pixel in the file create previously
 * 
 * @param img: image struct that provide the different values
 * @param max_iterations: maximum iteration for the mandelbrot computations
 * 
 * @returns zero if the function was done successfully otherwise a specific error
 */
int insert_pixel(image img, int max_iterations) {
    
    // using openMP to parallelize for loops dynamically
    #pragma omp parallel for collapse(2) schedule(dynamic)
    for (int row = 0; row < img->height; row++) {
        for (int col = 0; col < img->width; col++) {

            //creation of points in the plane of range [-2, 1] for the real part and [-i, i] for the imaginary part, then calculating the iteration
            complex c = create_complex((float)col / img->width * 3 - 2, (float)row / img->height * 2 - 1);
            int iter = mandelbrot_computations(c, max_iterations);
            free_complex(c);

            // calculation of the color that the pixel must have, based on whether or not it belongs to the Mandelbrot set
            int pixel_color;
            if (iter == max_iterations+1) {
                pixel_color = 255;
            } else {
                pixel_color = (int)floor(255 * log(iter) / log(max_iterations));
            }
            
            // saving the color in the right position/pixel
            img->data[row * img->width + col] = (char)pixel_color;
        }
    }

    // deallocating the mapped data
    if (munmap(img->data, img->size) == -1) {
        perror("Error unmapping memory");
        fclose(img->fd);
        free(img);
        return -5;
    }
    
    // if here all done successfully! Deallocating the image struct and close the file
    fclose(img->fd);
    free(img);
    printf("Image done and saved successfully.\n");
    return 0;
}