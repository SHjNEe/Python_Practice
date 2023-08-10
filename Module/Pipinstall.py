from pyjokes import get_joke

# Get a random joke
# joke = get_joke('en', 'neutral')
# print(joke)

from collections import Counter, defaultdict, OrderedDict


li = [1,1,3,4,5,6,7,8,9,10]
print(Counter(li))
sentence = 'Blah ......'
print(Counter(sentence))
# Counter({1: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1})
# Counter({'.': 6, 'B': 1, 'l': 1, 'a': 1, 'h': 1, ' ': 1})
# print(defaultdict(li))
# print(OrderedDict(li))


dictionary2 = defaultdict(lambda: 'Does not exist',{'a':1, 'b':2, 'c':3, 'd': 4})
print(dictionary2['asass']) #Does not exist

dictionary3 = OrderedDict()
dictionary3['a'] = 1
dictionary3['b'] = 2

print(dictionary3)

import datetime

print(datetime.date.today())