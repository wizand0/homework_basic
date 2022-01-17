from dataset import users, countries

from pprint import pprint

#pprint(users)
#print('-------------------------------')
#pprint(countries)

#print(type(users['password']))
users_wrong_password = [] # Создание пустого словаря

try:
    for user in users:
        if user['password'].isdigit():
            dict1 = {user['name']: user['mail']}
            users_wrong_password.append(dict1)
except KeyError:
    print('Нет ключа: name')
