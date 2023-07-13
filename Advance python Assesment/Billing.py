from tkinter import *
import mysql.connector
import tkinter.messagebox as msg
import random


def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="billing"
        )

#functioality
def total():
    global soap,facecream,hairspray,facewash,lotion,rice,food,daal,wheat,sugar,maza,coke,frooti,nimkos,bis,totalbill
    global totalcprice,totalctax,totalgprice,totalgtax,totaloprice,totalotax
    #cos
    soap=int(e_bath.get())*15
    facecream=int(e_cream.get())*50
    facewash=int(e_wash.get())*100
    hairspray=int(e_spray.get())*150
    lotion=int(e_lotion.get())*120
    totalcprice=soap+facecream+facewash+hairspray+lotion
    e_tc.delete(0,END)
    e_tc.insert(0,"Rs."+str(totalcprice))
    e_ct.delete(0,END)
    totalctax=totalcprice*0.12
    e_ct.insert(0,"Rs."+str(totalctax))
    #gro
    rice=int(e_rice.get())*180
    food=int(e_food.get())*200
    daal=int(e_daal.get())*90
    wheat=int(e_wheat.get())*78
    sugar=int(e_sugar.get())*55
    totalgprice=rice+food+daal+wheat+sugar
    e_tg.delete(0,END)
    e_tg.insert(0,"Rs."+str(totalgprice))
    e_gt.delete(0,END)
    totalgtax=totalgprice*0.10
    e_gt.insert(0,"Rs."+str(totalgtax))
    #oth
    maza=int(e_maza.get())*15
    coke=int(e_coke.get())*20
    frooti=int(e_frooti.get())*30
    nimkos=int(e_nimkos.get())*40
    bis=int(e_bis.get())*12
    totaloprice=maza+coke+frooti+nimkos+bis
    e_og.delete(0,END)
    e_og.insert(0,"Rs."+str(totaloprice))
    e_ot.delete(0,END)
    totalotax=totaloprice*0.5
    e_ot.insert(0,"Rs."+str(totalotax))
    totalbill=totalcprice+totalctax+totalgprice+totalgtax+totaloprice+totalotax

    

