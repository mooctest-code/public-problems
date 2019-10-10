'''TESTCASE
4
0.5 0.6 0.4 0.5
60 40 80 60
100
-
5
0.5 0.6 0.4 0.5 0.4
60 40 80 60 80
100
-
8
0.5 0.3 0.5 0.5 0.8 0.5 0.3 0.4
40 80 60 30 40 40 40 40
200
-
2
0.4 0.4
50 50
100
-
1
0.5
100
100
-
3
0.4 0.3 0.5
20 20 20
100
'''
import queue

n = int(input())
hit = list(map(float, input().split()))
hurt = list(map(float, input().split()))
blood = int(input())
pdie = 0


def dfs(x, h, p):
    global pdie
    if x == n:
        if h >= blood:
            pdie += p
        return
    dfs(x+1, h+hurt[x], p * hit[x])
    dfs(x+1, h, p*(1-hit[x]))


dfs(0, 0, 1)
print('{:.4f}'.format(pdie))
