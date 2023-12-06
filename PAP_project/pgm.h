#ifndef _PGM_H
#define _PGM_H

#include <stdio.h>

struct image_pgm {
    int width;
    int height;
    FILE * fd;
    char * filename;
};

typedef struct image_pgm * image;

void write_image(image img, int max_iterations);


#endif