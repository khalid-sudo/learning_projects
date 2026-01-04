import functools
#hello world
@functools.cache
def fibonaci(n):
    """fibonachi function"""
    if n < 2:
        return n
    else:
        return fibonaci(n-1) + fibonaci(n-2)
print(fibonaci(40))