num = int(input())
isSecret = True

while num > 1:
	num, m = divmod(num, 2)
	
	if m > 0:
		isSecret = False
		break

if isSecret:
	print("Yes")
else:
	print("No")