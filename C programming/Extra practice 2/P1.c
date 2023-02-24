# include<stdio.h>
int main(){
    float num;
    printf("Enter a number: ");
    scanf("%f", &num );
    if (num>=0){
        printf("It is an positive number");
    }
    if (num<0) {
        printf("It is a negative number");
    }
    return 0;

}