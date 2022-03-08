N, M = map(int, input().split())

 # N -> 20, M -> 40
NM = (N // 20) * (M // 40)

# M -> 20, N -> 40
MN = (N // 40) * (M // 20)

# ( N -> 20, M -> 40) & (M -> 20, N -> 40)
MN_n_NM = (N // 40) * (M // 40) * 2

print(NM+MN-MN_n_NM)