class Register:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, tup):
        self.scores.append(tup)

    def __iter__(self):
        self.idx = 0
        return self
    
    def __next__(self):
        if self.idx < len(self.scores):
            x = self.idx
            self.idx += 1
            return self.scores[x][0]
        else:
            raise StopIteration
 

l = eval(input())

r = Register('0')
for i in l:
    r.add_score(i)

for name in r:
    print(name)