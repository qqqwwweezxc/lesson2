num1 = int(input('Введите первое число: '))
num2 = int(input('Введие второе число: '))
operator = input('Введите операцию: ')
allow_operations = ['+', '-', '/', '*', '**']

if operator not in allow_operations:
    print('Неверная операция')
elif operator == '+':
    print(f'Сумма чисел {num1} и {num2} = {num1 + num2}')
elif operator == '-':
    print(f'Разость чисел {num1} и {num2} = {num1 - num2}')
elif operator == '*':
    print(f'Произведение чисел {num1} и {num2} = {num1 * num2}')
elif operator == '/':
    print(f'Частное от {num1} к {num2} = {num1 / num2}')
elif operator == '**':
    print(f'{num1} в степени {num2} = {num1 ** num2}')
