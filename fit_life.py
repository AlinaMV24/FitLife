WATER_REC = 30
WATER_PER_KG = 1000
print('Привет, Я бот FitLife — помогу следить за здоровьем и прогрессом.')
user_name = input('Напишите, пожалуйста, вашу фамилию и имя.')
user_age = int(input('Укажите полное количество лет. '))
print(f"Привет, {user_name.title()}!")
user_height = float(input('Пожалуйста, введите свой рост '
                          '(в м , через точку например: 1.62 ) '))
user_weight = float(input('Укажите, пожалуйста, вес (в кг, через точку)'))
# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)
# расчёт нормы воды
water_ml = user_weight * WATER_REC
water_l = water_ml / WATER_PER_KG
print('------------------------------------------------------------')
print(f"Отчет для пользователя:{user_name.title()} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print('============================================================')
print('Расчет окончен. Будьте здоровы!')
