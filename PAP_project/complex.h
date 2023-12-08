#ifndef _COMPLEX_H
#define _COMPLEX_H

#include <stdio.h>
#include <math.h>

struct num_complex {
    float real;
    float imaginary;
};

typedef struct num_complex * complex;

complex create_complex(float real, float imaginary);
void free_complex(complex num);
complex power_two(complex z);
float modulus(complex z);

#endif