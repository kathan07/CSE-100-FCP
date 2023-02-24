#include<stdio.h>
void main()
{
	int i,n,j,c;
	c=1;
	n=4;
	for(i=0;i<n;i++){
		for(j=1;j<=i+1;j++){
			printf("%d ",c++);
		}
	printf("\n");
	}

}