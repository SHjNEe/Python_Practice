# file = open('item.txt')
# # print(file)
# # help(open)

# fileContent = file.read(2222)
# print(fileContent)
# # file.close()
# fileContent2 = file.read(2222)
# print(fileContent2)


# def some_random_stuff():
#     print('hello from function'.capitalize())
  

# def test(a):
#     print('''hello from''')

# def is_odd(number):
#     number = int(number)
#     result = 'Is Odd' if number % 2 == 1 else 'This number is even'
#     print(result)


# inputNumber = input('Please input want to check : ')
# is_odd(inputNumber)

# *args, **kwargs
# def super_function(*args, **kwargs):
#     print(kwargs, kwargs.values())
#     return sum(list(args)) + sum(kwargs.values())

# result = super_function(1,2,3,4, num1 = 5, num2 =10)
# print(result)


# def highest_even(li):
#     evens = []
#     for item in li:
#         if item % 2 == 0:
#             evens.append(item)
#     return max(evens)        

# print(highest_even([1,2,3,4,5]))

# print(f"{(n := input('Please enter your name? : '))}")
# print(f'{(n := input("Please enter your name? : "))}')

# a = 100

# def newNumb():
#     global a
#     a += 200
#     return "hihi"

# newNumb()

# print(a)

# def inner():
#     str = 'Test'
#     def converStr():
#         nonlocal str
#         str = 'Hihii'
#         print(str)
#     converStr()    
#     print(str)

# inner()


# class Car():
#     membership =  True
#     def __init__(self, name, model, year):
#         if(Car.membership):
#             self.name = name
#             self.model = model
#             self.year = year
#     def run(self):
#         print('Run...')
#         print('Done...')
#     def shout(self):
#         print(f'My name is {self.name}')

#     @classmethod
#     def some_thing(cls, name, model, year):
#         return cls(f'Hello {name}', model, year)
#     def info(self):
#         print(self.name)

#     @staticmethod
#     def static_method():
#         print('Static is call')

# # mercedes = Car.some_thing('Mercedes', 'Tesla', 2021)

# # mercedes.info()
# # Car.run()

# Car.static_method()

# class PlayerCharacter():
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     def run(self):
#         print('Run...')
#         print('Done...')
#     def shout(self):
#         print(f'My name is {self._name}')

# player1 = PlayerCharacter('Andrei', 30)


# # player1.shout = 'HIHIHI'
# player1.name = 'HIHIHI'

# print(player1.name)

class User:
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('Loged in...')
    def sign_out(self):
        print('Loged out...')
    def attack(self):
        print('Do nothing....')

class Wizard(User):
    def __init__(self, name, power,email):
        self.name = name
        # User.__init__(self, email)
        super().__init__( email)
        self.power = power
    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, number_arrows,email):
        # User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.number_arrows = number_arrows
        
    def attack(self):
        print(f'Attacking with arrow of {self.number_arrows}')



wizard1 = Wizard('Merlin', 40, 'merlin@gmail.com')
# wizard1.attack()
# wizard1.sign_out()
# print('_______________')
archer1 = Archer('Hercules', 100, 'archer@gmail.com')
# archer1.attack()
# wizard1.sign_in()


# print(isinstance(wizard1, User))
# print(isinstance(wizard1, Wizard))


# def player_attack(char):
#     char.attack()


# player_attack(wizard1)
# player_attack(archer1)

# for char in [archer1, wizard1]:
#     char.attack()

# print(wizard1.email)

#Dunder method
# print(dir(wizard1))

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def __str__(self):
        return f'{self.color}'
    

action_figure = Toy('Green', 20)
# print(action_figure.__str__())
# print(str(action_figure))


# class HybirdBorg(Archer, Wizard):
#     def __init__(self, name, power, arrow):
#         Archer.__init__(name, arrow)
#         Wizard.__init__(name, power)

