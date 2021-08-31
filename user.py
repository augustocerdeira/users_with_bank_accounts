class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
        self.account_balance += amount	
        return self
    def makeWithdrawal(self,amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name +  " Balance $", self.account_balance)
        return self
    def tranfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(other_user.account_balance)
        return self


guido = User("Guido", "guido@mail.com")
monty = User("Monty", "monty@mail.com")
guido.make_deposit(300).makeWithdrawal(150).display_user_balance().tranfer_money(monty, 25)
monty.make_deposit(200).makeWithdrawal(50)
print(guido.account_balance)
print(monty.account_balance)


