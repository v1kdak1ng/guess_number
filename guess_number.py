import random


def choose_difficulty():

    while True:
        try:
            level = int(input("Введи число от 1 до 3"))
            if level == 1:
                print("Не всегда нужно идти на риски")
                return 1, 10
            elif level == 2:
                print("Это уроыень уже не для новичков")
                return 1, 100
            elif level == 3:
                print("Это станет для тебя настоящим кошмаром")
                return 1, 1000
            else:
                print("Некорркутный ввод, попробуй еще раз)")
        except ValueError:
            print("Пожалуйста, вводи только числа")


def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!!!")
    name = input("Как тебя зовут?")
    print(
        f"Очень приятно, {name}, если ты не против, то не мог бы ты выбрать уровень сложности для игры (от него будет зависть диапазон чисел среди которых будет скрыто то, которое ты ищешь)"
    )
    start, end = choose_difficulty()
    secret_number = random.randint(start, end)
    attempts = 0
    while True:
        try:
            guess = int(input(f"Введи число от {start} до {end} "))
            attempts += 1
            if guess > end or guess < start:
                print("Введенное число вышло из заданного диапазона")
            elif guess < secret_number:
                print("Введенное число меньше загадонного")
            elif guess > secret_number:
                print("Введенное число больше загадонного")

            else:
                print("Поздравляю, ты угадал загаданное число!")
                print(f"Количество ваших попыток: {attempts}")
        except ValueError:
            print("Пожалуйста, вводи только числа")


if __name__ == "__main__":
    guess_number()
