import time


def timethis(func):
    def wrapper(*args , **kwargs):
        print("Function Starts")
        start = time.time()
        f = func(*args , **kwargs)
        end = time.time()
        print("Function Ends")
        print("Time taken by this function is", end-start)
        return f

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


