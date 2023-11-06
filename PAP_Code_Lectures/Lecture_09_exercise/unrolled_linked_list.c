#include <stdlib.h>
#include <stdio.h>

#include "unrolled_linked_list.h"

// funzione per creare la lista
unrolled_linked_list ulst_make(void)
{
  // allochiamo la memoria
  unrolled_linked_list ulst = (unrolled_linked_list) malloc(sizeof(struct _unrolled_linked_list)); 
  ulst->head = NULL; // testa della lista nulla 
  return ulst;
}

// funzione per cancellare TUTTA la lista
void ulst_delete(unrolled_linked_list lst)
{
  if (lst == NULL) { // se la lista è nulla vuol dire che non ho una lista e quindi ritorniamo
    return;
  }

  unode current = lst->head; // inizializziamo un nodo a cui copio la testa della lista
  while (current != NULL) // fino a quando non finiamo la lista
  {
    unode prev = current; // copiamo il nodo
    current = current->next; // il nodo corrente punterà al nodo successivo
    free(prev); // deallochiamo la memoria di prev
  }

  free(lst); // deallochiamo la memoria della lista
}

// aggiungiamo un nodo alla lista
void ulst_add(unrolled_linked_list lst, int key)
{
  if (lst == NULL) { // se la lista è nulla vuol dire che non ho una lista e quindi ritorniamo
    return;
  }

  unode current = lst -> head; // inizializziamo un nodo a cui copio la testa della lista
  int i = 0; // contatore

  if (current == NULL) { // se il puntatore alla testa è nullo
    unode new = (unode) malloc(sizeof(struct _unrolled_node)); // allochiamo la memoria
    new -> keys[0] = key; // aggiungiamo la chiave nella prima cella dell'array
    new -> valid[0] = true; // cambiamo la cella associata alla chiave come un valore valido
    new -> next = lst->head; // il puntatore al nodo successivo diventa la testa della lista
    lst -> head = new; // la testa della lista diventa il nodo appena creato
    return;
  }

  while (i < UNROLLED_SIZE) { // fino a quando il nodo è libero:
    if(current -> valid[i] == false) { // se troviamo un false nell'array booleano vuol dire che la chiave non è valida
      current -> keys[i] = key; // sostituiamo la chiave i-esima con quella data
      current -> valid[i] = true; // aggiorniamo il valore dell'array booleano nella cella associata alla chiave valida
      return;
    }
    i++; // incrementiamo il contatore
  } 

  if (i == UNROLLED_SIZE) { // se il contatore è pari alla lunghezza dell'array all'interno del nodo
    unode new = (unode) malloc(sizeof(struct _unrolled_node)); // allochiamo la memoria
    new -> keys[0] = key; // aggiungiamo la chiave nella prima cella dell'array
    new -> valid[0] = true; // cambiamo la cella associata alla chiave come un valore valido
    new -> next = lst->head; // il puntatore al nodo successivo diventa la testa della lista
    lst -> head = new; // la testa della lista diventa il nodo appena creato
    return;
  }
}

// funzione per la ricerca di una chiave
bool ulst_search(unrolled_linked_list lst, int key)
{
  if (lst == NULL) { // se finisco la lista e non ho ancora trovato la chiave vuol dire che non c'è e restituisco false
    return false;
  }

  int i = 0; // contatore
  unode current = lst->head; // inizializziamo un nodo a cui copio la testa della lista
  while(current != NULL) { // finchè non arrivo in fondo alla lista
    while(i < UNROLLED_SIZE) { // finchè non finisco l'array delle chiavi
      if (current->keys[i] == key) { // se trovo la chiave restituisco true
        return true;
      }
      i++;
    }

    if (i == UNROLLED_SIZE) { // se ho visto tutto l'array delle chiavi
      current = current->next; // mi sposto nel nodo successivo
    }
  }

  return false;
}

// funzione per stampare la lista
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
      if (current->valid[i]) { // se il valore è valido 
	      printf("%d", current->keys[i]); // stampo la chiave 
      } else { // se non è valido
	      printf("."); // stampo un punto
      }
      if (i < UNROLLED_SIZE - 1) {
	      printf(" ");
      }
    }
    printf("]");
    
    if (current->next != NULL) { // se non ho un puntatore al nodo successivo printo uno spazio
      printf(" ");
    }

    current = current->next; // una volta pieno il nodo non srà più in testa alla lista
  }

  printf(")");
}
