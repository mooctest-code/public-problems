from functools import lru_cache

@lru_cache(maxsize=0) # TODO: change maxsize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

n = int(input())
fib.cache_clear()
fib(n)
print('Hits:', fib.cache_info().hits)
    
