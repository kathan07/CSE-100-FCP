#include<stdio.h>
void main()
{
    int n;
    float rem;
    printf("Enter a number: ");
    scanf("%d", &n);
    rem = n%2;
    if (rem=0){
        printf("%d is an even number",n);
    }
    else{
        printf("%d is an odd number",n);
    }
}