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

  unode current = lst -> head;
  int i = 0;

  if (current == NULL){
    unode new = (unode) malloc(sizeof(struct _unrolled_node));
    new -> keys[0] = key;
    new -> valid[0] = true;
    new -> next = lst->head;
    lst -> head = new;
    return;
  }

  while (i < UNROLLED_SIZE){
    if(current -> valid[i] == false){
      current -> keys[i] = key;
      current -> valid[i] = true;
      return;
    }
    i++;
  } 

  if (i == UNROLLED_SIZE){
    unode new = (unode) malloc(sizeof(struct _unrolled_node));
    new -> keys[0] = key;
    new -> valid[0] = true;
    new -> next = lst->head;
    lst -> head = new;
  }
}

bool ulst_search(unrolled_linked_list lst, int key)
{
  if (lst == NULL){
    return false;
  }

  int i = 0;
  unode current = lst->head;
  while(current != NULL){
    while(i < UNROLLED_SIZE){ 
      if (current->keys[i] == key){
        return true;
      }
      i++;
    }

    if (i == UNROLLED_SIZE){
      current = current->next; 
    }
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
