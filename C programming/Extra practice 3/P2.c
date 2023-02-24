#include<stdio.h>
void main(){
    int n,i,sum;
    sum=0;
    n=50;
    i=1;
    while(i<=n){
        sum = sum + i;
        i++;
    }
    printf("%d",sum);
}