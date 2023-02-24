#include<stdio.h>
void main(){
    int l,m,n;
    scanf("%d",&l);
    scanf("%d",&m);
    scanf("%d",&n);
    if (l>=m && l>=n)
    {
        printf("%d",l);
    }
    else if (m>=l && m>=n)
    {
        printf("%d",m);
    }
    else if (n>=m && n>=l)
    {
        printf("%d",n);
    }
    
}