# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list

def multiply_by2(li):
    return li * 2

def filter_by2(li):
    return li % 2 == 0

# new_list = multiply_by2([1,2,3,4,5])
# print(new_list)

arr = [1,2,3,4,5]
# new_list = list(map(multiply_by2,arr))
# new_list = list(map(lambda x: x*3,arr))
new_list = map(lambda x: x*3,arr)
new_list_filter = filter(filter_by2,arr)
# new_list_filter = filter(lambda x: x % 2 == 0,arr)

from functools import reduce
total_list = reduce(lambda x, y:  x + y,arr, 0)
print(list(new_list))
print(list(new_list_filter))
print(total_list)

mylist = [char + 'a' for char in 'Hello']
print(mylist)