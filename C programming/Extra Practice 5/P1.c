#include <stdio.h>
#include<stdlib.h>

int main()
{
	FILE *fptr;

	char c;
    fptr = fopen("Login.txt", "r");
	if (fptr == NULL)
	{
		printf("Cannot open file \n");
		exit(0);
	}

	// Read contents from file
	c = fgetc(fptr);
	while (c != EOF)
	{
		printf ("%c", c);
		c = fgetc(fptr);
	}

	fclose(fptr);
	return 0;
}
