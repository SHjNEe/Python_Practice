
# while True:
#     try:
#         age = int(input('Please enter your age : '))
#         10/age
#         print(age)
       
#     # except ValueError as error:
#     #     print(error)
#     # except ZeroDivisionError as error:
#     #     print(error)
#     except (ZeroDivisionError, TypeError) as error:
#         print(error)
#     else:
#         print('Tks')
#         break


def age_division():
    try:
        age = int(input('Please enter your age: '))
        result = 10 / age
        if age == 1:
            raise ValueError("Age cannot be zero.")
    except (ZeroDivisionError, ValueError, TypeError) as error:
        print('Error:', error)
    else:
        print('Result:', result)
    finally:
        print('End')

age_division()
