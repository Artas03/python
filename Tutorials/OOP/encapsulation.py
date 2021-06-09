class BankAccount:
    _money = 0

    def deposit(self, money, password):
        if (authenticate(password)):
            self.money += money

    def withdraw(self, money, password):
        if (authenitcate(password)):
            self.money -= money 

# no one has direct access to the variable _money, the user must have
# the correct password in order to change the variable throught he 
# deposit and withdraw command.