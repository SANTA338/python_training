print("welcome to the ATM ")
pin=1501
acc=1234567890
while True:
    pin=int(input("Enter the pin code"))
    if pin==1501:
        print("correct pin code")
        
    acc=int(input("Enter the acc number"))
    if acc==1234567890:
        print("withdrawl or deposite")
        break
    else:
        print("invalied pin code")    
