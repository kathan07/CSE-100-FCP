#include <stdio.h>
int main() {
  float first, second, n, sum , mul , div , sub;
  printf("For '+' press 1\n");
  printf("For '-' press 2\n");
  printf("For '*' press 3\n");
  printf("For '/' press 4\n");
  scanf("%f",&n);
  printf("Enter two operands: \n");
  scanf("%f %f", &first, &second);
  if (n==1){
    sum = first + second;
    printf("Sum of two numbers is equal to: %f", sum);
  }
  if (n==2){
    sub = first - second;
    printf("Subtraction of two numbers is equal to: %f", sub);
  }
  if (n==3){
    mul = first * second;
    printf("Multiplication of two numbers is equal to: %f", mul);
  }
  if (n==4){
    div = first/second;
    printf("Division of two numbers is equal to: %f", div);
  }


  return 0;
}