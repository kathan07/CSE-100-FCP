#include<stdio.h>
#include<string.h>
void main(){
    char n[100];
    int k;
    scanf("%s",n);
    k = strlen(n);
    strrev(n);
    for (int i = 0; i < k; i++)
    {
        printf("%c ",n[i]);
    }
    
    

}