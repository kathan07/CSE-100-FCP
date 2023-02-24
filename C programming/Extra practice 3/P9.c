#include<stdio.h>
int main()
{
	int num,sum=0,i,k;
	printf("Enter Postive numbers to sum:");
	scanf("%d",&num);
	i = 0;
	while(i<num)
	{
		scanf("%d",&k);
		if(k<0)
		{
			break;
		}
		sum=sum+k;
		i++;
	}
	printf("%d",sum);
	return 0;
}