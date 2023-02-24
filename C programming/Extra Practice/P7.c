#include<stdio.h>
#include<string.h>
int main()
{
 char name[20], address[80];

 printf("Enter your name:");
 gets(name);

 printf("Enter your address:");
 gets(address);

 printf("=====================\n");
 printf("Your name: %s \n",name);
 printf("Your address: %s\n", address);
 printf("=====================\n");
 return 0;
}