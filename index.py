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
    friends = user.get('friends', [])
#        friends = user['friends']
    for friend in friends:
        if 'cars' in friend and friend['sex'].upper() == 'F':
            girls_drivers.append(friend['name'])

# Point 3: Лучшая профессия.
        if friend['job']['salary'] > best_salary:
            best_salary = friend['job']['salary']
            best_occupation = friend['job'].copy()

# Point 4: Самый влиятельный пользователь.
    #Обнуление суммы зарплат друзей предыдущего юзера
    sum_of_salaries = 0
    friends = user.get('friends', [])
    for friend in friends:
        sum_of_salaries += friend['job']['salary']
    if sum_of_salaries > vip_sum_of_salaries:
        vip_sum_of_salaries = sum_of_salaries
        vip_user = user['name']

# Point 5: Путешественники.
    friends = user.get('friends', [])
    for friend in friends:
        cars = friend.get('cars', None)
        if cars:
            count_friends_with_cars += 1
            count_flights_by_friends_with_cars += len(friend.get('flights', []))
        try:
            # avg_flights может быть 0
            avg_flights = round(count_flights_by_friends_with_cars / count_friends_with_cars, 5)
        except ZeroDivisionError:
            avg_flights = 0

# Point 6: Чистка списка
i = 0
while i < len(users):
    # Флаг на необходимость удаления
    to_delete = False
    friends = users[i].get('friends', [])
    for friend in friends:
        flights = friend.get('flights', [])
        for flight in flights:
            if flight['country'] in countries:
                # Если страна полета в списке стран, то выход из всех циклов
                to_delete = True
                break
        if to_delete:
            break
    
    if to_delete:
        del users[i]
    else:
        i += 1
