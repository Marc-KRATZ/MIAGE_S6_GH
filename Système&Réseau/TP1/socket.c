#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

main()
{
int d[6];
/* Domaine Unix, virtual circuit (connection oriented), protocole TCP*/
if ((d[0]=socket(AF_UNIX, SOCK_STREAM, IPPROTO_TCP)) == -1)
  perror("[SOCK_STREAM, A_UNIX, IPPROTO_TCP]");
else
  printf("socket [SOCK_STREAM, AF_UNIX, IPPROTO_TCP] creee\n");
/* Domaine Internet, virtual circuit (connection oriented), protocole TCP*/
if ((d[1]=socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1)
  perror("[SOCK_STREAM, A_UNIX, IPPROTO_TCP]");
else
  printf("socket [SOCK_STREAM, AF_INET, IPPROTO_TCP] creee\n");
/* Domaine Internet, datagram (connectionless oriented), protocole par defaut*/
if ((d[2]=socket(AF_INET, SOCK_DGRAM, 0)) == -1)
  perror("[SOCK_DGRAM, AF_INET, 0]");
else
  printf("socket [SOCK_DGRAM, AF_INET, 0] creee\n");
/* Domaine Internet, datagram (niveau IP), protocole UDP */
if ((d[3]=socket(AF_INET, SOCK_RAW, IPPROTO_UDP)) == -1)
  perror("[SOCK_RAW, AF_INET, IPPROTO_UDP]");
else
  printf("socket [SOCK_RAW, AF_INET, IPPROTO_UDP] creee\n");
/* Domaine XEROX_NS, datagram (improved connection oriented), protocole par defaut*/
if ((d[4]=socket(AF_NS, SOCK_SEQPACKET, 0)) == -1)
  perror("[SOCK_SEQPACKET, AF_NS, 0]");
else
  printf("socket [SOCK_SEQPACKET, AF_NS, 0] creee\n");
/* Domaine Internet, datagram (improved connectionless oriented), protocole par defaut*/
if ((d[5]=socket(AF_INET, SOCK_RDM, 0)) == -1)
  perror("[SOCK_RDM, AF_INET, 0]");
else
  printf("socket [SOCK_RDM, AF_INET, 0] creee\n");
}
