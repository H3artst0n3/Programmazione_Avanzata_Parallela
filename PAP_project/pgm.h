// Angelica Rota SM3201142
#ifndef _PGM_H
#define _PGM_H

#include <stdio.h>

struct image_pgm {
    int width;
    int height;
    FILE * fd;
    char * filename;
    char * data;
    int size;
    int format;
};

typedef struct image_pgm * image;

// int create_image(image img, char * filename, int height, int width, int max_iterations);
// int write_image(image img, int max_iterations);
// int write_image(char* filename, int height, int width, int max_iterations);

int create_image(image *img, char *filename, int height, int width);
int insert_pixel(image img, int max_iterations);

#endif