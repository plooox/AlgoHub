N, S = map(int, input().split())
arr = list(map(int, input().split()))
hong, members = arr[0], arr[1:]
cnt = 0

def dfs(idx, tar):
	global cnt
	if idx == N-1:
		if tar == S:
			cnt +=1
		return
	else:
		dfs(idx+1, tar)
		dfs(idx+1, tar+members[idx])

dfs(0, hong)
print(cnt)