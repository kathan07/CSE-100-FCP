#include<stdio.h>
void main(){
    // 2, 4, 6, 8, ..... 100
    for (int i = 2; i <= 100; i+=2)
    {
        printf("%d ",i);
    }
    printf("\n");
    // 100, 90, 80, 70, ......., 10
    for (int i = 100; i >0; i-=10)
    {
        printf("%d ",i);
    }
    printf("\n");
    // 1, 3, 5, 7........99
    for (int i = 1; i < 100; i+=2)
    {
        printf("%d ",i);
    }
    printf("\n");
    //2, 4, 8, 16, 32, 64, 128, 256
    for (int i = 2; i <= 256; i=i*2)
    {
        printf("%d ",i);
    }
    
}