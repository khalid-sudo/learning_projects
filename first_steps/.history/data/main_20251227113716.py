n =100

def fibonaci(n: float):
    if n < 2:
        return n
    else:
        fibonaci(n-1) + fibonaci(n-2)
print