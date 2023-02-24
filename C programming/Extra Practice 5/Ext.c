#include <stdio.h>
#include<string.h>
#include<stdlib.h>
void main(){
    char n[10];
    gets(n);
    int k;
    int j = 0;
    k = strlen(n);
    for (int i = 0; i < (k/2); i++)
    {
        if (n[i]==n[k-i-1])
        {
            j = 1;
        }
        else{
            exit(0);
        }
        
    }
    if (j==1)
    {
        printf("It is an palindrome");
    }
    else{
        printf("It is nat an palindrome");
    }
    
    
}