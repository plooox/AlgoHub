#include <iostream>
#include <queue>
using namespace std;

int R,C;
char MAP[1001][1001] = {0,};
bool visited[1001][1001] = {false,};
int dy[4] = {-1,0,1,0};
int dx[4] = {0,1,0,-1};
int len = 0;
bool burned = false;

int start_R, start_C;
queue<pair<pair<int, int>,int>> q;

bool isBoundary(int r, int c)
{
	if(r < 0 || r >= R || c < 0 || c >= C){
		return false;
	}
	else{
		return true;
	}
}

void BFS()
{
	for(int i=0; i<R; i++)
	{
		for(int j=0; j<C; j++)
		{
			if(MAP[i][j] == '@')
			{
				q.push(make_pair(make_pair(i, j), len));
			}
		}
	}
	
	while(q.size() != 0)
	{
		int r = q.front().first.first;
	  int	c = q.front().first.second;
		int l = q.front().second;
		q.pop();
		
		if(!visited[r][c])
		{
			if(MAP[r][c] == '&')
			{
				len = l-1;
				burned = true;
				return;
			}
			// printf("%d %d\n",r,c);
			visited[r][c] = true;
			for(int i=0; i<4; i++)
			{
				int new_r = r + dy[i];
				int new_c = c + dx[i];
				
				if(isBoundary(new_r,new_c) && MAP[new_r][new_c] != '#' && visited[new_r][new_c] == false)
				{
					q.push(make_pair(make_pair(new_r,new_c),l+1));
				}
			}
		}
	}
	if(burned == false){
		len = -1;
	}
}

int main() {
	scanf("%d %d",&R, &C);
	getchar();
	
	for(int i=0; i<R; i++)
	{
		for(int j=0; j<C; j++)
		{
			scanf("%c", &MAP[i][j]);
			if(MAP[i][j] == '@')
			{
				start_R = i;
				start_C = j;
			}
		}
		getchar();
	}
	
	BFS();
	printf("%d\n",len);
	
	return 0;
}