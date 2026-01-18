def fibonaci(n):
    if n < 2:
        return n
    else:
        return fibonaci(n-1) + fibonaci(n-2)
print(fibonaci(40))

#optimized without cache
def fib(n, computed={0: 0, 1: 1}):

    if n not in computed:

        computed[n] = fib(n - 1, computed) + fib(n - 2, computed)

    return computed[n]