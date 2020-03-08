from result import Ok, Error


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def try_withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return Ok('Money was paid out', amount)
        return Error('Too little money in the account', amount)

    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimum_balance=1000):
        super().__init__(balance)
        self.minimumBalance = minimum_balance

    def try_withdraw(self, amount):
        if self.balance - amount > self.minimumBalance:
            return super().try_withdraw(amount)
        return Result(False, 'Too little money in the account', amount)

    def __str__(self):
        return str(self.balance)