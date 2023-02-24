#include <stdio.h>
int main(){
    float perc;
    int Rollno;
    printf("Enter Rollno:");
    scanf("%d", &Rollno);
    printf("Enter marks: ");
    scanf("%f", &perc);
    printf("Rollno:%d,percentage:%f",Rollno,perc);
    return 0;
}