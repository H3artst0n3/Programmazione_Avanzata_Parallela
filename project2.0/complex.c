// Angelica Rota SM3201142
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

#include "complex.h"

/*
 * Function that creates the struct complex number

 * @param real: real part of a complex number
 * @param imaginary: imaginary part of a complex number
 *
 * @returns struct complex_number
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
 * Function that deallocates the struct
 */
void free_complex(complex num) {
    if (num != NULL) {
        free(num);
    }
}

/*
 * Function that makes the square of a given complex number
 */
complex square(complex z) {
    float tmp = z->real;
    z->real =  z->real * z->real - z->imaginary *z->imaginary;
    z->imaginary = 2 * tmp * z->imaginary;
    return z;
}

/*
 * Function that makes the modulus of a given complex number
 */
float modulus(complex z) {
    float Re = z->real * z->real;
    float Im = z->imaginary * z->imaginary;

    return sqrtf(Re + Im);
}