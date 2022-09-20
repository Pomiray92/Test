class Bank_Account:
    
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport
        pass
    
account1 = Bank_Account("Bob", 10000, 12451245)

print(account1)