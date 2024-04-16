name = input('your name: ')
gender = input('you are a boy(y/n)? ')

# ###### 输入 ######
# your name: Real
# you are a boy(y/n)? y

welcome_str = 'Welcome to the matrix {prefix} {name}.'
welcome_dic = {
    'prefix': 'Mr.' if gender == 'y' else 'Mrs',
    'name': name
}

print('authorizing...')
print(welcome_str.format(**welcome_dic))

# ########## 输出 ##########
# authorizing...
# Welcome to the matrix Mr. Real.
