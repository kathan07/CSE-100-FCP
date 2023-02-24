#include <stdio.h>
#include <stdlib.h> // For exit()

int main()
{
	FILE *fp;
    char c;
    int count = 0;
	// Open file
	fp = fopen("Login.txt", "r");
	if (fp == NULL)
	{
		printf("Cannot open file \n");
		exit(0);
	}

	c = fgetc(fp);
	while (c != EOF)
	{
		count++;
		c = fgetc(fp);
	}
    fclose(fp);
    printf("%d",count);
	return 0;
}
