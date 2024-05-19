def func(message):
    print('Got a message: {}'.format(message))


send_message = func
send_message('hello world')  # Got a message: hello world


def root_call(function_name, message):
    print(function_name(message))


root_call(send_message, 'root call: hello world')  # Got a message: root call: hello world


def func(message):
    def get_message(message):
        print('Got a message: {}'.format(message))

    return get_message(message)


func('hello world')  # Got a message: hello world


def func_closure():
    def get_message(message):
        print('Got a message: {}'.format(message))

    return get_message


send_message = func_closure()
send_message('hello world')  # Got a message: hello world
