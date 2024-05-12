// https://www.acmicpc.net/source/71341176

import sys

E,S,M = map(int, sys.stdin.readline().split())

for i in range(1,15*28*19+2):
    if i%15==0:
        e=15
    else:
        e=i%15
    
    if i%28==0:
        s=28
    else:
        s=i%28
    
    if i%19==0:
        m=19
    else:
        m=i%19
    
    if (e==E) and (s==S) and (m==M):
        print(i)
        break
