// https://www.acmicpc.net/problem/10989

import sys

N = int(sys.stdin.readline().strip('\n'))
result = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline().strip('\n'))
    result[num] += 1
    
for idx, freq in enumerate(result):
    for _ in range(freq):
        print(idx)
