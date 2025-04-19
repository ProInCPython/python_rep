import random

class BlackjackController:

    def __init__(self):
        self.__game = Blackjack()
        self.__balance = self.__game.balance


    def controller(self):
        print(f"Ваш текущий баланс: {self.__balance}")
        bet = 0
        flag = True
        while flag:
            try:
                flag = False
                bet = int(input("Введите вашу ставку: "))
            except:
                flag = True
        if bet <= 0:
            print("Ставка должна быть больше нуля!")
        elif self.__balance - bet < 0:
            print("Не хватает денег для игры!")
            if input("Хотите добавить на счёт 10 долларов(YES/NO)?") == "YES":
                self.__balance += 10
            self.controller()

        self.__game.new_game(bet)

        while not self.__game.game_over:
            c = input("hit or stand? ")
            if c == "hit":
                print(self.__game.hit())
            elif c == "stand":
                print(self.__game.stand())
            else:
                print("Что-то пошло не так...")


class Blackjack:
    def __init__(self):
        self.__player_hand = [random.randint(2,11), random.randint(2,11)]
        self.__dealer_hand = [random.randint(2,11), random.randint(2,11)]
        self.__bet = 0
        self.__game_over = False
        f = open("balance.txt", "r")
        self.__balance = int(f.readline())
        f.close()

    def new_game(self, bet : int):
        self.__bet = bet
        print("Your cards: " + " ".join(list(map(str,self.player_hand))))
        print("Dealer's upcard: " + str(self.player_hand[0]))


    def hit(self) -> str:
        self.player_hand.append(random.randint(2,11))
        if sum(self.player_hand) > 21:
            self.end_game("loss")
            return f"Bust! You lost {self.__bet} dollars."
        elif sum(self.player_hand) == 21:
            self.end_game("win")
            return f"Win! Your final cards: " + " ".join(list(map(str,self.player_hand))) + f" You won {self.__bet * 2} dollars!"
        return "Your cards: " + " ".join(list(map(str, self.player_hand)))

    def stand(self):
        while sum(self.dealer_hand) < 17:
            self.dealer_hand.append(random.randint(2,11))

        if sum(self.dealer_hand) > 21:
            self.end_game("win")
            return f"Dealer bust! You won {self.__bet} dollars!"
        elif sum(self.dealer_hand) == 21:
            if sum(self.player_hand) == 21:
                self.end_game("even")
                return f"Even! You returned your {self.__bet} dollars bet."
        else:
            if sum(self.dealer_hand) < sum(self.player_hand):
                self.end_game("win")
                return f"Win! Your final cards: " + " ".join(list(map(str, self.player_hand))) + f" You won {self.__bet * 2} dollars!"
            elif sum(self.dealer_hand) > sum(self.player_hand):
                self.end_game("loss")
                return f"Dealer won! His final cards: " + " ".join(list(map(str, self.dealer_hand))) + f" You lost {self.__bet} dollars."
            self.end_game("even")
            return f"Even! You returned your {self.__bet} dollars bet."

    def end_game(self, status : str):
        self.__game_over = True
        if status == "win":
            self.balance += self.__bet * 2
        elif status == "loss":
            self.balance -= self.__bet
        f = open("balance.txt", "w")
        f.write(str(self.balance))
        f.close()

    @property
    def player_hand(self):
        return self.__player_hand

    @property
    def dealer_hand(self):
        return self.__player_hand

    @property
    def game_over(self):
        return self.__game_over

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value


while True:

    command = input("Нажмите Enter, чтобы начать игру или введите EXIT, чтобы выйти: ")
    if command == "EXIT":
        break
    else:
        controller = BlackjackController()
        controller.controller()