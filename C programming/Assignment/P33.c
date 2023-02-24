#include<stdio.h>
#include<string.h>
void main(){
    char c[500],d[500];
    int i;
    printf("Enter first string: \n");
    gets(c);
    printf("\nEnter second string:\n");
    gets(d);
    i = strcmp(c,d);
    if (i==0)
    {
        printf("Boath the strings are same.");
    }
    else{
        printf("Strings are different.");
    }

}