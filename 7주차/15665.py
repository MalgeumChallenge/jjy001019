https://www.acmicpc.net/problem/15665

import sys

n,m = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))
stack = []

def sequence():
    if len(stack) == m:
        print(*stack)
        return
    
    past = 0
    
    for i in range(n):
        if past != num[i]:
            past = num[i]
            stack.append(num[i])
            sequence()
            stack.pop()
            
sequence()
