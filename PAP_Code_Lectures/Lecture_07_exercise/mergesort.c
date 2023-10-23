#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#include "merge.h"

// funzione per inizializzare un vettore random di lunghezza len passata in input
int * random_vector(int len)
{
  int * v = (int *) malloc (len * sizeof(int));
  for (int i = 0; i < len; i++) {
    v[i] = rand();
  }
  return v;
}

void merge_sort(int * v, int len, void (* m) (int *, int, int *, int, int *))
{
  int * origin = v; // vettore originale preso in input
  //inizializziamo un vettore che ha la stessa lunghezza del vettore originale
  int * u = (int *)malloc(len * sizeof(int));
  int * tmp; // vettore temporaneo

  for (int i = 1; i < len; i *= 2) { // per grandezza blocchi da ordinare
    for (int j = 0; j < len; j += 2*i) { // per passare gli indici dei blocchi da ordinare 
      if (j+i >= len) { // ??
	memcpy(&u[j], &v[j], (len - j) * sizeof(int)); // ??
      } else {
	int end = (j + 2*i >= len)?(len -j - i):i; // ????
  // passiamo alla funzione presa in input i due vettori da ordinare, quanto sono lunghi e dove mettere il risultato
	m(&v[j], i, &v[j+i], end, &u[j]); 
      }
    }
    tmp = v; // da qui fino a fine funzione: ??
    v = u;
    u = tmp;
  }
  if (v != origin) {
    memcpy(origin, v, len * sizeof(int));
    free(v);
  } else {
    free(u);
  }
}

// funzione per vedere quanto tempo ci impiega mergesort con le diverse funzioni di merge
float test_mergesort(int n, void (* m) (int *, int, int *, int, int *))
{
  int * v = random_vector(n); // prendiamo vettore random
  clock_t start = clock();
  merge_sort(v, n, m); // passiamo vettore a merge_sort, la sua lunghezza e la funzione merge/merge_branchless
  clock_t end = clock();
  float ms = (float) (end - start) / (CLOCKS_PER_SEC / 1000.0);
  free(v);
  return ms;
}

// funzione per stabilire la media del tempo necessario per tot ripetizioni
float avg_test_sort(int n,
		    void (* m) (int *, int, int *, int, int *),
		    int repetitions)
{
  float avg = 0;
  for (int i = 0; i < repetitions; i++) {
    avg += test_mergesort(n, m);
  }
  return avg / repetitions;
}

// funzione per vedere se mergesort funziona
void check_mergesort(void (* m) (int *, int, int *, int, int *))
{
  int a[9] = {56, 4, 3, 2, 78, 35, 23, 18, 1};
  merge_sort(a, 9, m);
  for (int i = 0; i < 9; i++) {
    printf("%d ", a[i]);
  }
  printf("\n");
}

int main(int argc, char * argv[])
{
  srand(time(NULL));
  printf("Size\tBranchless\tWith branches\n");
  for (int i = 1000; i <= 20000; i += 1000) {
    float t1, t2;
    t1 = avg_test_sort(i, merge_branchless, 30);
    t2 = avg_test_sort(i, merge, 30);
    printf("%d\t%f\t%f\n", i, t1, t2);
  }
  return 0;
}
