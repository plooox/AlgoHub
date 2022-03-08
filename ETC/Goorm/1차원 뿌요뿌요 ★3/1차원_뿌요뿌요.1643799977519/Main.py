N, M = map(int, input().split())
S = input() + '#';
idx = 0
stack = []

# for i in range(0, len(S)):
# 	#print(stack)
# 	if len(stack) == 0:
# 		stack.append([S[i], 1])
# 	else:
# 		if(stack[-1][0] == S[i]):
# 			stack[-1][1] += 1
# 		else:
# 			if(stack[-1][1] >= M):
# 				stack.pop()
# 				i -= 1
# 			else:
# 				stack.append([S[i],1])
					
while idx < len(S):
	if(len(stack) == 0):
		stack.append([S[idx],1])
	else:
		if(stack[-1][0] == S[idx]):
			stack[-1][1] += 1
		else:
			if(stack[-1][1] >= M):
				stack.pop();
				idx -= 1
			else:
				stack.append([S[idx],1])
	idx += 1	

stack.pop()

if(len(stack) == 0):
	print("CLEAR!")
else:
	for ele in stack:
		for _ in range(ele[1]):
			print(ele[0],end='')
