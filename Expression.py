import re

pattern = re.compile('This is dummy string what i dummyyy cant write anythings')

string = 'This is dummy string what i dummyyy cant write anythings'

# print('dummy' in string)
print((pattern.search(string)))
print((pattern.findall(string)))
print((pattern.fullmatch(string)))
print((pattern.match(string)))