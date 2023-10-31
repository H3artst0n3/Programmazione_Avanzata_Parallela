#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

#include "ctree.h"

ctree make_cnode(int key, float val)
{
  ctree t = (ctree) malloc(sizeof(struct _ctree_node));
  t->key[0] = key;
  t->val[0] = val;
  t->first_free = 1;
  for(int i; i<=N+1; i++){
    t->children[i] = NULL;
  }
  return t;
}

ctree cinsert(ctree t, int key, float val)
{
  if (t == NULL){
    return make_cnode(key, val);
  }
  if (t->first_free<3){
    t->key[t->first_free] = key;
    t->val[t->first_free] = val; 
    t->first_free += 1;
  }
  
  printf("NON IMPLEMENTATO");

  return NULL;
}

bool csearch(ctree t, int key, float * val)
{
  printf("NON IMPLEMENTATO");
  return false;
}

void print_ctree(ctree t)
{
  printf("NON IMPLEMENTATO");
}
