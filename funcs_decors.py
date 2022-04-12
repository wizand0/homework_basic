
def fizz_buzz(a, b):
    tmp = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                tmp += i
    return tmp


def plural_form(number, form1, form2, form3):
    n = abs(number)
    n %= 100
    if n >= 5 & n <= 20:
        return form3
    n %= 10
    if n == 1:
        return form1
    if n >= 2 & n <= 4:
        return form2

    else:
        return form3
