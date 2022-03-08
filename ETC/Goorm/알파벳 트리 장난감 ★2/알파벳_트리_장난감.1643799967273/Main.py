height = int(input())

tree = []
values = []

for i in range(height):
	tree.append(input())
	
def DFS(tree, idx, val, h, height):
	val += ord(tree[h][idx]) - ord('A') + 1
	
	if h+1 == height:
		values.append(val)
		return 
	else:
		DFS(tree, idx*2, val, h+1, height)
		DFS(tree, idx*2 + 1, val, h+1, height)
	
DFS(tree, 0, 0, 0, height)
print(min(values))
print(max(values))
