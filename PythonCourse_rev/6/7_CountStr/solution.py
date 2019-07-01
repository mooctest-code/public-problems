'''TESTCASE
Python C Java Go Java PHP Python Java
-
python php python java rust php ruby
-
python
-
test TEST tesT Test
'''


def count_str(s: str):
    d = {}
    for i in s.split():
        d.setdefault(i, 0)
        d[i] += 1
    return d


d = count_str(input().lower())
cnt = sorted(d.items(), key=lambda x: x[0])
for i in cnt:
    print(i[0], i[1])

cnt = sorted(cnt, key=lambda x: (x[1], x[0]), reverse=True)
for i in cnt:
    print(i[0], i[1])
