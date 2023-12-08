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
};

typedef struct image_pgm * image;

void write_image(char* filename, int height, int width, int max_iterations);


#endif