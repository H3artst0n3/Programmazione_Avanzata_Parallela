// Angelica Rota SM3201142
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

#include "complex.h"

/*
 * Function:  create_complex
 * -------------------------
 * Function that creates the struct complex number, if the memory allocation was successful
 *
 * real: real part of a complex number
 * imaginary: imaginary part of a complex number
 *
 * returns: class complex
 */
complex create_complex(float real, float imaginary) {
    complex num = (complex)malloc(sizeof(struct complex_number));
    if (num != NULL) {
        num->real = real;
        num->imaginary = imaginary;
    }
    return num;
}

/*
 * Function:  free_complex
 * -----------------------
 * Function that deallocates the struct
 */
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