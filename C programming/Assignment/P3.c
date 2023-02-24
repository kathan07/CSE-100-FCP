#include<stdio.h>
void main(){
    int n;
    printf("Enter your age: ");
    scanf("%d",&n);
    if (n>=18){
        printf("Your are eligible to vote.");
    }
    else
    {
        printf("You are not eligible to vote.");
    }
    
    
}