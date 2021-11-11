#include<queue>
#include<cstdio>
#include<cstring>
#include<algorithm>
struct node{
	int weight, depth;
	node(){}
	node(int times){
		weight = times;
		depth = 1;
	}
	bool friend operator < (node a, node b){
		if(a.weight != b.weight) 
			return a.weight > b.weight;
		return a.depth > b.depth;
	}
};
int has[128];
std::priority_queue<node> Q;
int main(){
	freopen("digit.u", "r", stdin);
	freopen("minlen.u", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; ++i){
		int c;
		scanf("%d", &c);
		has[c] += 1;
	}
	int word_count = 0;
	int tot_length = 0;
	for(int c = 0; c < 128; ++c)
		if(has[c]){
			Q.push(node(has[c]));
			word_count += 1;
		}
	if(word_count == 1){
		printf("%d\n", Q.top().weight);
		return 0;
	}
	while(word_count > 1){
		node l, r;
		l = Q.top();Q.pop();
		r = Q.top();Q.pop();
		tot_length += l.weight + r.weight;
		Q.push(node(l.weight + r.weight));
		word_count -= 1;
	}
	printf("%d\n", tot_length);
	return 0;
}