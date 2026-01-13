# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме 
# всі символи між ними включно. Жодних перевірок на помилку робити не треба, мінімальне значення 
# завжди менше або дорівнює максимальному.Підказка: Використовуйте модуль string , у якому є 
# string.ascii_letters, з усім набором потрібних букв

# v1

# import string

# ALL_LETTERS = string.ascii_letters
# SEPARATOR = '-'

# user_input = input('Введите две буквы через дефис (a-b): ').strip()

# if len(user_input) == 3:
#     first_digit = user_input[0]
#     second_digit = user_input[2]
#     separator = user_input[1]

#     if first_digit.isalpha() and second_digit.isalpha() and separator == SEPARATOR:
#         start_index = ALL_LETTERS.index(first_digit)
#         end_index = ALL_LETTERS.index(second_digit)

#         if start_index > end_index:
#             start_index, end_index = end_index, start_index
        
#         result = ALL_LETTERS[start_index:end_index + 1]

# print(result)

# v2
# SEPARATOR = '-'

# user_input = input('Введите две буквы через дефис (a-b): ').strip()

# if len(user_input) == 3:
#     first_digit = user_input[0]
#     second_digit = user_input[2]
#     separator = user_input[1]
#     if first_digit.isalpha() and second_digit.isalpha() and separator == SEPARATOR:
#         for letter in range(ord(first_digit), ord(second_digit) + 1):
#             print(chr(letter), end = '')

