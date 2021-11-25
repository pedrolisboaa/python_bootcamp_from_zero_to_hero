class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        print('Deposit Accepted')

    def withdraw(self, value):
        if not value > self.balance:
            self.balance -= value
            print('Withdrawal Accepted')
        else:
            print(f'Funds Unavailable!')

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'


if __name__ == '__main__':
    ac = Account('Pedro', 100)
    print(ac)
    print(ac.owner)
    print(ac.balance)

    ac.deposit(50)
    print(ac.balance)
    ac.withdraw(75)
    print(ac.balance)
    ac.withdraw(500)
    print(ac.balance)
