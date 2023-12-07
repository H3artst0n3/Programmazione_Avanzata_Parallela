#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>

#include "pgm.h"
#include "complex.h"
#include "mandelbrot.h"

void write_image(image img, int max_iterations) {
    img->fd = fopen(img->filename, "w+");
    if (img->fd == NULL) {
        return;
    }

    fprintf(img->fd, "P5\n%d %d\n255\n", img->width, img->height);
    for (int row = 0; row < img->height; row++) {
        for (int col = 0; col < img->width; col++){            
            complex c = malloc(sizeof(struct num_complex));
            c->real = ((float)col / img->width) * 3 - 2;
            c->imaginary = ((float)row / img->height) * 2 - 1;
            // printf("c = %f +i%f", c->real, c->imaginary);
            int iter = mandelbrot_computations(c, max_iterations);

            int pixel_color;
            if (iter == max_iterations) {
                pixel_color = 255;
            } else {
                pixel_color = (int)(255 * log(iter)/log(max_iterations));
            }
            free(c);
            fprintf(img->fd, "%c ", (char)pixel_color);
        }
        
        fprintf(img->fd, "\n");
    }
    fclose(img->fd);
}

