from lab4.blackjack import BlackjackController
from lab4.guess_the_number import GameController
from lab4.tic_tac_toe import TicTacToeController

print("Добро пожаловать! Здесь вы можете сыграть в три игры: Угадай число, блэкджек и крестики-нолики!")

flag = True
while flag:
    try:
        flag = False
        choice = input("Введите 1, чтобы сыграть в Угадай число.\nВведите 2, чтобы сыграть в блэкджек.\nВведите 3, чтобы сыграть в крестики-нолики.\nВведите EXIT, чтобы выйти. ")
        if choice == "EXIT":
            break
        else:
            if int(choice) == 1:
                controller = GameController()
            elif int(choice) == 2:
                controller = BlackjackController()
            elif int(choice) == 3:
                controller = TicTacToeController()

            controller.controller()
            flag = True

    except:
        print("Что-то пошло не так.")
        flag = True