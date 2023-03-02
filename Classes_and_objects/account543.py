class Account:
    def __init__(self, id: int, name: str, balance=0):
        self.balance = balance
        self.id = id
        self.name = name

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return f'Amount exceeded balance'

    def info(self):
        return f'User {self.name} with account {self.id} has {self.balance} balance'


account = Account(123, 'George', 1000)
account.credit(1000)
print(account.info())
