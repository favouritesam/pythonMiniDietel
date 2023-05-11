class Account:
    def __init__(self, name, pin):
        self._withdraw = 0
        self._name = name
        self._pin = pin
        self._balance = 0

    def check_balance(self, pin):
        if pin == self._pin:
            return self._balance

    def deposit(self, amount):
        self._balance = self._balance + amount

    def withdraw(self, amount, pin):
        if pin == self._pin:
            self._balance -= amount
            return self._balance
