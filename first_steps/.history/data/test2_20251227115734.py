from functools impo
def fibonaci(n):
    if n < 2:
        return n
    else:
        return fibonaci(n-1) + fibonaci(n-2)
print(fibonaci(40))