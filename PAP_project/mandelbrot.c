#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "mandelbrot.h"

#define r 2

int mandelbrot_computations(complex c, int max_iter) {
    complex z;
    z->real = 0;
    z->imaginary = 0;
    int i = 0;

    while ((modulus(z)<r) && (i<max_iter)){
        complex zn = power_two(z);
        zn->real += c->real;
        zn->imaginary += c->imaginary;
        z = zn;
        i++;
    }
    return i;
}