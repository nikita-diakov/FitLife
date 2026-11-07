# Проект FitLife - MVP версия 1.0

# Создаем пару функцию для UI (статичная строчка из знака "равно")
def ui_string():
    print()
    print("=" * 50)
    print()


# Определяем константы
WATER_PER_KG = 30

# Подобие небольшой вступительной UI шапки
ui_string()
print('Приветствуем в цифровом фитнес-трекере FitLife!')
ui_string()

# Знакомство с юзером
user_name = input('Давайте познакомимся! Как Вас зовут? ')
user_age = int(input('Сколько Вам лет? '))

print()

# Сбор данных
user_weight = float(input('Введите, пожалуйста, свой вес в кг. (например, 85): '))
user_height = float(input('Введите, пожалуйста, рост в метрах (например, 1.90): '))

# Расчеты
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / user_height ** 2, ndigits=1)

# Подсчет воды: вес * 30 мл + перевод в литры
water_needed = round(user_weight * WATER_PER_KG / 1000, ndigits=2)

# Вывод красивого результата (шапка - текст - шапка - прощание с юзером - шапка)
ui_string()
print(f'Привет, {user_name}!')
print(f'Индекс массы тела - {bmi}, норма воды в день - {water_needed} л.')
ui_string()
print("Расчет окончен. Будьте здоровы!")
ui_string()