def bill():
    
    if e_name.get()=="" or e_phone.get()=="":
        msg.showinfo("Insert status","Customer Deatails Are Mandotary")
    elif e_tc.get()=="" and e_tg.get()=="" and e_og.get()=="":
        msg.showinfo("Insert status","No Products Are Selected")
    elif e_tc.get()=="Rs.0" and e_tg.get()=="Rs.0" and e_og.get()=="Rs.0":
        msg.showinfo("Insert status","No Products Are Selected")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into billing_software(Bill_no,Customer_name,Phone_no,Total_cosmetics,Total_grocery,Others_total,Cosmetics_tax,Grocery_tax,Others_tax) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        argu=(e_billno.get(),e_name.get(),e_phone.get(),e_tc.get(),e_tg.get(),e_og.get(),e_ct.get(),e_gt.get(),e_og.get())
        cursor.execute(query,argu)
        conn.commit()
        conn.close()
        textarea.delete(1.0,END)
        textarea.insert(END,"********WELCOME CUSTOMER**********")
        textarea.insert(END,"\n\nBill Number:"+ e_billno.get())
        textarea.insert(END,"\nCustomer Name:"+ e_name.get())
        textarea.insert(END,"\nPhone Number:"+ e_phone.get())
        textarea.insert(END,"\n===================================")
        textarea.insert(END,"\nProduct\t\tQTY\tPrice")
        textarea.insert(END,"\n===================================")
        if e_bath.get()!="0":
            textarea.insert(END,"\nBath Soap\t\t"+str(e_bath.get())+"\t"+str(soap))
        if e_cream.get()!="0":
            textarea.insert(END,"\nFacecream\t\t"+str(e_cream.get())+"\t"+str(facecream))
        if e_wash.get()!="0":
            textarea.insert(END,"\nFacewash\t\t"+str(e_wash.get())+"\t"+str(facewash))
        if e_spray.get()!="0":
            textarea.insert(END,"\nHairspray\t\t"+str(e_spray.get())+"\t"+str(hairspray))
        if e_lotion.get()!="0":
            textarea.insert(END,"\nBodylotion\t\t"+str(e_lotion.get())+"\t"+str(lotion))


        if e_rice.get()!="0":
            textarea.insert(END,"\nRice\t\t"+str(e_bath.get())+"\t"+str(rice))
        if e_food.get()!="0":
            textarea.insert(END,"\nFood\t\t"+str(e_cream.get())+"\t"+str(food))
        if e_daal.get()!="0":
            textarea.insert(END,"\nDaal\t\t"+str(e_wash.get())+"\t"+str(daal))
        if e_wheat.get()!="0":
            textarea.insert(END,"\nWheat\t\t"+str(e_wheat.get())+"\t"+str(wheat))
        if e_sugar.get()!="0":
            textarea.insert(END,"\nSugar\t\t"+str(e_lotion.get())+"\t"+str(sugar))
            

        if e_maza.get()!="0":
            textarea.insert(END,"\nMaza\t\t"+str(e_maza.get())+"\t"+str(maza))
        if e_coke.get()!="0":
            textarea.insert(END,"\nCoke\t\t"+str(e_coke.get())+"\t"+str(coke))
        if e_frooti.get()!="0":
            textarea.insert(END,"\nFrooti\t\t"+str(e_frooti.get())+"\t"+str(frooti))
        if e_nimkos.get()!="0":
            textarea.insert(END,"\nNimkos\t\t"+str(e_nimkos.get())+"\t"+str(nimkos))
        if e_bis.get()!="0":
            textarea.insert(END,"\nBiscuits\t\t"+str(e_bis.get())+"\t"+str(bis))

        textarea.insert(END,"\n===================================")
        if e_ct.get()!="Rs.0.0":
            textarea.insert(END,"\nCosmetic Tax\t\t"+str(e_ct.get()))
        if e_gt.get()!="Rs.0.0":
            textarea.insert(END,"\nGrocery Tax\t\t"+str(e_gt.get()))
        if e_og.get()!="Rs.0.0":
            textarea.insert(END,"\nOthers Tax\t\t"+str(e_og.get()))
        textarea.insert(END,"\n===================================")
        textarea.insert(END,"\nTotal Bill\t\t"+"Rs."+str(totalbill))


def clear():
    e_tc.delete(0,END)
    e_tg.delete(0,END)
    e_og.delete(0,END)
    e_ct.delete(0,END)
    e_gt.delete(0,END)
    e_ot.delete(0,END)

    e_bath.delete(1,END)
    e_cream.delete(1,END)
    e_wash.delete(1,END)
    e_spray.delete(1,END)
    e_lotion.delete(1,END)

    e_rice.delete(1,END)
    e_food.delete(1,END)
    e_daal.delete(1,END)
    e_wheat.delete(1,END)
    e_sugar.delete(1,END)

    e_maza.delete(1,END)
    e_coke.delete(1,END)
    e_frooti.delete(1,END)
    e_nimkos.delete(1,END)
    e_bis.delete(1,END)

    e_name.delete(0,END)
    e_phone.delete(0,END)
    e_billno.delete(0,END)

def exit1():
    root.destroy()
    
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
e_bath.insert(0,0)

