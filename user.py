class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
        self.account_balance += amount	
    def makeWithdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.name +  " Balance $", self.account_balance)
    def tranfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(other_user.account_balance)


guido = User("Guido", "guido@mail.com")
monty = User("Monty", "monty@mail.com")
guido.make_deposit(300)
monty.make_deposit(200)
print(guido.account_balance)
print(monty.account_balance)
guido.makeWithdrawal(150)
monty.makeWithdrawal(50)
print(guido.account_balance)
print(monty.account_balance)
guido.display_user_balance()
guido.tranfer_money(monty, 25)

