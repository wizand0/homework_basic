from dataset import users, countries


users_wrong_password = [] # Создание пустого словаря
girls_drivers = []
best_occupation = {}
best_salary = 0
sum_of_salaries = 0
vip_sum_of_salaries = 0
vip_user = ''
avg_flights = 0.0
count_friends_with_cars = 0
count_flights_by_friends_with_cars = 0
to_delete_list = []

for user in users:
# Point 1: Определение плохих паролей.
# Проверка, что пароль состоит только из цифр
    if user['password'].isdigit():
        dict1 = {'name': user['name'], 'mail': user['mail']}
        users_wrong_password.append(dict1)

# Point 2: Определение водителей-девушек.
    if 'friends' in user:
        friends = user['friends']
        for friend in friends:
            if 'cars' in friend and friend['sex'].upper() == 'F':
                girls_drivers.append(friend['name'])

# Point 3: Лучшая профессия.
            if friend['job']['salary'] > best_salary:
                best_salary = friend['job']['salary']
                best_occupation = friend['job'].copy()

# Point 4: Самый влиятельный пользователь.
    if 'friends' in user:
        friends = user['friends']
        for friend in friends:
            sum_of_salaries += friend['job']['salary']
        if sum_of_salaries > vip_sum_of_salaries:
            vip_sum_of_salaries = sum_of_salaries
            vip_user = user['name']

# Point 5: Путешественники.
            if 'flights' in friend and 'cars' in friend:
                count_friends_with_cars += 1
                count_flights_by_friends_with_cars += len(friend['flights'])
            try:
                avg_flights = round(count_flights_by_friends_with_cars/count_friends_with_cars, 5)
            except ZeroDivisionError:
                avg_flights = 0

# Point 6: Чистка списка
            
            if 'flights' in friend:
                for country in friend['flights']:
                    if country['country'] in countries:
                        to_delete_list.append(user['name'])

to_delete_list = list(set(to_delete_list))


for user in users:
    if user['name'] in to_delete_list:
        users.remove(user)
