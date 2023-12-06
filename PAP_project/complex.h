#ifndef _COMPLEX_H
#define _COMPLEX_H

#include <stdio.h>
#include <math.h>

struct num_complex {
    float real;
    float imaginary;
};

typedef struct num_complex * complex;

complex power_two(complex z);
int modulus(complex z);

#endif