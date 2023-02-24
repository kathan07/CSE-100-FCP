#include<stdio.h>
void main(){
    int n,i,sum;
    sum=0;
    n=100;
    i=1;
    do
    {
        sum = sum+i;
        i++;
    } while (i<=100);
    printf("%d",sum);
    
}