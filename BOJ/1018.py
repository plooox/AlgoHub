import sys

sys.stdin = open("input.txt", "r")
##################################################################


def Chk(arr, x, y):
    BW_ref = [
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB'
    ]
    BW_cnt = 0
    for i in range(8):
        for j in range(8):
            if BW_ref[i][j] != arr[i+y][j+x]:
                BW_cnt += 1

    WB_ref = [
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW'
    ]

    WB_cnt = 0
    for i in range(8):
        for j in range(8):
            if WB_ref[i][j] != arr[i+y][j+x]:
                WB_cnt += 1

    return WB_cnt if WB_cnt < BW_cnt else BW_cnt


N, M = map(int, sys.stdin.readline().split())
tiles = [sys.stdin.readline().rstrip('\n') for _ in range(N)]

x_margin = M - 7
y_margin = N - 7

answer = N * M

for x in range(x_margin):
    for y in range(y_margin):
        curr = Chk(tiles, x, y)
        if answer > curr:
            answer = curr

print(answer)
