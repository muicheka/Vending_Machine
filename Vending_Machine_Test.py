import unittest
from Vending_Machine import *


class VendingMachineTest(unittest.TestCase):

    def setUp(self):
        self.machine = VendingMachine()

    def test_machine_has_zero_balance(self):
        self.assertTrue(self.machine.get_current_value() == 0)

    def test_insert_single_coin(self):
        self.machine.insert_coin(Coin.DOLLAR)
        self.assertTrue(self.machine.get_current_value() == 100)

    def test_insert_multiple_coin(self):
        self.machine.insert_coin(Coin.DOLLAR)
        self.machine.insert_coin(Coin.QUARTER)
        self.assertTrue(self.machine.get_current_value() == 125)

    def test_coin_return(self):
        self.machine.insert_coin(Coin.DOLLAR)
        self.machine.insert_coin(Coin.QUARTER)
        returned_coins = self.machine.return_coins()
        self.assertTrue(len(returned_coins) == 2)
        self.assertTrue(returned_coins.count(Coin.QUARTER) == 1)
        self.assertTrue(returned_coins.count(Coin.DOLLAR) == 1)

    def test_check_balance_after_coin_return(self):
        self.machine.insert_coin(Coin.DOLLAR)
        self.machine.insert_coin(Coin.QUARTER)
        returned_coins = self.machine.return_coins()
        self.assertTrue(self.machine.get_current_value() == 0)

    # def test_sufficient_money(self):
    #     self.machine.insert_coin(Coin.DOLLAR)
    #     self.machine.insert_coin(Coin.QUARTER)
    #     self.assertTrue(self.machine.vend_item(Item.B))
    #     self.assertTrue(self.machine.get_current_value() == 0)

    # def test_insufficient_money(self):
    #     self.machine.insert_coin(Coin.DOLLAR)
    #     self.assertFalse(self.machine.vend_item(Item.B))

    def test_excessive_money(self):
        self.machine.insert_coin(Coin.DOLLAR)
        self.machine.insert_coin(Coin.DOLLAR)
        self.assertTrue(self.machine.vend_item(Item.C))
        returned_coins = self.machine.return_change(Item.C)
        self.assertTrue(len(returned_coins) == 2)
        self.assertTrue(returned_coins.count(Coin.QUARTER) == 2)
