n = int(input())
num_list = [0]+list(map(int, input().split()))
dp = [0] * (len(num_list)+1)
max_value = 0
for i in range(1,len(num_list)):
	dp[i] = max(dp[i-1] + num_list[i], num_list[i])
	max_value = max(max_value, dp[i])
print(max_value)
	