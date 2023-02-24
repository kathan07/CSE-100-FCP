#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, num;  //declare variables i, num
    int oddSum=0,evenSum=0;
    //declare and initialize variables oddSum,evenSum
    printf("Enter the value of num \n");
    scanf("%d",&num);
    for(i=1; i<=num; i++){// for loop use  to iterate 1 to num
        if(i%2==0)  //Check even number for sum
            evenSum=evenSum+i;
        else
            oddSum=oddSum+i;
    }
    printf("Sum of all odd numbers are: %d",oddSum);
    printf("\nSum of all even numbers are: %d",evenSum);
    getch();
    return 0;
}