/*
* DO NOT MODIFY THIS FILE
*/
#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
int LeN = 102400;
int main(){
	FILE *fascii = fopen("input.u", "w");
	FILE *fdigit = fopen("digit.u", "w");
	srand(time(NULL));
	int len = LeN;
	fprintf(fdigit, "%d\n", len);
	for(int i = 1; i <= len; ++i){
		int c = rand() % 32;
		if(c == 10) c = 13;
		fprintf(fascii, "%c", c);
		fprintf(fdigit, "%d ", c);
	}
	fclose(fascii);
	fclose(fdigit);
	return 0;
}