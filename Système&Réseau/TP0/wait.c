/** Fichier wait.c :   cr�ation/terminaison propre d'un processus :
    a) On cr�e un fils.
    b) Le p�re attend la fin de celui-ci en testant la condition de sa fin.

    On peut simuler une mauvaise fin en effectuant un 'kill' du
    processus fils.  */
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
int main(int argc, char *argv[]) {
  int exit_cond;
  pid_t pid;
  int temps= 2;
  int nb = 1;
  for (int i = 0; i < 6; i++) {
    if (pid > 0){
      temps += 5;
      pid = fork();
    }
  }

  switch (pid) {
  case -1 : perror("Erreur de cr�ation du processus");
    exit(1);
  case 0 : /* Ce code s'ex�cute chez le fils */
    printf("Pid du fils = %d\n", getpid());
    sleep(temps); /* Duree de vie du fils */
    break;
  default : /* Ce code s'ex�cute chez le p�re */
    printf("Pid du pere = %d\n", getpid());
    printf("Attente de la terminaison du fils...\n");

    while (nb < 6){
      nb ++;
      pid = wait(&exit_cond);
      if (WIFEXITED(exit_cond))
        printf("Le fils %d s'est termine correctement : %d\n", pid, WEXITSTATUS (exit_cond));
      else
	     printf("Le fils %d s'est mal termine : %d\n", pid, WTERMSIG (exit_cond));
     } /* switch */
   }
  exit(0);  /* ex�cut� par le fils et le p�re */
}
