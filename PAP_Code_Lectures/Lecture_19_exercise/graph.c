#include <stdlib.h>
#include <math.h>
#include <omp.h>

#include "graph.h"

void shortcut_std(float * m, float * d, int n)
{
    for (int i = 0; i<n; i++){
        for (int j = 0; j<n; j++){
            m[i*n +j] = INFINITY;
            for (int k = 0; k<n; k++){
                float val = d[i*n + k] + d[k*n + j];

                if (val < m[i*n + j]){
                    m[i*n + j] = val;
                }
            }
        }
    }
}

void shortcut_trs(float * m, float * d, int n)
{
    float * t = malloc(sizeof(float)*n*n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
        t[j * n + i] = d[i * n + j];
        }
    }

    for (int i = 0; i<n; i++){
        for (int j = 0; j<n; j++){
            m[i*n +j] = INFINITY;
            for (int k = 0; k<n; k++){
                float val = d[i*n + k] + t[j*n + k];

                if (val < m[i*n + j]){
                    m[i*n + j] = val;
                }
            }
        }
    }

    free(t);
}

void shortcut_omp(float * m, float * d, int n)
{
    #pragma omp parallel for 
        for (int i = 0; i<n; i++){
            for (int j = 0; j<n; j++){
                m[i*n +j] = INFINITY;
                for (int k = 0; k<n; k++){
                    float val = d[i*n + k] + d[k*n + j];

                    if (val < m[i*n + j]){
                        m[i*n + j] = val;
                    }
                }
                
            }
        }
}

void shortcut(float * m, float * d, int n)
{
    float * t = malloc(sizeof(float)*n*n);
    #pragma omp parallel for
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
            t[j * n + i] = d[i * n + j];
            }
        }

    #pragma omp parallel for
        for (int i = 0; i<n; i++){
            for (int j = 0; j<n; j++){
                m[i*n +j] = INFINITY;
                for (int k = 0; k<n; k++){
                    float val = d[i*n + k] + t[j*n + k];

                    if (val < m[i*n + j]){
                        m[i*n + j] = val;
                    }
                }
            }
        }

    free(t);
}
