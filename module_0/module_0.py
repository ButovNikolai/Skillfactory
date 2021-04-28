import numpy as np


def game_core_v3(number):
    '''Указываем произвольное random число -> проводим бинарный поиск '''
    count = 0
    predict = 50 # Каждый раз начинаем с середины диапазона
    min_number = 0
    max_number = 101 # Чтобы угадывать 0 и 100 берем диапазон 0-101
    while number != predict:
        count+=1
        if number > predict:
            min_number = predict # Установим новую нижнюю границу для поиска
            predict = (max_number - predict)//2 + predict # Предположим середину нового диапазона
        elif number < predict:
            max_number = predict # Установим новую верхнюю границу для поиска
            predict = (predict -  min_number)//2 + min_number # Предположим середину нового диапазона
    return(count) # Выход из цикла, при условии угадывания


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # Фиксируем random seed для воспроизведения эксперемента
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3) # Запуск программы