from functools import reduce
print(reduce(lambda x,y: x+y, eval(input())))