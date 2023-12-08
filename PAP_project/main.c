#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>

#include "complex.h"
#include "mandelbrot.h"
#include "pgm.h"

int main(int argc, char * argv[]) {
    if (argc <4){
        printf("Insufficient arguments\n");
        return -1;
    }

    int max_iterations = atoi(argv[2]);
    int height = atoi(argv[3]);
    char * filename = argv[1];
    int width = height*1.5;
    write_image(filename, height, width, max_iterations);
    return 0;
}