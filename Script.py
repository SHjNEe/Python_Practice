# my_file = open('test.txt')
# print(
# my_file.readlines(1)
# )

# my_file.close()
# with open('test.txt', mode='w') as my_file:
#     print(
#     my_file.readlines(1)
#     )

#     my_file.close()

# Open the file in append mode ('a' mode)
# file_path = 'test.txt'
# content_to_append = "This is the new content to append.\n"

# with open(file_path, 'a') as file:
#     file.write(content_to_append)

# print("Content appended successfully.")

from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('test-ja.txt',mode='w') as new_file:
              new_file.write(translation)
              

except FileNotFoundError as err:
        # print(err)
        raise err
except IOError as err:
        print(err)