l_cream=Label(cos,text="Face Cream",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_cream.grid(row=1,column=0)
e_cream=Entry(cos,relief=GROOVE,bd=5)
e_cream.grid(row=1,column=1,padx=5,pady=10)
e_cream.insert(0,0)

l_wash=Label(cos,text="Face Wash",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_wash.grid(row=2,column=0)
e_wash=Entry(cos,relief=GROOVE,bd=5)
e_wash.grid(row=2,column=1,padx=5,pady=10)
e_wash.insert(0,0)

l_spray=Label(cos,text="Hair Spray",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_spray.grid(row=3,column=0)
e_spray=Entry(cos,relief=GROOVE,bd=5)
e_spray.grid(row=3,column=1,padx=5,pady=10)
e_spray.insert(0,0)

l_lotion=Label(cos,text="Hair Lotion",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_lotion.grid(row=4,column=0)
e_lotion=Entry(cos,relief=GROOVE,bd=5)
e_lotion.grid(row=4,column=1,padx=5,pady=10)
e_lotion.insert(0,0)

#grocery
gro=LabelFrame(pf,text="Grocery",font=("Arial",10),fg="gold",bg="RoyalBlue3",relief=GROOVE,bd=8)
gro.grid(row=0,column=1)

l_rice=Label(gro,text="Rice",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_rice.grid(row=0,column=1)
e_rice=Entry(gro,relief=GROOVE,bd=5)
e_rice.grid(row=0,column=2,padx=5,pady=10)
e_rice.insert(0,0)

l_food=Label(gro,text="Food Oil",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_food.grid(row=1,column=1)
e_food=Entry(gro,relief=GROOVE,bd=5)
e_food.grid(row=1,column=2,padx=5,pady=10)
e_food.insert(0,0)

l_daal=Label(gro,text="Daal",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_daal.grid(row=3,column=1)
e_daal=Entry(gro,relief=GROOVE,bd=5)
e_daal.grid(row=3,column=2,padx=5,pady=10)
e_daal.insert(0,0)

l_wheat=Label(gro,text="Wheat",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_wheat.grid(row=4,column=1)
e_wheat=Entry(gro,relief=GROOVE,bd=5)
e_wheat.grid(row=4,column=2,padx=5,pady=10)
e_wheat.insert(0,0)

l_sugar=Label(gro,text="Sugar",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_sugar.grid(row=5,column=1)
e_sugar=Entry(gro,relief=GROOVE,bd=5)
e_sugar.grid(row=5,column=2,padx=5,pady=10)
e_sugar.insert(0,0)

#others
oth=LabelFrame(pf,text="Others",font=("Arial",10),fg="gold",bg="RoyalBlue3",relief=GROOVE,bd=8)
oth.grid(row=0,column=2)

l_maza=Label(oth,text="Maza",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_maza.grid(row=0,column=0)
e_maza=Entry(oth,relief=GROOVE,bd=5)
e_maza.grid(row=0,column=1,padx=5,pady=10)
e_maza.insert(0,0)

l_coke=Label(oth,text="Coke",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_coke.grid(row=1,column=0)
e_coke=Entry(oth,relief=GROOVE,bd=5)
e_coke.grid(row=1,column=1,padx=5,pady=10)
e_coke.insert(0,0)

l_frooti=Label(oth,text="Frooti",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_frooti.grid(row=2,column=0)
e_frooti=Entry(oth,relief=GROOVE,bd=5)
e_frooti.grid(row=2,column=1,padx=5,pady=10)
e_frooti.insert(0,0)

l_nimkos=Label(oth,text="Nimkos",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_nimkos.grid(row=3,column=0)
e_nimkos=Entry(oth,relief=GROOVE,bd=5)
e_nimkos.grid(row=3,column=1,padx=5,pady=10)
e_nimkos.insert(0,0)

l_bis=Label(oth,text="Biscuits",font=("Arial",11),fg="white",bg="RoyalBlue3")
l_bis.grid(row=4,column=0)
e_bis=Entry(oth,relief=GROOVE,bd=5)
e_bis.grid(row=4,column=1,padx=5,pady=10)
e_bis.insert(0,0)

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

total=Button(bt_frame,text="Total",font=("Arial",11),fg="white",bg="RoyalBlue3",bd=7,width=8,command=total)
total.grid(row=0,column=0,padx=10)

bill=Button(bt_frame,text="Generate Bill",font=("Arial",11),fg="white",bg="RoyalBlue3",bd=7,width=10,command=bill)
bill.grid(row=0,column=1,padx=10)

clear=Button(bt_frame,text="Clear",font=("Arial",11),fg="white",bg="RoyalBlue3",bd=7,width=8,command=clear)
clear.grid(row=0,column=2,padx=10)

exi=Button(bt_frame,text="Exit",font=("Arial",11),fg="white",bg="RoyalBlue3",bd=7,width=8,command=exit1)
exi.grid(row=0,column=3,padx=10)


root.mainloop()






