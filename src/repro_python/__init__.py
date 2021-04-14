__version__ = '0.1.0'

def fibo(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b