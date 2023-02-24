#include <stdio.h>
int main(){
	int a [10][10] ,sum=0 ;
	printf("Enter elements of 4*4 matrix :\n");
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			scanf("%d",&a[i][j]);
	}
  }
  for (int k=0;k<4;k++){
  	 sum=sum+a[k][k] ;
  }
  printf("The sum of diagonal elements of the matrix are : %d",sum);
}
