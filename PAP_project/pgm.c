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
    for (int nrows = 0; nrows < img->height; nrows++) {
        for (int ncols = 0; ncols < img->width; ncols++) {
            complex c;
            c->real = ((float)ncols/img->width)* 3 - 2;
            c->imaginary = ((float)nrows/img->height)* 2 - 1;

            int iter = mandelbrot_computations(c, max_iterations);

            int pixel_color;
            if (iter == max_iterations) {
                pixel_color = 255;
            } else {
                pixel_color = floor(255 * log(iter)/log(max_iterations));
            }

            fprintf(img->fd, "%d", pixel_color);
        }
        fprintf(img->fd, "\n");
    }
    
    fclose(img->fd);
}