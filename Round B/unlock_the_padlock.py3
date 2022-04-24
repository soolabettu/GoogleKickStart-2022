# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round B - Problem C. Unlock the Padlock
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acef55
#
# Time:  O(N^2)
# Space: O(N^2)
#

from functools import lru_cache

def unlock_the_padlock():
    @lru_cache(None)
    def f(left, right, x):
        if left > right:
            return 0
        l = left
        while l <= right and V[l] == V[left]:
            l += 1
        r = right
        while r >= left and V[r] == V[right]:
            r -= 1
        return min(f(l, right, V[left])+min((V[left]-x)%D, D-(V[left]-x)%D),
                   f(left, r, V[right])+min((V[right]-x)%D, D-(V[right]-x)%D))

    N, D = map(int, input().split())
    V = list(map(int, input().split()))
    return f(0, N-1, 0)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, unlock_the_padlock()))