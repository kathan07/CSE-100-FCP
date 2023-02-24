#include<stdio.h>
#include<stdlib.h>
void main(){
    FILE *fp;
    char c;
    int count;
    count = 0;
    fp = fopen("p36.txt","r");
    if (fp == NULL)
	{
		printf("Cannot open file \n");
		exit(0);
    }
    c = fgetc(fp);
    if (c=='A'||c=='E'||c=='I'||c=='O'||c=='U'||c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
    {
        count++;
    }
    
	while (c != EOF)
	{
		c = fgetc(fp);
		if (c=='A'||c=='E'||c=='I'||c=='O'||c=='U'||c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
        {
            count++;
        }
	}
    printf("%12d",count);

	fclose(fp);
}