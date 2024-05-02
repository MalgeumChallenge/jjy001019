// https://www.acmicpc.net/problem/3474

import sys

test_case = int(sys.stdin.readline().strip('\n'))

for _ in range(test_case):
    n = int(sys.stdin.readline().strip('\n'))
    max_5 = 0
    num_5 = 0
    while 5**max_5 <= n:
        max_5 += 1
    max_5 -= 1
    for i in range(1,max_5+1):
        num_5 += n//(5**i)
    print(num_5)
