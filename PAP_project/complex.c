#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

#include "complex.h"

complex power_two(complex z) {
    float tmp = z->real;
    z->real =  z->real * z->real - z->imaginary *z->imaginary;
    z->imaginary = 2 * tmp * z->imaginary;
    return z;
}

int modulus(complex z) {
    float Re = z->real * z->real;
    float Im = z->imaginary * z->imaginary;

    return sqrtf(Re + Im);
}