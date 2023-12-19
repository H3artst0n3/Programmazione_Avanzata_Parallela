// Angelica Rota SM3201142
#include <stdio.h>
#include <stdlib.h> 
#include <unistd.h>
#include <math.h>

#include "mandelbrot.h"


#define r 2

/*
 * Function that calculates the minimum n such that, given a complex number c, 
 * the created sequence belongs to the Mandelbrot set.
 * 
 * @param c: complex number
 * @param max_iter: maximum iteration for the total computations
 * 
 * @returns the maximum iteration if the point is inside the Mandelbrot set 
 *          or the minimum iteration for which it is outside it
 * 
 */
int mandelbrot_computations(complex c, int max_iter) {
    
    // creation of two complex numbers with real part 0 and imaginary part 0
    complex z = create_complex(0,0);
    complex zn = create_complex(0,0);
    
    // counter iteration
    int i;

    // creation of the sequence of complex numbers
    for(i = 0; i <= max_iter; i++){
        // square of z
        z = square(z);
        
        // adding the complex number given as a parameter
        zn->real = z->real + c->real;
        zn->imaginary = z->imaginary + c->imaginary;
        
        // if the modulus is greater than the radius, than break
        if (modulus(zn)>= r) {
            break;
        }

        // reassignment of the complex number for the next iteration
        z->real = zn->real;
        z->imaginary = zn->imaginary;
    }

    // when the termination of the for loop occurs, deallocation of the structs and return the last iteration of the for loop
    free_complex(z);
    free_complex(zn);
    return i;
}