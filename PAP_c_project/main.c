// Angelica Rota SM3201142
#include <stdio.h>
#include <stdlib.h>

#include "complex.h"
#include "mandelbrot.h"
#include "pgm.h"

int main(int argc, char * argv[]) {
    if (argc < 4){
        printf("Insufficient arguments. Depending on You.\n");
        return -1;
    }

    // assignment of the parameters given from the command line
    char * filename = argv[1];
    int max_iterations = atoi(argv[2]); 
    int height = atoi(argv[3]);
    int width = height*1.5;

    // creating mandelbrot image struct
    image mandelbrot;

    printf("Start Me Up.\n");
    
    // function calls for creating the image and inserting pixels
    create_image(&mandelbrot, filename, height, width);
    insert_pixel(mandelbrot, max_iterations);

    printf("Sweet Sounds of Heaven.\n");

    return 0;
}