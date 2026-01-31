#include <stdio.h>
#include <string.h>

int main() {

    char adj1[50] = "";
    char noun[50] = "";
    char adj2[50] = "";
    char verb[50] = "";
    char adj3[50] = "";

    printf("Enter an adjective (description): ");
    fgets(adj1, sizeof(adj1), stdin);
    adj1[strlen(adj1) - 1] = '\0';

    printf("Enter a noun (animal or person): ");
    fgets(noun, sizeof(noun), stdin);
    noun[strlen(noun) - 1] = '\0';

    printf("Enter an adjective (description): ");
    fgets(adj2, sizeof(adj2), stdin);
    adj2[strlen(adj2) - 1] = '\0';

    printf("Enter a verb (ending in -ing): ");
    fgets(verb, sizeof(verb), stdin);
    verb[strlen(verb) - 1] = '\0';

    printf("Enter an adjective (description): ");
    fgets(adj3, sizeof(adj3), stdin);
    adj3[strlen(adj3) - 1] = '\0';


    printf("Today I went to a %s zoo.\nIn an exhibit, I saw a %s.\n%s was %s and %s!\nI was %s!", adj1, noun, noun, adj2, verb, adj3);



    return 0;
}