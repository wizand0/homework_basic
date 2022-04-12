def fizz_buzz(a, b):
    tmp = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                tmp += i
    return tmp


def plural_form(number, form1, form2, form3):
    n = abs(number)
    if n % 10 == 1 and n % 100 != 11:
        return form1
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        return form2
    else:
        return form3


def html(*args, **kwargs):
    def decorator(decorated_function):
        def wrapper(argument):

            result_url = decorated_function(argument)
            position_arg = ''
            for i in args:
                position_arg += f'{i}'

            temp_str = ''

            if kwargs:
                for k, v in kwargs.items():
                    temp_str += f' {k}="{v}"'

            result_url = f'<{position_arg}{temp_str}>{result_url}</{position_arg}>'
            return result_url

        return wrapper

    return decorator
