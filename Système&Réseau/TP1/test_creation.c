/**  Fichier : test_creation.c */
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main(int argc, char *argv[]){
  int sd; /* Socket descriptor */

  /* Domaine Unix, virtual circuit (connection oriented), protocole
     TCP */
  printf("[AF_UNIX, SOCK_STREAM, IPPROTO_TCP] : \n");
  if ((sd=socket(AF_UNIX, SOCK_STREAM, IPPROTO_TCP)) == -1)
    perror("\t\tEchec");
  else
    printf("\t\tSocket creee\n");

  /* Domaine Internet, virtual circuit (connection oriented),
     protocole TCP */
  printf("[AF_INET, SOCK_STREAM, IPPROTO_TCP] : \n");
  if ((sd=socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1)
    perror("\t\tEchec");
  else
    printf("\t\tSocket creee\n");
  
  /* Domaine Internet, datagram (connectionless oriented), protocole
     par defaut */
  printf("[AF_INET, SOCK_DGRAM, 0] : \n");
  if ((sd=socket(AF_INET, SOCK_DGRAM, 0)) == -1)
    perror("\t\tEchec");
  else
    printf("\t\tSocket creee\n");
  
  /* Domaine Internet, datagram (niveau IP), protocole UDP */
  printf("[AF_INET, SOCK_RAW, IPPROTO_UDP] : \n");
  if ((sd=socket(AF_INET, SOCK_RAW, IPPROTO_UDP)) == -1)
    perror("\t\tEchec");
  else
    printf("\t\tSocket creee\n");
  
  /* Domaine XEROX_NS, datagram (improved connection oriented),
     protocole par defaut */
  printf("[AF_X25, SOCK_SEQPACKET, 0] : \n");
  if ((sd=socket(AF_X25, SOCK_SEQPACKET, 0)) == -1)
    perror("\t\tEchec");
  else
    printf("\t\tSocket creee\n");
  
  /* Domaine Internet, datagram (improved connectionless oriented),
     protocole par defaut */
  printf("[AF_INET, SOCK_RDM, 0] : \n ");
  if ((sd=socket(AF_INET, SOCK_RDM, 0)) == -1)
    perror("\t\tEchec");
  else
    printf("\t\tSocket creee\n");
}
