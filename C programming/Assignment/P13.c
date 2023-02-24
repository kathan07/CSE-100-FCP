#include<stdio.h>
void main(){
    int n,k,l;
    scanf("%d",&n);
    l = 0;
    k = 0;
    while (n>0)
    {
        k = n%10;
        n = n/10;
        l = l+k;
    }
    printf("%d",l);



}