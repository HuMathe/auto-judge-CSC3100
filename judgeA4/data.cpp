#include<map>
#include<ctime>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
int n, m, num;
std::map<std::pair<int, int>, int> M1, M2, Msum;
void printMatrix(FILE* handle, std::map<std::pair<int, int>, int>&M){
	fprintf(handle, "%d, %d", n, m);
	int i = 1;
	for(auto & [key, value] : M){
		if(value == 0) continue;
		if(i <= key.first) fprintf(handle, "\n");
		for(;i < key.first; ++i) fprintf(handle, "%d :\n", i);
		if(i == key.first) fprintf(handle, "%d ", i++);
		fprintf(handle, "%d:%d ", key.second, value);
	}
	if(i<=n)fprintf(handle, "\n");
	for(;i<=n; ++i) fprintf(handle, "%d :\n", i);
	return ;
}
int main(int argc, const char * argvs[]){
	srand(time(NULL));
	FILE* f1 = fopen("input1.in", "w");
	FILE* f2 = fopen("input2.in", "w");
	FILE* fans = fopen("stdop.out", "w");
	switch (argvs[1][0]){
	case '0': n = 3;m = 3;num = 3;break;
	case '1': n = 5;m = 5;num = 3;break;
	case '2': n = 3;m = 3;num = 20;break;
	case '3': n = 5;m = 5;num = 30;break;
	case '4': n = 10;m = 10;num = 50;break; 
	case 'A': n = 100;   m = 50;   num = 300; break;
	case 'B': n = 1000;  m = 500;  num = 30000; break;
	case 'C': n = 10000; m = 5000; num = 70000; break;
	case 'D': n = 100;   m = 50;   num = 100000; break;
	case 'E': n = 1000;  m = 500;  num = 100000; break;
	case 'F': n = 10000; m = 5000; num = 1000000; break;
	}
	for(int t = 1; t <= num; ++t){
		int i(rand()%n + 1), j(rand()%m + 1), k(1000 - rand()%2000);
		M1[std::pair<int, int>(i, j)] = k;
	}
	for(int t = 1; t <= num; ++t){
		int i(rand()%n + 1), j(rand()%m + 1), k(1000 - rand()%2000);
		M2[std::pair<int, int>(i, j)] = k;
	}
	for(auto & [key, value] : M1){
		Msum[key] = value;
	}
	for(auto & [key, value] : M2){
		if(Msum.count(key)) Msum[key] += value;
		else Msum[key] = value;
	}
	printMatrix(f1, M1);
	printMatrix(f2, M2);
	printMatrix(fans, Msum);
	fclose(f1);
	fclose(f2);
	fclose(fans);
	return 0;
}