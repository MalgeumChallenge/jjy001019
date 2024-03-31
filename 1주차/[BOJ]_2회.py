// https://www.acmicpc.net/source/71398373

import sys

n,m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
stack = []

num.sort()

def sequence():
    if len(stack) == m:
        print(' '.join(map(str,stack)))
        return
    
    for i in num:
        stack.append(i)
        sequence()
        stack.pop()
        
sequence()
