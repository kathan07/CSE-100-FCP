#include <stdio.h>
#include <String.h>
int main(){
	int a;
    char b;
	FILE *fp1,*fp2;
	fp1 = fopen("odd.txt","w");
	fp2 = fopen("even.txt","w");
	scanf("%d",&a);
	if (a%2==0){
        b = (float)(a);
		putw(a,fp2);
	}
	else{
        b = (float)(a);
		putw(a,fp1);
	}
    fclose(fp1);
    fclose(fp2);
}
