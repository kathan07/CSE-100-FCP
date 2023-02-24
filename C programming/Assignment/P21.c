#include<stdio.h>
#include<string.h>
void main(){
    char c[100];
    gets(c);
    strrev(c);
    printf("%s",c);
}