#include<stdio.h>
int main(){
	char a;
	FILE *f1,*f2;
	f1 = fopen("file1.txt","r");
	f2 = fopen("file2.txt","a");
    printf("\n");
	for(int i=0;i<9999999;i++){
		char a = fgetc(f1);
		if(a==EOF){
			break;
		}
		else{
		fputc(a,f2);
	}
	}
	fclose(f1);
	fclose(f2);
}
