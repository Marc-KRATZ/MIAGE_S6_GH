#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]){ 
  char *adresse;
  int famille;
  int port;
  
  int looptime = 0; /* Numero de la boucle */
  socklen_t ls = sizeof(struct sockaddr_in); /* Taille des adresses */
  
  /*---- Caracterisation de la socket localen ----------*/
  int sd0;           /* Descripteur  */
  int ps0 = atoi(argv[1]);    /* Port         */
  struct sockaddr_in adr0, *padr0 = &adr0; /* Adresse  */
  
  /* a) Creation : Domaine AF_INET, type DGRAM, proto. par defaut*/
  if ((sd0=socket(AF_INET, SOCK_DGRAM, 0)) == -1)
    perror("[SOCK_DGRAM, AF_INET, 0]");
  else
    printf("socket [SOCK_DGRAM, AF_INET, 0] creee\n");
  
  /* b) Preparation de l'adresse d'attachement */
  adr0.sin_family      = AF_INET;
  adr0.sin_addr.s_addr = htonl(INADDR_ANY);  /* Format reseau */
  adr0.sin_port        = htons(ps0);  /* Port fixe !!! a choisir  */
  
  /* c) Demande d'attachement de la socket */
  if (bind(sd0,(struct sockaddr *)(padr0),ls) == -1) {
    perror("Attachement de la socket impossible");
    close(sd0);  /* Fermeture de la socket               */
    exit(2);       /* Le processus se termine anormalement.*/
  }
  
  /* d) Recuperation de l'adresse effective d'attachement. */
  getsockname(sd0,(struct sockaddr *)padr0,&ls);
  
  
  /*---- Caracterisation de la socket distante ------*/
  struct sockaddr_in adr1,*padr1 = &adr1;  /* Adresse du destinataire */
  
  /*---- Buffers pour Messages -------------------------------*/ 
  char msg_in[3] = "0";      /* Message recu de "0" a "99" */
  char msg_out[3] = "0";    /* Message a envoyer "0" a "99" */
  
  /* 3) Boucle emission-reception a particulariser selon que l'on est
     le serveur ou le client ..*/
  
  for(;;) {
    int i;
    struct sockaddr_in adr2,  *padr2 = &adr2; 
    printf("\n------------------\n");
    
    /* a) Reception */
    printf("Attente de reception ... ");
    if (recvfrom(sd0,msg_in,sizeof(msg_in),0, 
		 (struct sockaddr *)padr1, &ls) == -1) {
      printf("inachevee : %s !\n",msg_in);
    }
    else {
      adresse=inet_ntoa(adr1.sin_addr);
      famille=adr1.sin_family;
      port=adr1.sin_port;
      printf("terminee : valeur = %s !\n",msg_in);
      printf("Adresse client: %s \n",adresse);
      printf("Port client: %u \n",port);
      printf("Machine client: %d \n",famille);
    }  
    
    /* b) Traitement : La reception est bonne, on fait evoluer i */
    i = atoi(msg_in);
    i = (i+1)%100; 
    sprintf(msg_out,"%d",i);
    
    
    /* c) Emission */
    printf("\n\nEnvoi(%d) ... ", looptime);
    if (sendto(sd0,msg_out,strlen(msg_out)+1,0,
	       (struct sockaddr *)padr1,ls) >0)
      printf("termine : valeur = %s !\n",msg_out);
    else
      printf("inacheve : %s !\n",msg_out);
    
  }
  sleep(1);
  looptime++;
}
