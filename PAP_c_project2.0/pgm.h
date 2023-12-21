// Angelica Rota SM3201142
#ifndef _PGM_H
#define _PGM_H

struct image_pgm {
    int width;
    int height;
    FILE * fd;
    char * filename;
    int offset;
    char * data;
    // char * data_g;
    // char * data_b;
    int size;
    int format;
};

typedef struct image_pgm * image;

int create_image(image *img, char *filename, int height, int width);
int insert_pixel(image img, int max_iterations);

#endif