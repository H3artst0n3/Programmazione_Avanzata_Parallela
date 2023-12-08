#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

#include "complex.h"

complex create_complex(float real, float imaginary) {
    complex num = (complex)malloc(sizeof(struct num_complex));
    if (num != NULL) {
        num->real = real;
        num->imaginary = imaginary;
    }
    return num;
}

void free_complex(complex num) {
    if (num != NULL) {
        free(num);
    }
}

complex power_two(complex z) {
    float tmp = z->real;
    z->real =  z->real * z->real - z->imaginary *z->imaginary;
    z->imaginary = 2 * tmp * z->imaginary;
    return z;
}

float modulus(complex z) {
    float Re = z->real * z->real;
    float Im = z->imaginary * z->imaginary;

    return sqrtf(Re + Im);
}