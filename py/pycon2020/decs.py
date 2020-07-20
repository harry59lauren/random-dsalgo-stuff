import functools
import time



def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Timed took : { end - start} ')
        return value
    return _wrapper

def trace(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        arguments = str(args)[:-1] + ',' + ','.join([f' {k}={v}' for k,v in kwargs.items()])
        print(f"Calling {func.__name__}{arguments})")
        value = func(*args, **kwargs)
        print(f'Returned : {value}')
        return value
    return _wrapper


fib = lambda n : 1 if n < 2 else fib(n - 1) + fib(n - 2)

@trace
def waste_time(num1, num2, **kwargs):
    total = 0
    for num in range(num1):
        total += sum(n for n in range(num))
    return total

waste_time(100, 200, ct=40, name="John")