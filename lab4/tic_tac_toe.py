from collections import Counter
from itertools import chain



class TicTacToeController:

    def __init__(self):
        self.__game = TicTacToe()

    def controller(self):
        while True:
            command = input("Нажмите Enter, чтобы начать игру или введите EXIT, чтобы выйти: ")
            if command == "EXIT":
                break
            else:
                print("Добро пожаловать в игру Крестики-нолики!")
                print()

                while not self.__game.game_over:
                    flag = True
                    while flag:
                        try:
                            flag = False
                            self.__game.print_field()
                            new_move = int(input(f"Ход игрока под номером {self.__game.next_player}! Введите номер клетки, которую вы хотите закрыть. "))
                            self.__game.move(new_move)
                        except:
                            print("Что-то пошло не так.")
                            flag = True





class TicTacToe:

    def __init__(self):
        self.__field = [[i, i+1, i+2] for i in range(1,8,3)]
        self.__game_over = False
        self.__next_player = 1

    @property
    def next_player(self):
        return self.__next_player

    @property
    def game_over(self):
        return self.__game_over

    def move(self, coord : int):
        try:
            if Counter(chain(*self.__field))[coord] != 0:
                if coord % 3 == 0:
                    first_coord = (coord // 3) - 1
                    second_coord = 2
                else:
                    first_coord = coord // 3
                    second_coord = (coord % 3) - 1

                self.__field[first_coord][second_coord] = "X" if self.__next_player == 1 else "O"
                self.__next_player = 2 if self.__next_player == 1 else 1
                self.print_field()
                is_game_over = self.is_game_over()
                if is_game_over == 0:
                    print("Ход следующего игрока!")
                    print()
                else:
                    if is_game_over == 1:
                        print("Первый игрок выиграл!")
                    elif is_game_over == 2:
                        print("Второй игрок выиграл!")
                    elif is_game_over == 3:
                        print("Ничья!")
                    self.__game_over = True
            else:
                if 1 <= coord <= 9:
                    print("Эта клетка уже занята!")
                else:
                    print("По-моему, клетки с таким номером нет на поле!")
        except:
            print("Что-то пошло не так.")

    def is_game_over(self):
        a = [[self.__field[i][j] for i in range(0,3)] for j in range(0,3)]
        b = [self.__field[i][i] for i in range(0,3)]
        c = [self.__field[i][2-i] for i in range(0,3)]


        if (['X','X','X'] in self.__field) or (['X','X','X'] in a) or (['X','X','X'] == b) or (['X','X','X'] == c):
            return 1
        elif (['O','O','O'] in self.__field) or (['O','O','O'] in a) or (['O','O','O'] == b) or (['O','O','O'] == c):
            return 2
        else:
            if Counter(chain(*self.__field))["X"] + Counter(chain(*self.__field))["O"] == 9:
                return 3
            return 0



    def new_game(self):
        self.__init__()

    def print_field(self):
        #print("———" * 4)
        for i in self.__field:
            print(f"| {i[0]} | {i[1]} | {i[2]} |")
        #print("———" * 4)
        print()


# controller = TicTacToeController()
# controller.controller()

