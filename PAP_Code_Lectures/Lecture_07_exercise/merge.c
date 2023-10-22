#include "merge.h"
#include <string.h>

void merge(int * v1, int n1, int * v2, int n2, int * results)
{
  int i = 0;
  int j = 0;
  int k = 0;

  while ((i < n1) && (j < n2)){
    if (v1[i] < v2[j]){
      results[k] = v1[i];
      i++;
    }else{
      results[k] = v2[j];
      j++;
    }
    k++;
  }

  memcpy(&results[k], &v1[i], sizeof(int)*(n1-i));
  memcpy(&results[k], &v2[j], sizeof(int)*(n2-j));
}


void merge_branchless(int * v1, int n1, int * v2, int n2, int * results)
{
  int i = 0;
  int j = 0;
  int k = 0;

  while ((i < n1) && (j < n2)){
    int q = v1[i] < v2[j];
    results[k] = v1[i]*q + v2[j]*(1-q);
    i += q;
    j += (1-q);
    k++;
  }

  memcpy(&results[k], &v1[i], sizeof(int)*(n1-i));
  memcpy(&results[k], &v2[j], sizeof(int)*(n2-j));
}
