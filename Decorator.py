from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Took {t2 - t1}s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()

def print_info(**kwargs):
    # print(kwargs.values())
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York")
