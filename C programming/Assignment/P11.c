#include<stdio.h>
void main(){
    char c;
    scanf("%c",&c);
    if (c>='A' && c<='Z'){
        printf("It is in Upper case.");
    }
    else if (c>='a' && c<='z') {
        printf("It is in lower case.");
    }
}