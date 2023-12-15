// Angelica Rota SM3201142
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

    image mandelbrot;
    
    // printf("Function create_image called: message out the function\n\n");
    create_image(&mandelbrot, filename, height, width);
    // printf("\nFunction create_image done successfully.\n\n");
    // printf("Function insert_pixel called: message out the function\n\n");
    insert_pixel(mandelbrot, max_iterations);
    // printf("\nFunction insert_pixel done successfully\n");

    return 0;
}