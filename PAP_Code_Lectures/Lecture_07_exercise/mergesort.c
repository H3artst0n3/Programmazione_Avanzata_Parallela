#include <stdio.h>
#include "merge.h"

void merge_sort(int *v, int len, void (*m) (int *, int, int *, int, int *)){
    int u[len];
    for(int i=1; i<len; i *= 2){
      for(int j=0; j<len; j += (i*2)){
        m(&v[j], i, &v[j+i], i, &u[j]);
      }
    }

}

void check_merge_sort(void (*m) (int *, int, int *, int, int *))
{
  int a[8] = {1, 6, 2, 17, 5, 22, 8, 24};
  merge_sort(a, 8, m);
  for (int i = 0; i < 8; i++) {
    printf("%d ", a[i]);
  }
  printf("\n");
}

int main(int argc, char * argv[])
{
  // srand(time(NULL));
  // check if functions works
  check_merge_sort(merge);
  //check_merge(merge_branchless);
  // they work!
   

  /*for(int i=1; i<=20; i++){
    printf("\nvettore lungo: %d\n", i*1000);
    float a = avg_test_merge(i*1000, merge, 1000);
    float b = avg_test_merge(i*1000, merge_branchless, 1000);
    
    printf("tempo: %f\n", a);
    printf("tempo: %f\n", b);
     
    printf("differenza tempo: %f\n", a-b);
  }*/
  return 0;
}