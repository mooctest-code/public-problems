import queue

n = int(input())

q = queue.PriorityQueue()
q.put(1)
s = set()
s.add(1)
c = [2, 3, 5]

for i in range(n-1):
    k = q.get()
    for j in range(3):
        x = c[j] * k
        if x not in s:
            s.add(x)
            q.put(x)

print(q.get())