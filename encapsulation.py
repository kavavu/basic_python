#it restricts access to certain attributes and methods to prevent direct modification
class  bankaccount:
    def __init__(self,balance):
        self.__balannce=balance
    def deposit(self,amount):
        if amount >0 and amount<=1000000:
            self.__balannce+=amount
    def get_balance(self):
        return self.__balannce
    

account=bankaccount(2500)
account.deposit(350)
print("balance", account.get_balance())