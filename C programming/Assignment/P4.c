#include<stdio.h>
void main(){
    float l,k,m,n;
    printf("Enter value of three angles: ");
    scanf("%f",&k);
    scanf("%f",&m);
    scanf("%f",&n);
    l = k+m+n;
    if (l==180)
    {
        printf("It is a Triangle");
    }
    else{
        printf("It is not a triangle");
    }
    
}