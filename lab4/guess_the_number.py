from datetime import datetime, timedelta
import random

class GameController:

    def __init__(self):
        self.__game = Game()

    def controller(self):
        while True:
            command = input("Нажмите Enter, чтобы начать игру или введите EXIT, чтобы выйти: ")
            if command == "EXIT":
                break
            else:
                start = 1
                end = 100
                flag = True
                while flag:
                    try:
                        flag = False
                        start = int(input("Введите нижнее число: "))
                    except:
                        flag = True
                flag = True
                while flag:
                    try:
                        flag = False
                        end = int(input("Введите верхнее число: "))
                    except:
                        flag = True

                self.__game.new_game(start, end)

                while not self.__game.is_game_over:
                    flag = True
                    while flag:
                        try:
                            flag = False
                            guess = int(input("Попробуйте угадать число: "))
                        except:
                            flag = True

                    print(self.__game.guess(guess))



class Game:

    def __init__(self):
        self.__number = 0
        self.__attempts = 0
        self.__logger = None
        self.__game_start_time = None
        self.__is_game_over = False

    def guess(self, number : int) -> str:
        if number > self.__number:
            self.__attempts -= 1
            if self.__attempts > 0:
                self.logger.bigger(number, self.attempts)
                return f"Загаданное число меньше вашего! У вас осталось {self.__attempts} " + self.attempts_generator()
            self.logger.game_over(number, datetime.now() - self.__game_start_time)
            self.__is_game_over = True
            return f"Вы проиграли. Число, которое было загадано: {self.__number}. Времени потрачено: {datetime.now() - self.__game_start_time}."
        elif number < self.__number:
            self.__attempts -= 1
            if self.__attempts > 0:
                self.logger.smaller(number, self.attempts)
                return f"Загаданное число больше вашего! У вас осталось {self.__attempts} " + self.attempts_generator()
            self.logger.game_over(number, datetime.now() - self.__game_start_time)
            self.__is_game_over = True
            return f"Вы проиграли. Число, которое было загадано: {self.__number}. Времени потрачено: {datetime.now() - self.__game_start_time}."
        else:
            self.__attempts -= 1
            self.logger.correct(number, self.attempts, datetime.now() - self.__game_start_time)
            self.__is_game_over = True
            return f"Вы угадали число за {5 - self.__attempts} " + self.attempts_generator() + f". Поздравляем! Времени потрачено: {datetime.now() - self.__game_start_time}."

    def new_game(self, starting_number : int, ending_number : int):
        self.__number = random.randint(starting_number, ending_number)
        self.__attempts = 5
        self.__logger = Logger()
        self.__game_start_time = datetime.now()
        self.__is_game_over = False

    def attempts_generator(self) -> str:
        if 2 <= self.__attempts <= 4: return "попытки"
        elif self.__attempts == 1: return "попытка"
        else: return "попыток"

    @property
    def logger(self):
        return self.__logger

    @property
    def attempts(self):
        return self.__attempts

    @property
    def is_game_over(self):
        return self.__is_game_over



class Logger:

    def __init__(self):
        self.__log = open("log.txt", "a")
        self.__log.write(str(datetime.now().year) + "/" + str(datetime.now().month) + "/" + str(datetime.now().day) + " " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second) + "\n")

    def bigger(self, guess : int, attempts : int):
        self.__log.write(f"User guess was: {guess}. It was bigger than the real number. Attempts left: {attempts}.\n")

    def smaller(self, guess : int, attempts : int):
        self.__log.write(f"User guess was: {guess}. It was smaller than the real number. Attempts left: {attempts}.\n")

    def correct(self, guess : int, attempts : int, time : timedelta):
        self.__log.write(f"User guess was: {guess}. He/she guessed the number in {5 - attempts} attempts. Total game time: {time}.\n")

    def game_over(self, guess : int, time : timedelta):
        self.__log.write(f"Game over. User last guess was: {guess}. Total game time: {time}.\n")
        self.__log.close()


# controller = GameController()
# controller.controller()

