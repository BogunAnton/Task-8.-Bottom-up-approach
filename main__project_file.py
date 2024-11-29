# 4.Входные данные: текст. Результат работы алгоритма: массив анаграмм во входном тексте.
from main_function import f1, f2, f3
from additional_functions import is_int
def menu(): # Изменения, чтобы закоммитить
    anagramms = []
    text_entered = False  # Флаг для отслеживания ввода текста
    algorithm_executed = False  # Флаг для отслеживания выполнения алгоритма
    while True:
        print("Выберите пункт меню:\n"
              "1. Ввод исходного текста, вручную или сгенерированного случайным образом\n"
              "2. Выполнение алгоритма по поиску анаграмм в исходном тексте\n"
              "3. Вывод результата алгоритма\n"
              "0. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)
        if choice == 1:
            text_entered = f1()
        elif choice == 2:
            if text_entered:
                anagramms = f2()
                algorithm_executed = True
            else:
                print("Сначала введите текст (пункт 1).")
        elif choice == 3:
            if text_entered and algorithm_executed:
                f3(anagramms)
            else:
                print("Сначала выполните пункты 1 и 2.")
        elif choice == 0:
            break
        else:
            print('error')

if __name__ == "__main__":
    menu()