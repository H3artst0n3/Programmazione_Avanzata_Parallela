#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include "node.h"
#include "tree.h"

int main (int argc, char * argv[])
{
  int n;
  srand((int)time(NULL));
  printf("Numero di nodi: ");
  while (!scanf("%d",&n));
  s_test(n);
  r_test(n);
  return 0;
}