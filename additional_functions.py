import random
def is_int(choice):
    """ Проверка на то, что s - целое число"""
    try:
        if type(choice) is int:
            return True
        if choice is None:
            return False
        if not choice.isdecimal():
            return False
        int(choice)
        return True
    except (Exception, ValueError, TypeError):
        return False

def self_input_text():
    # Функция, которая позволяет пользователю самостоятельно ввести текст
    print("Введите текст (для завершения ввода введите пустую строку):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    # Объединяем все строки в один текст
    return " ".join(lines)

def random_input_text(min_length=10, max_length=1000):
    # Генерация случайного текста на русском языке
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' + ' ' * 7
    length = random.randint(min_length, max_length)  # Генерация случайной длины
    return ''.join(random.choice(letters) for _ in range(length))