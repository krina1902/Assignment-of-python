from tkinter import *

#tk
root=Tk()
root.title("Billing Software")
root.geometry("1000x560")
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
pf.pack(fill=X,pady=2)

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

l_rice=Label(gro,text="Rice",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_rice.grid(row=0,column=1)
e_rice=Entry(gro,relief=GROOVE,bd=5)
e_rice.grid(row=0,column=2,padx=5,pady=10)

l_food=Label(gro,text="Food Oil",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_food.grid(row=1,column=1)
e_food=Entry(gro,relief=GROOVE,bd=5)
e_food.grid(row=1,column=2,padx=5,pady=10)

l_daal=Label(gro,text="Daal",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_daal.grid(row=3,column=1)
e_daal=Entry(gro,relief=GROOVE,bd=5)
e_daal.grid(row=3,column=2,padx=5,pady=10)

l_wheat=Label(gro,text="Wheat",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_wheat.grid(row=4,column=1)
e_wheat=Entry(gro,relief=GROOVE,bd=5)
e_wheat.grid(row=4,column=2,padx=5,pady=10)

l_sugar=Label(gro,text="Sugar",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_sugar.grid(row=5,column=1)
e_sugar=Entry(gro,relief=GROOVE,bd=5)
e_sugar.grid(row=5,column=2,padx=5,pady=10)

#others
oth=LabelFrame(pf,text="Others",font=("Arial",10),fg="gold",bg="RoyalBlue3",relief=GROOVE,bd=8)
oth.grid(row=0,column=2)

l_maza=Label(oth,text="Maza",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_maza.grid(row=0,column=0)
e_maza=Entry(oth,relief=GROOVE,bd=5)
e_maza.grid(row=0,column=1,padx=5,pady=10)

l_coke=Label(oth,text="Coke",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_coke.grid(row=1,column=0)
e_coke=Entry(oth,relief=GROOVE,bd=5)
e_coke.grid(row=1,column=1,padx=5,pady=10)

l_frooti=Label(oth,text="Frooti",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_frooti.grid(row=2,column=0)
e_frooti=Entry(oth,relief=GROOVE,bd=5)
e_frooti.grid(row=2,column=1,padx=5,pady=10)

l_nimkos=Label(oth,text="Nimkos",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_nimkos.grid(row=3,column=0)
e_nimkos=Entry(oth,relief=GROOVE,bd=5)
e_nimkos.grid(row=3,column=1,padx=5,pady=10)

l_bis=Label(oth,text="Biscuits",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_bis.grid(row=4,column=0)
e_bis=Entry(oth,relief=GROOVE,bd=5)
e_bis.grid(row=4,column=1,padx=5,pady=10)

#billframe
b_frame=Frame(pf,bd=8,relief=GROOVE)
b_frame.grid(row=0,column=3)

b_area=Label(b_frame,text="Bill Area",font=("Arial",12),bd=7,relief=GROOVE)
b_area.pack(fill=X)

scrollbar=Scrollbar(b_frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(b_frame,height=13,width=35,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

#billmenu

bm_frame=LabelFrame(root,text="Bill Menu",font=("Arial",10),fg="gold",bg="RoyalBlue3",relief=GROOVE,bd=8)
bm_frame.pack(fill=X)

l_tc=Label(bm_frame,text="Total Cosmetics",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_tc.grid(row=0,column=0)
e_tc=Entry(bm_frame,relief=GROOVE,bd=5)
e_tc.grid(row=0,column=1,padx=5,pady=10)

l_tg=Label(bm_frame,text="Total Grocery",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_tg.grid(row=1,column=0)
e_tg=Entry(bm_frame,relief=GROOVE,bd=5)
e_tg.grid(row=1,column=1,padx=5,pady=10)

l_og=Label(bm_frame,text="Others Total",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_og.grid(row=2,column=0)
e_og=Entry(bm_frame,relief=GROOVE,bd=5)
e_og.grid(row=2,column=1,padx=5,pady=10)


l_ct=Label(bm_frame,text="Cosmetics Tax",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_ct.grid(row=0,column=2)
e_ct=Entry(bm_frame,relief=GROOVE,bd=5)
e_ct.grid(row=0,column=3,padx=5,pady=10)

l_gt=Label(bm_frame,text="Grocery Tax",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_gt.grid(row=1,column=2,padx=10)
e_gt=Entry(bm_frame,relief=GROOVE,bd=5)
e_gt.grid(row=1,column=3,padx=5,pady=10)

l_ot=Label(bm_frame,text="Others Tax",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_ot.grid(row=2,column=2,padx=10)
e_ot=Entry(bm_frame,relief=GROOVE,bd=5)
e_ot.grid(row=2,column=3,padx=5,pady=10)

bt_frame=Frame(bm_frame,bg="RoyalBlue3")
bt_frame.grid(row=0,column=4,rowspan=3)

total=Button(bt_frame,text="Total",font=("Arial",11),fg="white",bg="RoyalBlue3",bd=7,width=8)
total.grid(row=0,column=0,padx=10)

bill=Button(bt_frame,text="Generate Bill",font=("Arial",11),fg="white",bg="RoyalBlue3",bd=7,width=10)
bill.grid(row=0,column=1,padx=10)

clear=Button(bt_frame,text="Clear",font=("Arial",11),fg="white",bg="RoyalBlue3",bd=7,width=8)
clear.grid(row=0,column=2,padx=10)

exi=Button(bt_frame,text="Exit",font=("Arial",11),fg="white",bg="RoyalBlue3",bd=7,width=8)
exi.grid(row=0,column=3,padx=10)







