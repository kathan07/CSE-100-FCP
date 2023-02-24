#include<stdio.h>
int main(){
    float n1,n2,sum;
    int c;
    printf("Enter n1: ");
    scanf("%f",&n1);
    printf("Enter n2: ");
    scanf("%f",&n2);
    sum = n1+n2;
    c = (int)sum;
    printf("Sum: %d , sum: %f",c,sum);
    return 0;
}