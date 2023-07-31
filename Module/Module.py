# import Utility
    
# # result = Utility.multiply(2,2)

# from Utility import multiply

# result = multiply(2,2)
# print(result)

# # print(__name__)

# new_list = [1,2,3,4,5,6,7]

# new_list2 = new_list[::-1]


# print(new_list2)


from random import random,randint,choice,shuffle

# print(randint(1,10))
# print(random())
# print(choice([1,2,3,4,5,6,7,8,9,0]))
# mylist = [1,2,3,4,5,6]
# shuffle(mylist)
# print(mylist)

# from sys import argv

# first = argv[0]
# print(f'{first}')



################################
# GUESS NUMBER GAME
# def guess_number():
#     try:
#         enterdNumber = int(input('Enter you right number 1 ~ 10 : '))
#         result = randint(1,10)
#         if enterdNumber == result:
#             print('Corrected')
#         else:
#             raise ValueError("Is not correct, please try again")
#     except (ZeroDivisionError, ValueError, TypeError) as error:
#         print('Error:', error)
#         guess_number()

# guess_number()



while True:
    try:
        result = randint(1,10)
        guess_number = int(input('Enter you right number 1 ~ 10 : '))
        if guess_number < 1 or guess_number > 10:
            raise ValueError("Is not correct, please try again with number in 1~10")
        if guess_number == result:
            print('Corrected')
            break
        else:
            raise ValueError("Is not correct, please try again")
    except ValueError as error:
        print('Error:', error)
        continue
