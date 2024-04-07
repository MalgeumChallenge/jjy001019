// https://www.acmicpc.net/problem/1748
import sys

N = int(sys.stdin.readline().strip('\n'))

if len(str(N)) == 1:
    print(N)
else:
    standard = 10**(len(str(N))-1)
    ans_1 = 0
    ans_2 = (N - standard + 1)*len(str(N))
    for i in range(1,len(str(N))):
        ans_1 += i*(9*(10**(i-1)))
    print(ans_1+ans_2)
