N = int(input())

def dist (p1, p2):
	return abs(p1[0]-p2[0])**2 + abs(p2[1]-p1[1])**2

points = []
for _ in range(N):
	points.append(list(map(int,input().split())))

max_len = 0
ans1, ans2 = 0, 0
for i in range(N):
	for j in range(i+1, N):
		l = dist(points[i],points[j])
		if max_len < l:
			ans1 = i
			ans2 = j
			max_len = l
print(ans1+1,ans2+1)
			
	