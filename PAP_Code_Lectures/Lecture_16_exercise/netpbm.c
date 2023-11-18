#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>

#include "netpbm.h"

// funzione che apre una immagine popolando la struttura img passata come argomento
int open_image(char * path, netpbm_ptr img)
{
  // apriamo l'immagine in lettura e salviamo il valore ritornato dalla funzione nella variabile del file descriptor nella struct
  img->fd = fopen(path, "r+");
  if (img->fd == NULL) {
    // se l'immagine non si è aperta correttamente return -1
    return -1;
  }
  
  // creiamo una struct per salvare le informazioni fornite da stat
  struct stat sbuf;
  // prendiamo il file (nel nostro caso l'immagine) e salviamo le informazioni nel secondo argomento (struct sbuf)
  stat(path, &sbuf);
  // salviamo la dimensione nel file nella variabile size della struct img
  img->size = sbuf.st_size;
  // prendendo l'immagine, leggiamo "P5 \n *valore* *valore* \n 255 \n" e salviamo i valori in larghezza e altezza
  if (fscanf(img->fd, "P5\n%d %d\n255\n", &img->width, &img->height) != 2) { // se leggiamo un valore diverso da due...
    fclose(img->fd); // ... vuol dire che qualcosa è andato storto e chiudiamo l'immagine
    return -2; // per differenziare dall'errore di prima chiudiamo con un secondo valore negativo
  }

  // dopo aver letto con fscanf salviamo il valore del cursore in offset così da sapere dove iniziano i dati dell'immagine
  img->offset = ftell(img->fd);
  // mappiamo in un'area di memoria il file associato al file descriptor e salviamo il puntatore ai dati dell'immagine
  img->data = mmap((void *)0, img->size, PROT_READ | PROT_WRITE, MAP_SHARED, fileno(img->fd), 0);
  // se fallisce la mappatura a mmap...
  if (img->data == MAP_FAILED) {
    fclose(img->fd); // ... chiudiamo l'immagine e restituiamo un terzo valore negativo
    return -3;
  }
  return 0; // se tutto è andato a buon fine restituiamo zero
}

// funzione implementata per appoggiarsi a open_image 
int empty_image(char * path, netpbm_ptr img, int width, int height)
{
  // crea il file in path in scrittura
  FILE * fd = fopen(path, "w+");
  if (fd == NULL) { // se c'è stato un errore ...
    return -1; // ... ritorna un valore negativo
  }
  // scrivo tramite fprintf l'intestazione "P5 \n larghezza altezza \n 255 \n"
  int written = fprintf(fd, "P5\n%d %d\n255\n", width, height);
  // aggiusto la grandezza dell'immagine
  ftruncate(fileno(fd), written + width * height);
  fclose(fd); // chiudo l'immagine
  return open_image(path, img); // restituisco il valore ritornato da open_image
}

// funzione che restituisce un puntatore al pixel in posizione (x, y) nell’immagine passata come argomento
char * pixel_at(netpbm_ptr img, int x, int y)
{
  // se img è NULL, immagine vuota
  if (img == NULL) {
    return NULL; // non ho pixel da restituire
  }
  // se x supera i limiti dell'immagine
  if (x < 0 || x >= img->width) {
    return NULL; // non ho pixel da restituire
  }
  // se y supera i limiti dell'immagine
  if (y < 0 || y >= img->height) {
    return NULL; // non ho pixel da restituire
  }
  // prendo il puntatore ai dati dell'immagine e restituisco il pixel in posizione (x, y)
  return &img->data[y * img->width + x + img->offset];  
}

// funzione che chiude l’immagine
int close_image(netpbm_ptr img)
{
  // se l'immagine è nulla c'è stato un errore ...
  if (img == NULL) { 
    return -1; // ... quindi restituisco un valore negativo
  }
  // tolgo la mappatura dalla memoria
  munmap(img->data, img->size);
  // chiudo il file associato al file descriptor
  fclose(img->fd);
  return 0; // se tutto è andato a buon fine restituisco zero
}
