from threading import Lock, Thread
from time import sleep
from random import randint
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.lock.acquire()
    def deposit(self):
        for i in range(100):
            money = randint(50, 500)
            self.balance += money
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {money}. Баланс: {self.balance}.')
            sleep(0.001)
    def take(self):
        for j in range(100):
            money = randint(50, 500)
            print(f'Запрос на {money}.')
            if money <= self.balance:
                self.balance -= money
                print(f'Снятие: {money}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()
            sleep(0.001)
bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')