import heapq

N = int(input())

arr = []
heap = []
move = 0
cur = 1

for _ in range(N*2):
	init_input = input()
	
	if init_input == "remove":
		cmd = init_input
	else:
		cmd, num = init_input.split()
		num = int(num)	
	
	if cmd == "add":
		# print("add -> ", end='')
		arr.append(num)
	
	if cmd == "remove":
		# print("remove -> ", end='')
		if len(arr) != 0:
			if arr[-1] == cur:
				arr.pop()
			else:
				# print("(move) ",end='')
				move += 1
				for ele in arr:
					heapq.heappush(heap, ele)
				arr = []
				heapq.heappop(heap)
		else:
			if len(heap) != 0:
				heapq.heappop(heap)
		cur += 1
	# print(arr, heap)

print(move)


# for _ in range(N*2):
# 	init_input = input()
	
# 	if init_input == "remove":
# 		cmd = init_input
# 	else:
# 		cmd, num = init_input.split()
# 		num = int(num)	
	
# 	if cmd == "add":
# 		arr.append(num)
	
# 	if cmd == "remove":
# 		if arr[-1] == cur:
# 			arr.pop()
# 		else:
# 			move += 1
# 			arr = sorted(arr, reverse=True)
# 			arr.pop()
# 		cur += 1