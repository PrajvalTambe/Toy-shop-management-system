from tkinter import *
from PIL import ImageTk,Image

from bill import *
from add_product import *
from add_stock import *
from add_supplier import *
from supplier_details import *
from product_details import *
from bill_details import *

import os


def __information__():
    filename = 'AddProduct_F.py'
    os.system(filename)
    os.system('notepad' + filename)


def __FeeReport__():
    filename = 'Bill_F.py'
    os.system(filename)
    os.system('notepad' + filename)

mydb = mysql.connector.connect(host= "localhost",user = "root",password= "root",database="mydb")
mycursor = mydb.cursor()
mydb.commit()

screen = Tk()
screen.title("Main")
screen.geometry("1350x750")
screen.config(bg="lightblue")




headingFrame1 = Frame(screen,bg="orange",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to Toy Shop", bg='Navajo white', fg='black', font=('Times New Roman',24))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

my_menu=Menu(screen)
screen.config(menu=my_menu)


C_Bill = Button(screen,text="Customer Bill",bg='lightgrey', fg='black',font=("Times New Roman",16),command=bill)
C_Bill.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

Add_Product = Button(screen,text="Add Product",bg='lightgrey', fg='black',font=("Times New Roman",16), command=aproduct)
Add_Product.place(relx=0.28,rely=0.41, relwidth=0.45,relheight=0.1)

Add_Stock = Button(screen,text="Add Stock",bg='lightgrey', fg='black',font=("Times New Roman",16), command=a_stock)
Add_Stock.place(relx=0.28,rely=0.52, relwidth=0.45,relheight=0.1)

Add_Supplier = Button(screen,text="Add Supplier",bg='lightgrey', fg='black',font=("Times New Roman",16), command=a_supplier)
Add_Supplier.place(relx=0.28,rely=0.63, relwidth=0.45,relheight=0.1)

Supplier_Details = Button(screen,text="Supplier Details",bg='lightgrey', fg='black',font=("Times New Roman",16), command=supplier_d)
Supplier_Details.place(relx=0.14,rely=0.74, relwidth=0.25,relheight=0.1)

Product_Details = Button(screen,text="Product Details",bg='lightgrey', fg='black',font=("Times New Roman",16), command=product_d)
Product_Details.place(relx=0.4,rely=0.74, relwidth=0.25,relheight=0.1)

Product_Details = Button(screen,text="Bill Details",bg='lightgrey', fg='black',font=("Times New Roman",16), command=bill_d)
Product_Details.place(relx=0.66,rely=0.74, relwidth=0.25,relheight=0.1)

screen.mainloop()
