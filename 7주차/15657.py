// https://www.acmicpc.net/problem/15657

import sys

n,m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
stack = []
num.sort()

def sequence():
    if len(stack) == m:
        print(*stack)
        return
    
    for i in num:
        if (len(stack)==0) or (i>=stack[-1]):
            stack.append(i)
            sequence()
            stack.pop()
            
sequence()
