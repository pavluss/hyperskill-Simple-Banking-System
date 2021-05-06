import random
import sqlite3


class BankingSystem:

    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS card (
                       id INTEGER,
                       number TEXT,
                       pin TEXT,
                       balance INTEGER DEFAULT 0
                       )""")
        self.conn.commit()

    def firs_menu(self):
        act = int(input("""1. Create an account
2. Log into account
0. Exit"""))
        print()
        if act == 1:
            self.create_account()
        elif act == 2:
            self.login_account()
        else:
            self.exit()

    def create_account(self):
        digit = random.randint(0000000000, 999999999)
        card = (400000000000000 + digit)
        card = self.luhn_algorithm(card)
        pin = random.randint(0000, 9999)
        pin = str(pin).zfill(4)
        if self.check_exist(card) is None:
            self.cur.execute("""SELECT id FROM card WHERE id=(SELECT max(id) FROM card)""")
            temp = self.cur.fetchone()
            if temp is None:
                id = 0
            else:
                id = temp[0]
            self.add_value(id+1, card, str(pin))
            print(f"""Your card has been created
Your card number:
{card}
Your card PIN:
{pin}""")
            print()
            self.firs_menu()
        else:
            self.create_account()

    def login_account(self):
        card = int(input("Enter your card number:"))
        pin = input("Enter your PIN:")
        print()
        self.cur.execute(f"""SELECT number, pin FROM card WHERE number = {card} and pin = '{pin}'""")
        exe = self.cur.fetchone()
        if exe is not None and card == int(exe[0]) and pin == exe[1]:
            print("You have successfully logged in!")
            print()
            self.account_menu(card)
        else:
            print("Wrong card number or PIN!")
            self.firs_menu()

    def account_menu(self, card):
        act = int(input("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit"""))
        print()
        if act == 1:
            balance = self.balance(card)
            print(f"Balance: {balance}")
            self.account_menu(card)
        elif act == 2:
            money = int(input("Enter income:"))
            self.add_income(card, money)
            print("Income was added!")
            print()
            self.account_menu(card)
        elif act == 3:
            card_to = input("Enter card number:")
            self.do_transfer(card, card_to)
            self.account_menu(card)
        elif act == 4:
            self.close_account(card)
            print("The account has been closed!")
            self.firs_menu()
        elif act == 5:
            print("You have successfully logged out!")
            self.firs_menu()
        else:
            self.exit()
            print("Bye!")

    def exit(self):
        self.conn.close()

    def luhn_algorithm(self, card):
        card_ = str(card)
        card = [int(x) for x in card_]
        for i in range(len(card)):
            if i % 2 == 0:
                card[i] = card[i] * 2
            if card[i] > 9:
                card[i] = card[i] - 9
        last_dig = 10 - sum(card) % 10
        if last_dig == 10:
            last_dig = 0
        return int(card_ + str(last_dig))

    def add_value(self, id, card, pin):
        self.cur.execute(f"""INSERT INTO card (id, number, pin) VALUES ({id}, {card}, "{pin}")""")
        self.conn.commit()

    def balance(self, card):
        self.cur.execute(f"""SELECT balance FROM card WHERE number = {card}""")
        return self.cur.fetchone()[0]

    def add_income(self, card, money):
        current_balance = self.balance(card)
        add_money = current_balance + money
        self.cur.execute(f"""UPDATE card SET balance = {add_money} WHERE number = {card}""")
        self.conn.commit()

    def check_exist(self, card):
        self.cur.execute(f"""SELECT * FROM card WHERE number = {card}""")
        return self.cur.fetchone()

    def do_transfer(self, card_from, card_to):
        if card_from == card_to:
            print("You can't transfer money to the same account!")
        elif str(self.luhn_algorithm(card_to[:-1])) != card_to:
            print("Probably you made a mistake in the card number. Please try again!")
        elif self.check_exist(card_to) is None:
            print("Such a card does not exist.")
        else:
            money = int(input("Enter how much money you want to transfer:"))
            if self.balance(card_from) < money:
                print("Not enough money!")
            else:
                self.add_income(card_from, -money)
                self.add_income(card_to, money)
                print("Success!")

    def close_account(self, card):
        self.cur.execute(f"""DELETE FROM card WHERE number = {card}""")
        self.conn.commit()


bank = BankingSystem()
bank.firs_menu()
