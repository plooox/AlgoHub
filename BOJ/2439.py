N = int(input())
for i in range(N):
    blank = ' ' * (N-1-i)
    star = '*' * (i+1)
    print(blank+star)
