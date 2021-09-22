#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>

//pthread_mutex_t lock;

void *hola(void *arg)
 {
   //pthread_mutex_lock(&lock);
   char *msg = "Hola";
   int i;
   for ( i = 0 ; i < strlen (msg) ; i++ ) 
   {
      printf (" %c", msg[i]);
      fflush (stdout );
      usleep (1000000) ;
   }
  // pthread_mutex_unlock(&lock);
   return NULL;
}

void *mundo(void *arg )
{
   //pthread_mutex_lock(&lock);
   char *msg = " mundo ";
   int i;
   for ( i = 0 ; i < strlen (msg) ; i++ ) 
   {
      
      printf (" %c", msg[i]);
      fflush (stdout );
      usleep (1000000) ; 
      
   }
   //pthread_mutex_unlock(&lock);
   return NULL;
}

int main(int argc , char *argv []) 
{
   pthread_t h1; //Declara dos variables de tipo hilo 
   pthread_t h2; //Aqui se deposita la información de control del hilo
//Se manda NULL porque son apuntadores a nulo  
   pthread_create(&h1, NULL , hola , NULL); //Funcion que crea el hilo, necesita la variable de tipo hilo 
   pthread_create(&h2, NULL , mundo , NULL); //Tambien recibe la funcion donde esta el código del hilo 
   printf ("Fin\n"); //Los hilos mueren porque el proceso termina
   pthread_join(h1, NULL);
   pthread_join(h2, NULL);
   //pthread_mutex_destroy(&lock);

}