// Angelica Rota SM3201142
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "mandelbrot.h"

#define r 2

/*
 * Function:  mandelbrot_computations
 * ----------------------------------
 * Function that calculate the minimum n such that c is in the fractal of mandelbrot
 * 
 * complex c: complex number
 * int max_iter: maximum iteration for the total computations
 */
int mandelbrot_computations(complex c, int max_iter) {
    complex z = create_complex(0,0);
    complex zn = create_complex(0,0);
    
    z->imaginary=0;
    z->real=0;

    for(int i = 0; i <= max_iter; i++){
        z = square(z);
        zn->real = z->real + c->real;
        zn->imaginary = z->imaginary + c->imaginary;
        
        z->real = zn->real;
        z->imaginary = zn->imaginary;
        
        if (modulus(zn)>= r) {
            return i;
        }

    }
    free_complex(z);
    free_complex(zn);
    return max_iter;
}