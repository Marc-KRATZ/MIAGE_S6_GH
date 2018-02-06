/** Fichier : sock_unix.c */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>

/* Nombre max de socket creables par ce pgm */
#define NB_MAX 64
/* Adresse servant au nommage de la socket  */
struct sockaddr_un adresse;

/* Creation et nommage de sockets dans le domaine UNIX */
/* Passage en parametre des noms d'attachement         */
int main(int argc, char *argv[]){
  int desc[NB_MAX];
  int i, nb_sock;

  /* Nombre de sockets a creer. */
  nb_sock=(argc>NB_MAX+1)?NB_MAX:argc-1;

  /* Type : AF_UNIX             */
  adresse.sun_family = AF_UNIX;

  for(i=0; i<nb_sock ; i++){
      /* ---- Creation de la ieme socket --------- */
      if((desc[i]=socket(AF_UNIX,SOCK_STREAM,0)) == -1){
	  perror("socket");
	  exit(1);
	}
      else
	printf("socket %d creee ! \n",i);

      /* On recupere l'adresse numero i (dans les arguments) */
      memcpy(adresse.sun_path,argv[i+1],strlen(argv[i+1]));

      /* ---- Attachement de la ieme socket ------ */
      if(bind(desc[i], (struct sockaddr *)&adresse, sizeof(adresse)) == -1){
	perror(argv[i+1]);
	continue;
      }
  }
  /* on attend 60 secondes avant de sortir ... pour les voir sous netstat */
  sleep(60);
}
