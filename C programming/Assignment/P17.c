#include<stdio.h>
#include<math.h>
void main(){
    float a,b,c,s,area,n;
    scanf("%f %f %f",&a,&b,&c);
    s = (a+b+c)/2;
    n = s*(s-a)*(s-b)*(s-c);
    area = sqrt(n);
    printf("%f",area);

}