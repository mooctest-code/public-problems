'''TESTCASE
1 5 4 3 1
3
-
2 3 4 2 6 2 5 1
3
-
2 3 1 24 9 7 1 20 19 3 8 9 1 4 9 10 4
2
-
1 2 3
1
'''
from collections import deque

def findMaxs(arr, k):
    n = len(arr)
    Qi = deque() 
      
    for i in range(k): 
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop() 
    
        Qi.append(i); 
          
    ans = []
    for i in range(k, n): 
        ans.append(arr[Qi[0]])

        while Qi and Qi[0] <= i-k: 
            Qi.popleft()  

        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop() 
          
        Qi.append(i) 
    ans.append(arr[Qi[0]])
    return ans

print(*findMaxs(list(map(int, input().split())), int(input())))