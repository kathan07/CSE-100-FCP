#include<stdio.h>
#include<math.h>
void main(){
    char k[10];
    int n,g,l;
    float a;
    for (int i = 0; i < 10; i++)
    {
        printf("k[%d]: ",i);
        scanf("%d",&n);
        k[i]=n;
    }
    g = k[0];
    for (int j = 1; j < 10; j++)
    {
        if (k[j]>g)
        {
            g=k[j];
        }
        
    }
    l = k[0];
    for (int m = 1; m < 10; m++)
    {
        if (k[m]<l)
        {
            l = k[m];
        }
        
    }
    int sum;
    sum = 0;
    for (int f = 0; f < 10; f++)
    {
        sum = sum + k[f];
    }
    
    a = sum/10;
    
    printf("Maximum:%d",g);
    printf("\nMaximum:%d",l);
    printf("\nAverage:%f",a);
}