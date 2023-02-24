#include<stdio.h>
void main(){
    int row,col, arr[3][3];
  //Logic to read matrix 
  for(row=0; row<3; row++) // rows
  {
    for(col=0; col<3; col++) //columns
    {
       printf("Enter matrix number[%d][%d]:", row+1, col+1);
       scanf("%d", &arr[row][col]);
    }
  }
  //Logic to print matrix
  printf("The 3 X 3 matrix:\n");
  for(row=0; row<3; row++) // rows
  {
    for(col=0; col<3; col++) //columns
    {
       printf("%d ", arr[row][col]);
    }
    printf("\n");
  }
}