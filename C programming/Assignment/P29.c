#include <stdio.h>
int Square(int n1){
	int m=n1*n1;
	return m;
}
int main(){
	int a;
	printf("Enter a number : \n");
	scanf("%d",&a);
	printf("The square of the number you wrote is = %d",Square(a));
}
