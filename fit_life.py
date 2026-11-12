# Проект FitLife - MVP версия 1.0

# Определяем константы
WATER_PER_KG = 30
ML_PER_LITER = 1000
MIN_AGE = 0
MIN_WEIGHT = 0
MIN_HEIGHT = 0


# Создаем функцию для UI (статичная строчка из знака "равно")
def ui_string():
    """Выводим разделительную строчку для UI."""
    print(f'\n{"=" * 50}\n')


# Подобие небольшой вступительной UI шапки
ui_string()
print('Приветствуем в цифровом фитнес-трекере FitLife!')
ui_string()


# Знакомство с юзером
user_name = input('Давайте познакомимся! Как Вас зовут? ').strip()


# Избавляемся от ошибок ввода со стороны юзера
while True:
    try:
        user_age = int(input('Сколько Вам лет? '))
        if user_age <= MIN_AGE:
            print(f'Возраст должен быть больше {MIN_AGE}!')
            continue
        break
    except ValueError:
        print('Ошибка! Введите, пожалуйста, целое число. ')


print()


# Сбор данных (вес)
while True:
    try:
        user_weight = float(input(
            'Введите, пожалуйста, свой вес в кг. (например, 85): '
        ))
        if user_weight <= MIN_WEIGHT:
            print(f'Вес должен быть больше {MIN_WEIGHT}!')
            continue
        break
    except ValueError:
        print('Ошибка! Нужно ввести число.')


# Сбор данных (рост)
while True:
    try:
        user_height = float(input(
            'Введите, пожалуйста, рост в метрах (например, 1.90): '
        ))
        if user_height <= MIN_HEIGHT:
            print(f'Рост должен быть больше {MIN_HEIGHT}!')
            continue
        break
    except ValueError:
        print('Ошибка! Нужно ввести число, разделив точкой.')


# Расчеты
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = round(user_weight / user_height ** 2, ndigits=1)


# Подсчет воды: вес * 30 мл + перевод в литры
water_needed = round(user_weight * WATER_PER_KG / ML_PER_LITER, ndigits=2)


# Вывод результата и прощание с юзером
ui_string()
print(f'Привет, {user_name}!')
print(f'Индекс массы тела - {bmi}, норма воды в день - {water_needed} л.')
ui_string()
print('Расчет окончен. Будьте здоровы!')
ui_string()
