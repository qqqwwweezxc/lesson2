# # Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# # Змінна не може:
# # починатися з цифри
# # містити великі літери,
# # пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# # бути жодним із зареєстрованих слів.
# # При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# # Список зареєстрованих слів можна взяти із keyword.kwlist.
# # У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# # Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))

# import string
# import keyword

# variable = input('Введите имя переменной: ')
# is_correct = True

# if variable and variable[0].isdigit():
#     is_correct = False

# for i in variable:
#     if i.isupper() or i == ' ':
#         is_correct = False
#     if i in string.punctuation and i != '_':
#         is_correct = False

# if variable in keyword.kwlist:
#     is_correct = False

# if variable.count('_') > 1:
#     is_correct = False

# print(is_correct)
