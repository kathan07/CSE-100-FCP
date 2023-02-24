#include<stdio.h>
void main(){
    float a,b,c;
    scanf("%f %f %f",&a,&b,&c);
    if (a+b>=c)
    {
        if (a==b && b==c)
        {
            printf("It is an equilateral triangle");
        }
        else if (a==b||b==c||c==a)
        {
            printf("It is an isosceles triangle");
        }
        else{
            printf("It is an scalene triangle");
        }
        
        
    }
    else{
        printf("This triangle is not possible.");
    }
     
}