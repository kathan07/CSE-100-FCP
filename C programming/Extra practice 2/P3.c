# include<stdio.h>
void main()
{
    float time;
    printf("Enter Time");
    scanf("%f",&time);


    if (time<=12)
    {
        printf("Good Morning");
    }
    else if (time>12 && time<=15)
    {
        printf("Good afternoon");
    }
    else if (time>15 && time<=19)
    {
        printf("Good evening");
    }
    else{
        printf("Good night");
    }
}