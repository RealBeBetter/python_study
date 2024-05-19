import functools


def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):  # 如果用户处于登录状态
            return func(*args, **kwargs)  # 执行函数 post_comment()
        else:
            raise Exception('Authentication failed')

    return wrapper


@authenticate
def post_comment(request, *args, **kwargs):
    ...
