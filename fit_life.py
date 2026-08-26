import io
import sys

# Принудительно устанавливаем кодировку вывода в UTF-8
# Это решает ошибку UnicodeDecodeError в тестах на Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

WATER_REC = 30
WATER_PER_KG = 1000

print('Привет, Я бот FitLife — помогу следить за здоровьем и прогрессом.')
user_name = input('Напишите, пожалуйста, вашу фамилию и имя.')
user_age = int(input('Укажите полное количество лет. '))
print(f"Привет, {user_name.title()}!")

# Порядок ввода строго как в тесте: имя, возраст, ВЕС, РОСТ
user_weight = float(input('Укажите, пожалуйста, вес (в кг, через точку)'))
user_height = float(
    input('Пожалуйста, введите свой рост (в м, через точку например: 1.62) '))

# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# расчёт нормы воды
water_ml = user_weight * WATER_REC
water_l = water_ml / WATER_PER_KG
print(f"Отчет для пользователя:{user_name.title()} ({user_age} г.)")
print("Твой Индекс Массы Тела:", bmi)
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print('Расчет окончен. Будьте здоровы!')
