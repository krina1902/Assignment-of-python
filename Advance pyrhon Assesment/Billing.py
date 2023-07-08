from tkinter import *

#tk
root=Tk()
root.title("Billing Software")
root.geometry("1000x600")
root.resizable(width=False,height=False)


#design
head=Label(root,text="Billing Software",font=("Arial",20),fg="white",bg="RoyalBlue3",relief=GROOVE,bd=8)
head.pack(fill=X,pady=2)
#customer
customer_frame=LabelFrame(root,text="Customer Details",font=("Arial",10),fg="gold",bg="RoyalBlue3",relief=GROOVE,bd=8)
customer_frame.pack(fill=X)

l_name=Label(customer_frame,text="Customer Name",font=("Arial",12),fg="white",bg="RoyalBlue3")
l_name.grid(row=0,column=0)
e_name=Entry(customer_frame,relief=GROOVE,bd=5,width=30)
e_name.grid(row=0,column=1,padx=8)

l_phone=Label(customer_frame,text="Phone No",font=("Arial",12),fg="white",bg="RoyalBlue3")
l_phone.grid(row=0,column=2)
e_phone=Entry(customer_frame,relief=GROOVE,bd=5,width=30)
e_phone.grid(row=0,column=3,padx=8)

l_billno=Label(customer_frame,text="Bill No.",font=("Arial",12),fg="white",bg="RoyalBlue3")
l_billno.grid(row=0,column=4)
e_billno=Entry(customer_frame,relief=GROOVE,bd=5)
e_billno.grid(row=0,column=5,padx=8)

b_enter=Button(customer_frame,text="Enter",font=("Arial",12),fg="white",bg="RoyalBlue3",relief=GROOVE,bd=8,padx=15)
b_enter.grid(row=0,column=6,pady=3,padx=18)
#cosmetics
pf=Frame(root)
pf.pack()

cos=LabelFrame(pf,text="Cosmetics",font=("Arial",10),fg="gold",bg="RoyalBlue3",relief=GROOVE,bd=8)
cos.grid(row=0,column=0)

l_bath=Label(cos,text="Bath Soap",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_bath.grid(row=0,column=0)
e_bath=Entry(cos,relief=GROOVE,bd=5)
e_bath.grid(row=0,column=1,padx=5,pady=10)

l_cream=Label(cos,text="Face Cream",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_cream.grid(row=1,column=0)
e_cream=Entry(cos,relief=GROOVE,bd=5)
e_cream.grid(row=1,column=1,padx=5,pady=10)

l_wash=Label(cos,text="Face Wash",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_wash.grid(row=2,column=0)
e_wash=Entry(cos,relief=GROOVE,bd=5)
e_wash.grid(row=2,column=1,padx=5,pady=10)

l_spray=Label(cos,text="Hair Spray",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_spray.grid(row=3,column=0)
e_spray=Entry(cos,relief=GROOVE,bd=5)
e_spray.grid(row=3,column=1,padx=5,pady=10)

l_lotion=Label(cos,text="Hair Lotion",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_lotion.grid(row=4,column=0)
e_lotion=Entry(cos,relief=GROOVE,bd=5)
e_lotion.grid(row=4,column=1,padx=5,pady=10)

#grocery
gro=LabelFrame(pf,text="Grocery",font=("Arial",10),fg="gold",bg="RoyalBlue3",relief=GROOVE,bd=8)
gro.grid(row=0,column=1)


