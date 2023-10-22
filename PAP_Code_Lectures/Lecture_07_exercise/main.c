#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#include "merge.h"

int cmpfunc (const void * a, const void * b) {
  return ( *(int*)a - *(int*)b );
}

int * random_vector(int len)
{
  int * v = (int *) malloc (len * sizeof(int));
  for (int i = 0; i < len; i++) {
    v[i] = rand();
  }
  return v;
}

float test_merge(int n, void (* m) (int *, int, int *, int, int *))
{
  int * v1 = random_vector(n);
  int * v2 = random_vector(n);
  int * results = (int *) malloc(2 * n * sizeof(int));
  qsort(v1, n, sizeof(int), cmpfunc);
  qsort(v2, n, sizeof(int), cmpfunc);
  clock_t start = clock();
  m(v1, n, v2, n, results);
  clock_t end = clock();
  float ms = (float) (end - start) / (CLOCKS_PER_SEC / 1000.0);
  free(v1);
  free(v2);
  free(results);
  return ms;
}

float avg_test_merge(int n,
		    void (* m) (int *, int, int *, int, int *),
		    int repetitions)
{
  float avg = 0;
  for (int i = 0; i < repetitions; i++) {
    avg += test_merge(n, m);
  }
  return avg / repetitions;
}

void check_merge(void (* m) (int *, int, int *, int, int *))
{
  int a[8] = {4, 6, 9, 17, 20, 22, 23, 24};
  int b[5] = {2, 5, 7, 10, 18};
  int c[13];
  m(a, 8, b, 5, c);
  for (int i = 0; i < 13; i++) {
    printf("%d ", c[i]);
  }
  printf("\n");
}

int main(int argc, char * argv[])
{
  srand(time(NULL));
  // check if functions works
  //check_merge(merge);
  //check_merge(merge_branchless);
  // they work!
   

  for(int i=1; i<=20; i++){
    printf("\nvettore lungo: %d\n", i*1000);
    float a = avg_test_merge(i*1000, merge, 1000);
    float b = avg_test_merge(i*1000, merge_branchless, 1000);
    
    printf("tempo: %f\n", a);
    printf("tempo: %f\n", b);
     
    printf("differenza tempo: %f\n", a-b);
  }
  return 0;
}
