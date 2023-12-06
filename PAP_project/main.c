#include <stdio.h>

#include "complex.h"
#include "mandelbrot.h"
#include "pgm.h"

int main(int argc, char * argv[]) {
    // controlli sul numero di elementi in lettura
    int max_iterations = atoi(argv[2]);
    image mandelbrot;
    mandelbrot->filename = argv[1];
    mandelbrot->height = atoi(argv[3]);
    mandelbrot->width = mandelbrot->height*1.5;
    write_image(mandelbrot, max_iterations);
    return 0;
}