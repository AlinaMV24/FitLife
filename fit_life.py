import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


WATER_REC = 30
WATER_PER_KG = 1000

print('Привет, Я бот FitLife — помогу следить за здоровьем и прогрессом.')
user_name = input('Напишите, пожалуйста, вашу фамилию и имя.')
user_age = int(input('Укажите полное количество лет. '))
formatted_name = user_name.title()
print(f"Привет, {formatted_name}!")

# Порядок ввода строго как в тесте: имя, возраст, ВЕС, РОСТ
user_weight = float(input('Укажите, пожалуйста, вес (в кг, через точку)'))
user_height = float(input('Пожалуйста, введите свой рост '
                          '(в м, через точку например: 1.62) '))

# расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

# расчёт нормы воды
water_ml = user_weight * WATER_REC
water_l = water_ml / WATER_PER_KG

print('------------------------------------------------------------')
print(f"Отчет для пользователя:{formatted_name} ({user_age} г.)")
print("Твой Индекс Массы Тела:", bmi)
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print('============================================================')
print('Расчет окончен. Будьте здоровы!')
