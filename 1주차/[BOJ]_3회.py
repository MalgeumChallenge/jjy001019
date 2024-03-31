// https://www.acmicpc.net/source/71099767

import sys

N = int(sys.stdin.readline())
cards = [i for i in range(1,N+1)]

while len(cards) > 1:
    if len(cards)%2 == 0:
        cards = cards[1::2]
    else:
        cards.append(cards[1])
        cards = cards[1::2]
        cards.pop(0)

print(cards[0])
