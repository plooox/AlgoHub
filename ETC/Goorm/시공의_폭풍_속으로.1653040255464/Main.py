isPicked = [False for _ in range(88)]

champ = list(map(int, input().split()))

for ele in champ:
	isPicked[ele] = True

want = list(map(int, input().split()))
result = 0
for ele in want:
	if not isPicked[ele]:
		result += 1
print(result)