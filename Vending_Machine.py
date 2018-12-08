from enum import IntEnum


class Coin(IntEnum):
    DOLLAR = 100
    QUARTER = 25
    DIME = 10
    NICKEL = 5


class Item(IntEnum):
    A = 100
    B = 125
    C = 150
    D = 145


class VendingMachine:
    def __init__(self):
        self.inserted_coins = []
        self.change_coins = []

    def get_current_value(self):
        total = 0
        for coin in self.inserted_coins:
            total += coin
        return total

    def insert_coin(self, coin):
        self.inserted_coins.append(coin)

    def return_coins(self):
        temp = self.inserted_coins.copy()
        self.inserted_coins.clear()
        return temp

    def vend_item(self, item):
        total = self.get_current_value()
        if total == item:
            total -= item
            self.inserted_coins.clear()
            return True
        elif total > item:
            total -= item
            return True
        else:
            return False

    def return_change(self, item):
        change = []
        temp = self.get_current_value()
        self.inserted_coins.clear()
        temp -= item
        while temp != 0:
            if temp == 0:
                break
            elif temp % 25 == 0:
                quarters = temp / 25
                quarters = int(round(quarters))
                for coin in range(quarters):
                    temp -= Coin.QUARTER
                    change.append(Coin.QUARTER)
            elif temp % 5 == 0:
                temp -= Coin.NICKEL
                change.append(Coin.NICKEL)
        return change
