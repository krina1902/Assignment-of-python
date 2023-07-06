import datetime
import collections
d={}
class Customer:
            def add_customer(self,cname,acno,balance):
                self.cname=cname
                self.acno=acno
                self.balance=balance
            def display(self):
                print("Customer Name is:",self.cname)
                print("Customer Account Number is:",self.acno)
                print("Customer Balance is:",self.balance)
def withdraw(amount):
    if amount<=d[ac]['Balance']:
        d[ac]['Balance']=d[ac]['Balance']-amount
    else:
        needs=amount-d[ac]['Balance']
        print("Sorry,you need",needs,"more rupees for withdrawl amount..")
def deposit(amount):
    d[ac]['Balance']=d[ac]['Balance']+amount
def checkbalance():
    print("Your Current Balance is:",d[ac]['Balance'])
    

print("****************WELCOME TO PYTHON MANAGEMENT SYSTEM ********************")
while True:
    print("<<<<<<<<<<<<<<<<<<<<<<<<<< Select your role <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("1. Banker")
    print("2. Customer")
    print("3. Exit")
    select=int(input("Select your role:"))
    b=Customer()
    if select==1:                  
        while True:
            print("^^^^^^^^^^^^^^^^^^^^^^Welcome To Banker's App ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<< Operation Menu >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
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
                print("Thank You For Using Our Banker Services...")
                break
            else:
                print("Invalid Choice. Better Luck Next Time.")


    elif select==2:
        b.add_customer(cname,acno,balance)    
        while True:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ WELCOME TO COUSTMOER'S APP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Operation Menu >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("1. Withdraw Amount")
                print("2. Deposit Amount")
                print("3. Exit")
                choose=int(input("Enter operation which you want to perform:"))
            
                if choose==1:
                    ac=int(input("Enter Your Account Number:"))
                    print(d[ac])
                    checkbalance()
                    amount=int(input("Enter Your Withdrawl Amount:"))
                    withdraw(amount)
                    checkbalance()
                elif choose==2:
                    ac=int(input("Enter Your Account Number:"))
                    print(d[ac])
                    checkbalance()
                    amount=int(input("Enter Your Deposit Amount:"))
                    deposit(amount)
                    checkbalance()
                elif choose==3:
                    print("Thank You For Using Our Customer Service.")
                    break
                else:
                    print("Invalid Choice. Better Luck Next Time.")


    elif select==3:
        print("THANK YOU FOR USING OUR PYTHON MANAGEMENT SYSTEM")
        break
    else:
        print("Invalid choice. If you want use our services then select option from above menu...")
        
                        
                    
           
            
                        
                    
        
    
