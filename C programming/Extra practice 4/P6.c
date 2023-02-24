#include<stdio.h>
#include<string.h>
void main(){
    char name[30];
    int k ;
    printf("Enter your name: ");
    scanf("%s",name);
    k = strlen(name);
    for (int i =0 ; i <k; i++)
    {
        printf("%c",name[i]-32);
    }
    

}