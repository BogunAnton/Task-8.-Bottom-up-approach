# 4.Входные данные: текст. Результат работы алгоритма: массив анаграмм во входном тексте.
from main_function import f1, f2, f3
from additional_functions import is_int
def menu():
    anagramms = []
    while True:
        print("Выберите пункт меню:\n"
              "1. Ввод исходного текста, вручную или сгенерированного случайным образом\n"
              "2. Выполнение алгоритма по поиску анограмм в исходном тексте\n"
              "3. Вывод результата алгоритма\n"
              "0. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)
        if choice == 1:
            f1()
        elif choice == 2:
            f2(anagramms)
        elif choice == 3:
            f3(anagramms)
        elif choice == 0:
            break
        else:
            print('error')

if __name__ == "__menu__":
    menu()