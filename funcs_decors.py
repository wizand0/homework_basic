def fizz_buzz(a, b):
    tmp = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                tmp += i
    return tmp


def plural_form(number, form1, form2, form3):
    if number % 10 == 1 and number != 11:
        #    if number == 1:
        return f'{number} {form1}'
    if 1 < number < 5:
        return f'{number} {form2}'
    if 4 < number:
        return f'{number} {form3}'

