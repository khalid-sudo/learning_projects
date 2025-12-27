def f(n):
    if n < 2:
        return n
    else:
        f(n-1) + fibonaci(n-2)
print(fibonaci(40))