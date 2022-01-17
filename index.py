from dataset import users, countries

from pprint import pprint

#pprint(users)
#print('-------------------------------')
#pprint(countries)

#print(type(users['password']))
users_wrong_password = [] # Создание пустого словаря

for user in users:
    if user['password'].isdigit():
        dict1 = {user['name']: user['mail']}
        users_wrong_password.append(dict1)


    else:
        print('Good password')

print(users_wrong_password)
#    print(user['password'])