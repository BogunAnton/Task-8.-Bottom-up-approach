from additional_functions import is_int, self_input_text, random_input_text
def f1():
    global full_text
    print("Выберите опцию 1-2:\n"
          "1. Ввести текст самостоятельно\n"
          "2. Сгенерировать случайный текст\n")
    option = input()
    if is_int(option):
        option = int(option)
    if option == 1:
        full_text = self_input_text()
        print("Вы ввели следующий текст:")
        print(full_text)
    elif option == 2:
        full_text = random_input_text()
        print("Сгенерированный случайный текст:")
        print(full_text)
    else:
        print('error')
    return True  # Возвращаем True, чтобы указать, что текст был введен

def f2(anagramms):
    """ Выполнение алгоритма по заданию """
    words = full_text.split()
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    result = [group for group in anagrams.values() if len(group) > 1]
    print("Алгоритм выполнен")
    return result

def f3(anagramms):
    """ Вывод результата """
    if len(anagramms) == 0:
        print("Анаграмм в тексте нет!!!")
    else:
        for group in anagramms:
            print("Анаграммы:", group)