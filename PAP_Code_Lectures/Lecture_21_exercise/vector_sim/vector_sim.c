#include <math.h>
#include <omp.h>
#include <stdlib.h>

#include "vector_sim.h"

float cosine_similarity(float * v1, float * v2, int len)
{
  float num = 0;
  float den_x = 0;
  float den_y = 0;

  for (int i = 0; i < len; i++) {
    num += v1[i] * v2[i];
    den_x += v1[i]*v1[i];
    den_y += v2[i]*v2[i];
  }

  den_x = sqrtf(den_x);
  den_y = sqrtf(den_y);

  return num/(den_x*den_y);
}

int most_similar(float * v, float * M, int nrows, int ncols)
{ 
  float maxcosine = 0;
  float * cosine = (float *) malloc(sizeof(float)* nrows);
  int index = 0;

  for (int i = 0; i < nrows; i++) {
    cosine[i] = cosine_similarity(v, M+i*ncols, ncols);
  }

  for (int i = 0; i < nrows; i++) {
    if (maxcosine < cosine[i]) {
      maxcosine = cosine[i];
      index = i;
    }
  }
  free(cosine);
  return index;
}

int omp_most_similar(float * v, float * M, int nrows, int ncols)
{
  float maxcosine = 0;
  float * cosine = (float *) malloc(sizeof(float)* nrows);
  int index = 0;

  #pragma omp parallel for
  for (int i = 0; i < nrows; i++) {
    cosine[i] = cosine_similarity(v, M+i*ncols, ncols);
  }

  for (int i = 0; i < nrows; i++) {
    if (maxcosine < cosine[i]) {
      maxcosine = cosine[i];
      index = i;
    }
  }
  return index;
}


