#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char *argv[])
{
    printf("Total argument: %d",argc);
    int num1 = atoi(argv[2]);
    int num2 = atoi(argv[3]);
    if(strcmp((argv[1]),"add")==0)
    {
        printf("\nSum of given numbers: %d",num1 + num2);
    }
    else if(strcmp((argv[1]),"multiply")==0)
    {
        printf("\nMultiplication of given numbers: %d",num1 * num2);
    }
    else if(strcmp((argv[1]),"divide")==0)
    {
        printf("\nMultiplication of given numbers: %d",num1 / num2);
    }
    else if(strcmp((argv[1]),"subtract")==0)
    {
        printf("\nMultiplication of given numbers: %d",num1 - num2);
    }
    else
    {
        printf("Wrong operation!!");
    }
    return 0;
}
    