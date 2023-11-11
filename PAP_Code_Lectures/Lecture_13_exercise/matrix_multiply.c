#include "matrix_multiply.h"

void simple_multiply(float * A, float * B, float * C, int n)
{
  // moltiplicazione di matrici righe per colonne
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      for (int k = 0; k < n; k++) {
	      C[i * n + j] += A[i * n + k] * B[k * n + j];
      }
    }
  }
}

void transposed_multiply(float * A, float * B, float * C, int n)
{
  // non serve fare la trasposta perchè passiamo in input direttamente la matrice trasposta 
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      for (int k = 0; k < n; k++) {
        // cambiamo gli indici così che moltiplichiamo le matrici riga per riga siccome B è in column major order
	      C[i * n + j] += A[i * n + k] * B[j * n + k]; 
      }
    }
  }
  
}

void kernel(float * A, float * B, float * C, int x, int dx, int y, int dy, int z, int dz, int n)
{
  /*
   * Moltiplicazione di blocchi. Si prende il blocco A[x:x+dx, z:z+dz] e si moltiplica con B[z:z+dz, y:y+dy]
   * sommando il risultato nella posizioni C[x:x+dx, y:y+dy].
   * Prestare attenzione che x+dx, y+dy e z+dz potenzialmente potrebbero essere maggiori di n,
   * quindi serve limitarsi a n come dimensione.
   */

  // per fare il controllo sulla lunghezza facciamo:
  int distx = (x+dx > n) ? n : x+dx;
  int disty = (y+dy > n) ? n : y+dy;
  int distz = (z+dz > n) ? n : z+dz;

  // ciclo for parte da x, y o z siccome questi valori mi indicano qual è la prima cella della sottomatrice
  for (int i = x; i < distx; i++) { 
    for (int j = y; j < disty; j++) {
      for (int k = z; k < distz; k++) {
        // essendo che B è in column major order teniamo gli stessi indici della trasposta, ovvero acceddiamo all'array sequenzialmente
	      C[i * n + j] += A[i * n + k] * B[j * n + k]; 
      }
    }
  }  
}

void blocked_multiply(float * A, float * B, float * C, int n)
{
  const int s1 = 16; // Provare inizialmente con 2 o 4
  const int s2 = 16; // grandezza dei sottoblocchi
  const int s3 = 16;

  for (int i = 0; i < n; i += s1){
    for (int j = 0; j < n; j +=s2){
      for (int k = 0; k < n; k+=s3)
        // siccome abbiamo dei puntatori agli array, posso semplicemente chiamare la funzione passando in input i valori aggiornati
        // non serve sommare nulla in questa funzione siccome nella funzione kernel facciamo C += A*B
        kernel(A, B, C, i, s1, j, s2, k, s3, n);
    }
  }
}
