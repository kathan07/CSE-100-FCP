#include<stdio.h>
#include<string.h>
void main(){
    char k[100];
    gets(k);
    strlwr(k);
    printf("%s",k);
}