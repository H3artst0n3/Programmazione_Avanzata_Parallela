#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

#include "ctree.h"

// funzione per creare un nodo
ctree make_cnode(int key, float val)
{
  ctree t = (ctree) malloc(sizeof(struct _ctree_node));
  t->key[0] = key; // inseriamo la chiave nella prima cella dell'array
  t->val[0] = val; // inseriamo il valore nella prima cella dell'array
  t->first_free = 1; // aggiorniamo il valore della prima cella libera nell'array
  for(int i=0; i<=N+1; i++) {
    t->children[i] = NULL; // inizializziamo i figli a NULL 
  }
  return t;
}

// funzione per l'inserimento
ctree cinsert(ctree t, int key, float val)
{
  if (t == NULL) { // se abbiamo il nodo pari a NULL 
    return make_cnode(key, val); // creiamo il nodo
  }

  // controllo per vedere se la chiave è già presente
  for (int i=0; i<t->first_free; i++) {
    if (t->key[i] == key) {
      t->val[i] = val; // aggiorniamo solamente il valore legato alla chiave
      return t;
    }
  }

  // controllo per vedere se è possibile inserire la chiave nel nodo corrente
  if (t->first_free < N) { // controllo dove è posizionata la prima cella libera
    for (int i=0; i<t->first_free; i++) {
      if (t->key[i] > key){ // se ho che la chiave che devo inserire è minore della chiave presente nella cella i-esima
        int tmp = t->key[i]; // switch della chiave
        t->key[i] = key;
        key = tmp; 

        float tmpval = t->val[i]; // switch dei valori associati alle chiavi
        t->val[i] = val;
        val = tmpval;
      }
    }
    t->key[t->first_free] = key; // inseriamo la chiave nella prima cella libera
    t->val[t->first_free] = val; // inseriamo il valore nella prima cella libera
    t->first_free += 1; // incrementiamo di uno la posizione della prima cella libera
    return t;
  } else { // se invece non ho una cella libera devo creare un nuovo nodo
    for (int i = 0; i<N; i++) {
      if (key < t->key[i]) { // controllo se la mia chiave è minore della cella i-esima
        t->children[i] = cinsert(t->children[i], key, val); // se è minore cambio il puntatore al figlio i-esimo
        return t;
      }
    }
    // se invece la mia chiave è maggiore rispetto a tutte quelle nell'array allora cambio il puntatore del figlio n+1-esimo
    t->children[N+1] = cinsert(t->children[N+1], key, val);
  }
  return t;
}

// funzione per la ricerca
bool csearch(ctree t, int key, float * val)
{
  if (t == NULL) { // se non ho trovato la chiave restituisco false
    return false;
  }

  // controllo se la chiave è presente nel nodo preso in considerazione e mi salvo il valore corrispondente
  for (int i=0; i<N; i++) {
    if (t->key[i] == key) {
      *val = t->val[i];
      return true;
    }
  }

  // se non ho trovato la chiave:
  for (int i = 0; i<N; i++) {
    if (key < t->key[i]) { // se la chiave è minore della chiave i-esima
      return csearch(t->children[i], key, val); // allora chiamo la funzione di ricerca nel figlio i-esimo
    }
  }
  // se la chiave è maggiore di tutte quelle presenti
  return csearch(t->children[N+1], key, val); // chiamo la funzione di ricerca nell'ultimo figlio
}

// funzione che stampa l'albero
void print_ctree(ctree t)
{
  if (t == NULL) { // se il figlio è NULL
    printf(".");
    return;
  }
  
  printf("(");

  // stampo la prima metà dei figli (sottoalbero sinistro)
  for (int i=0; i<(N+1)/2; i++)
  {
    print_ctree(t->children[i]);
  }
  
  // stampo le chiavi del nodo
  for (int i=0; i<t->first_free; i++)
  {
    printf(" %d ", t->key[i]);
  }
  
  // stampo la seconda metà dei figli (sottoalbero destro)
  for (int i=(N+1)/2; i<(N+1); i++)
  {
    print_ctree(t->children[i]);
  }
  
  printf(")");
  
/* CODICE DEL PROF:
  printf("(");
    for (int i = 0; i < t->first_free; i++) {
      print_ctree(t->children[i]);
      printf(" %d ", t->key[i]);
  }
  print_ctree(t->children[N]);
  printf(")");
  */
}
