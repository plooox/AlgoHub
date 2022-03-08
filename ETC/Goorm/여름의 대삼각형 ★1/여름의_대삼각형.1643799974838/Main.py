x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

S = abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))/2

print("{0:.2f}".format(S))