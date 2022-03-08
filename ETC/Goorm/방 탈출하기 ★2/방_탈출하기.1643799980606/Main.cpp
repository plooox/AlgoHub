#include <iostream>
#include <map>
using namespace std;

map<int, int> arr;
int N, M;
int num;

int main() {
	
	scanf("%d",&N);
	for(int i=0; i<N; i++)
	{
		scanf("%d",&num);
		arr[num] = 1;
	}
	
	scanf("%d", &M);
	for(int i=0; i<M; i++)
	{
		scanf("%d",&num);
		printf("%d\n",arr[num]);
	}
	
	return 0;
}