#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

#include "complex.h"

complex power_two(complex z) {
    complex z2;
    z2->real = z->real * z->real - z->imaginary *z->imaginary;
    z2->imaginary = 2 * z->real * z->imaginary;
    
    return z2;
}

int modulus(complex z) {
    float Re = z->real * z->real;
    float Im = z->imaginary * z->imaginary;

    return sqrtf(Re + Im);
}