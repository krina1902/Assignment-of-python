import datetime
import collections

d={}
class Bank:
    def add_customer(self,cname,acno,balance):
            self.cname=cname
            self.acno=acno
            self.balance=balance
    def display(self):
        print("Customer Name is:",self.cname)
        print("Customer Account Number is:",self.acno)
        print("Customer Balance is:",self.balance)
        
b=Bank()

while True:
    print("########## Welcome To Banker's App ##############")
    print("Operation Menu")
    print("1. Add Customer")
    print("2. View Customer")
    print("3. Search Customer")
    print("4. View All Customer")
    print("5. Total Amount In Bank")
    print("6. Exit")
    print("*"*70)

    choice=int(input ("Enter operation which you want to perform:"))
    if choice==1:
        cname=input("Enter customer name:")
        acno=int(input("Enter account number:"))
        balance=int(input("Enter balance:"))
        b.add_customer(cname,acno,balance)
        date=str(datetime.datetime.now())
        d.update({acno:{"name":cname,"Balance":balance,"Opening_Date":date}})
    elif choice==2:
        b.display()
    elif choice==3:
        ac=int(input("Enter Your Account Number:"))
        print(d[ac])
    elif choice==4:
        print(d)
    elif choice==5:
        TotalAmount = sum(i['Balance'] for i in d.values() if i)
        print("Total Amount In Bank Is:",TotalAmount)
    elif choice==6:
        print("Thank You For Use Our Services...")
        break
    else:
        print("Invalid Choice. Better Luck Next Time.")
        
    
