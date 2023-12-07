#include <stdio.h>
#include <stdlib.h>

#include "complex.h"
#include "mandelbrot.h"
#include "pgm.h"

int main(int argc, char * argv[]) {
    if (argc <4){
        printf("Insufficient arguments\n");
        return -1;
    }

    int max_iterations = atoi(argv[2]);

    image mandelbrot = malloc(sizeof(struct image_pgm));

    mandelbrot->filename = argv[1];
    printf("file name: %s\n", mandelbrot->filename);
    mandelbrot->height = atoi(argv[3]);
    printf("file height: %d\n", mandelbrot->height);
    mandelbrot->width = mandelbrot->height*1.5;
    printf("file width: %d\n", mandelbrot->width);
    write_image(mandelbrot, max_iterations);

    free(mandelbrot);
    return 0;
}