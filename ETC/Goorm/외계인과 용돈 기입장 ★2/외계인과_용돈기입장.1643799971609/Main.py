N,M = map(int, input().split())
money = list(map(int, input().split()))
sub_sum = [0]*(len(money)+1)

for i in range(1, N+1):
	sub_sum[i] = sub_sum[i-1] + money[i-1]

for _ in range(M):
	start, end = map(int, input().split())
	val = sub_sum[end] - sub_sum[start-1]
	
	if val > 0:
		print('+'+str(val))
	else:
		print(val)
		