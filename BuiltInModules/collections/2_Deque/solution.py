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