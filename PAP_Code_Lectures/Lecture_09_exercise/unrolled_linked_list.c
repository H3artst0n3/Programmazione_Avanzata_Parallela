#include <stdlib.h>
#include <stdio.h>

#include "unrolled_linked_list.h"

unrolled_linked_list ulst_make(void)
{
  unrolled_linked_list ulst = (unrolled_linked_list) malloc(sizeof(struct _unrolled_linked_list)); 
  ulst->head = NULL;
  return ulst;
}

void ulst_delete(unrolled_linked_list lst)
{
  if (lst == NULL){
    return;
  }
  unode current = lst->head;
  while (current != NULL)
  {
    unode prev = current;
    current = current->next;
    free(prev);
  }
  free(lst);
}

void ulst_add(unrolled_linked_list lst, int key)
{
  if (lst == NULL){
    return;
  }
  unode new = (unode) malloc(sizeof(struct _unrolled_node));
  /*new->keys[] = key;
  new->valid[] = true;
  new->next = lst->head;
  lst->head = new;*/
}

bool ulst_search(unrolled_linked_list lst, int key)
{
  if (lst == NULL){
    return false;
  }
  unode current = lst->head;
  while(current != NULL){
    if (current->keys == key){
      return true;
    }
    current = current->next;
  }
  return false;
}

void ulst_print(unrolled_linked_list lst)
{
  if (lst == NULL) {
    printf("NIL");
    return;
  }
  printf("(");
  unode current = lst->head;
  while (current != NULL) {
    printf("[");
    for (int i = 0; i < UNROLLED_SIZE; i++) {
      if (current->valid[i]) {
	printf("%d", current->keys[i]);
      } else {
	printf(".");
      }
      if (i < UNROLLED_SIZE - 1) {
	printf(" ");
      }
    }
    printf("]");
    if (current->next != NULL) {
      printf(" ");
    }
    current = current->next;
  }
  printf(")");
}
