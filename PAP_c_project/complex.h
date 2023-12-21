// Angelica Rota SM3201142
#ifndef _COMPLEX_H
#define _COMPLEX_H

struct complex_number {
    float real;
    float imaginary;
};

typedef struct complex_number * complex;

complex create_complex(float real, float imaginary);
void free_complex(complex num);

complex square(complex z);
float modulus(complex z);

#endif