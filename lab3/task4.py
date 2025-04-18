from typing import List
from datetime import datetime


class BankAccount:
    """Класс BankAccount.

    Класс используется для симуляции банковского счёта.

    Attributes
    ----------
    __balance : int, private
        текущий баланс
    __transactions : List[str], private
        лог транзакций

    Methods
    -------
    @property
    balance() -> int
        Метод с декоратором @property,
        позволяет получить значение атрибута __balance
    deposit(amount) -> str
        Кладёт на счёт сумму, равную amount
        Если amount не указан или меньше либо равен 0, возвращает соответствующее сообщение
    withdraw(amount) -> str
        Снимает с счёта сумму, равную amount
        Если amount не указан или меньше либо равен 0, возвращает соответствующее сообщение
        Если денег на счёте меньше, чем amount, возвращает соответствующее сообщение
    show_log() -> str
        Возвращает записи из transactions, каждая запись располагается в отдельной строке
    """

    def __init__(self, balance : int = 0, transactions : List[str] = []):
        self.__balance = balance
        self.__transactions = transactions

    @property
    def balance(self):
        """Верни текущий баланс."""

        return self.__balance

    def deposit(self, amount : int = 0) -> str:
        """Положи на счёт сумму, равную amount.

        Parameters
        ----------
        amount : int
            сумма, которую нужно положить на счёт

        Если аргумент amount не указан или меньше либо равен 0,
        метод возвращает сообщение "Сумма денег не задана или меньше либо равна 0."
        Делается запись в лог:
        "[дата и время] deposit [сумма] [баланс] error Сумма денег не задана или меньше либо равна 0."

        Если операция прошла успешно, метод возвращает сообщение "Success"
        Делается запись в лог:
        "[дата и время] deposit [сумма] [новый баланс] success"
        """

        time = str(datetime.now()).split(".")[0]
        if amount <= 0:
            self.__transactions.append(f"{time} deposit {amount} "
                                       f"{self.__balance} error "
                                       f"Сумма денег не задана или меньше либо равна 0.")
            return "Сумма денег не задана или меньше либо равна 0."
        else:
            self.__balance += amount
            self.__transactions.append(f"{time} deposit {amount} {self.__balance} success")
            return "Success"

    def withdraw(self, amount : int = 0) -> str:
        """Сними со счёта сумму, равную amount.

        Parameters
        ----------
        amount : int
            сумма, которую нужно снять со счёта

        Если аргумент amount не указан или меньше либо равен 0,
        метод возвращает сообщение "Сумма денег не задана или меньше либо равна 0."
        Делается запись в лог:
        "[дата и время] withdraw [сумма] [баланс] error Сумма денег не задана или меньше либо равна 0."

        Если на счёте недостаточно денег,
        метод возвращает сообщение "Недостаточно средств на счёте."
        Делается запись в лог:
        "[дата и время] withdraw [сумма] [баланс] error Недостаточно средств на счёте."

        Если операция прошла успешно, метод возвращает сообщение "Success"
        Делается запись в лог:
        "[дата и время] withdraw [сумма] [новый баланс] success"
        """

        time = str(datetime.now()).split(".")[0]
        if amount <= 0:
            self.__transactions.append(f"{time} withdraw {amount} "
                                       f"{self.__balance} error "
                                       f"Сумма денег не задана или меньше либо равна 0.")
            return "Сумма денег не задана или меньше либо равна 0."
        else:
            if self.__balance - amount < 0:
                self.__transactions.append(f"{time} withdraw {amount} "
                                           f"{self.__balance} error "
                                           f"Недостаточно средств на счёте.")
                return "Недостаточно средств на счёте."
            else:
                self.__balance -= amount
                self.__transactions.append(f"{time} withdraw {amount} {self.__balance} success")
                return "Success"

    def show_log(self):
        """Выведи записи из __transactions"""

        return "\n".join(self.__transactions)

if __name__ == "__main__":
    print("Примеры использования:")
    print("acc = BankAccount() "
          "-> создаёт объект acc типа BankAccount с атрибутами по умолчанию")
    print("acc.deposit(1000) -> кладёт на счёт acc 1000")
    print("acc.withdraw(2000) -> снимает со счёта acc 2000")
    print("acc.show_log() -> показывает список транзакций счёта acc")
    print()


acc = BankAccount()
acc.deposit(1000)
acc.deposit(2000)
acc.deposit(-100)
acc.withdraw(1500)
acc.withdraw(2000)
acc.withdraw(0)
acc.withdraw()
acc.deposit()
print(acc.show_log())

