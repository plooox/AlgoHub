N = int(input())
tree = []
num_tree = [[0 for _ in range(N+2)]]
max_value_tree = [[0 for _ in range(N+2)] for _ in range(N+1)]
# Read tree
for _ in range(N):
	tree.append(list(input()))

# Read character => integer value
for tree_h in tree:
	n = len(tree_h)
	num_list = [0]
	for ch in tree_h:
		num_list.append(ord(ch) - 64)
	for _ in range(N-n+1):
		num_list.append(0)
	num_tree.append(num_list)
	

for i in range(1,N+1):
	for j in range(1, N+1):
		max_value_tree[i][j] = max(num_tree[i][j]+max_value_tree[i-1][j],
												 num_tree[i][j]+max_value_tree[i-1][j-1])
print(max(max_value_tree[-1]))
