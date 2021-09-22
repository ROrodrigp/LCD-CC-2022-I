#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void)
{
   int i;
   int a,b;
   pid_t pidh1,pidh2,pidx;
   int prod,mayor;
   int res;


   printf("\nDame dos enteros: \n");
   scanf("%d%d", &a, &b);
   printf("res: %d\n",res );
   pidh1 = fork();
   printf("res: %d\n",res );
// código del padre
   if(pidh1)
   {  
      printf("\nEjecucion padre : \n");
      printf("res: %d\n",res );
      pidh2 = fork();
      if(pidh2)
      {
        printf("\nEjecucion padre sigue : \n");
        printf("res: %d\n",res );
        for(i = 0; i < 2; i++)
        {   
          printf("\nPadre espera por %d vez : \n",i);
           pidx = wait(&res);
           printf("\npadre sigue despues de esperar : \n");
           printf("pro del padre: %d\n",prod);
           printf("res: %d\n",res );
           printf("pidx: %d\n",pidx);
           printf("pidh1: %d\n",pidh1 );
        if (pidx == pidh1){
            printf("res del if: %d\n",res );
             prod = res >> 8;}
           else{
              printf("res del else: %d\n",res );
             mayor = res >> 8;}
          }
        
        printf("\n El producto de %d y %d es %d", a,b,prod);
        printf("\n El mayor de %d y %d es %d \n", a,b,mayor);
        printf("\nTermina padre : \n");
      }

      else
      {
          printf("\nEjecucion hijo 2 : \n");
         if(a > b){
            printf("Aqui igual " );
            printf("\nTermina hijo 2 : \n");
           exit(a);}
         else{
            printf("Aqui tambien  " );
            printf("\nTermina hijo 2 : \n");
           exit(b);}
      }
   }
// hijo 1
   else
      {
      printf("\nEjecucion hijo 1  : \n");
     prod = a * b;
     printf("Llega aqui");
     printf("pro del hijo 1: %d\n",prod);
     printf("\nTermina hijo 1 : \n");
     exit(prod);
      }

  return(0);

 }