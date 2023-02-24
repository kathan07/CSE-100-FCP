#include<stdio.h>
#include<string.h>
void main(){
    char name[10],surname[10];
    printf("Enter your name: ");
    scanf("%s",name);
    printf("Enter your surname: ");
    scanf("%s",surname);
    strcat(name,surname);
    printf("Your name is: %s",name);
}