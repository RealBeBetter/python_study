# encoding: utf-8

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    print(num1 / num2)
except (ValueError, ZeroDivisionError) as err:
    print('ValueError or ZeroDivisionError: {}'.format(err))
finally:
    print('continue')

# please enter two numbers separated by comma: a,b
# Value Error: invalid literal for int() with base 10: 'a'
# continue

# please enter two numbers separated by comma: 1,0
# ValueError or ZeroDivisionError: division by zero
# continue


file_name = './test.txt'
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError as err:
    print('FileNotFoundError: {}'.format(err))
finally:
    print('finally block')
# FileNotFoundError: [Errno 2] No such file or directory: './test.txt'
# finally block
