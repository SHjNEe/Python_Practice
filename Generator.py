def gen_function(num):
    for item in range(num):
        yield item * 2

# g = gen_function(20)

# next(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# print(list(gen_function(10))) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# for item in gen_function(10):
#     print(item)
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        result = t2 - t1
        print(result)
    return wrapper

@performance
def long_time(num):
    print('Start')
    for i in range(num):
        i * 5
    print('End')
    

long_time(2000000)