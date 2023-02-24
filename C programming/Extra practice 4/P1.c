#include<stdio.h>
void main(){
    int num[5],i;
    for (i = 0; i < 5; i++)
    {
        printf("Enter num[%d]: ",i);
        scanf("%d",&num[i]);
    }
    for ( i = 0; i < 5; i++)
    {
        printf("num[%d] = %d  ",i,num[i]);
    }
    
    
}
