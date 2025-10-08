class bank:
    def __init__(self,balance):
        acc_num=int(input("Enter your acc number:"))
        acc_name=input("Enter your name")
        self.balance=balance
    def depo(self,amount):
        if amount>0:
            self.balance+=amount
            print("your deposite",amount,"tol amount",self.balance)
            
        else:
            print("money is't deposite")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance-=amount
            print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
    

b1=bank(50)
b1.depo(500)
b1.withdraw(5)
