#include<stdio.h>
#include<string.h>
void main(){
    char a[100],b[100];
    int c;
    printf("Enter first string: ");
    gets(a);
    printf("Enter number of caracters to be copied: ");
    scanf("%d",&c);
    strncpy(b,a,c);
    printf("%s",b);
}