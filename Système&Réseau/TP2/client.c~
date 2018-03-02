/** Fichier : inc.c (Communication Sockets/UDP)
 *   Les deux processus distants s'envoient un nombre qu'ils 
 *   incrementent successivement : L'un compte en pair, l'autre en impair ...  */
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

#define PORT 6666
#define MAXBUFFER 10

int main(int argc, char *argv[]){ 
 int sock = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP);
    if (sock ==-1) {
        perror("socket");
        exit(0);
    }
 
    if(fork()!=0){
 	
        struct sockaddr_in si;
        si.sin_family = AF_INET;
        si.sin_addr.s_addr = inet_addr(argv[1]);
        si.sin_port = htons(PORT);
 
        while(1){
            char buff[MAXBUFFER];
            //gets(buff);
            printf("recu \n");
            ssize_t message = sendto(sock, buff,strlen(buff)+1,0,(struct sockaddr *)&si,sizeof(si));
            if (message ==-1)
                perror("sendto\n");
        }
    }
 
    else {
        while(1){
            char buff[MAXBUFFER];
            ssize_t recu = recvfrom (sock,buff,sizeof(buff)+1, 0,NULL,0);
            if (recu==-1)
                perror("erreur recvfrom\n");
            else
                printf("message = %s\n",buff);
        }
    }
 
    close(sock);
 
    return 0;
}

