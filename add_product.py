from tkinter import *
import mysql.connector
from tkcalendar import DateEntry
#from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import ttk



def addproduct():
    product_id =productid_entry .get()
    product_name = product_name_entry.get()
    supplier_name = sname_entry.get()
    #category = category_name_entry.get()
    stock_add_date=date_entry.get()
    p_price=pprice_entry.get()
    s_price=sprice_entry.get()
    added_stock=add_stock_entry.get()

    con = mysql.connector.connect(host="localhost", user="root", password="root",database="mydb")
    cur = con.cursor()
    productinfo = "INSERT INTO add_product(product_id,product_name,supplier_name,stock_add_date,p_price,s_price,added_stock) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val = (product_id,product_name,supplier_name,stock_add_date,p_price,s_price,added_stock)
    try:
        cur.execute(productinfo, val)
        con.commit()
        messagebox.showinfo('Success', "Product added successfully")
        screen.destroy()
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(product_id)
    print(product_name)
    print(supplier_name)

    print(stock_add_date)
    print(p_price)
    print(s_price)
    print(added_stock)

def delete():
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")
    cur = con.cursor()

    cur.execute("DELETE FROM add_product WHERE product_id="+productid_entry.get())
    con.commit()
    messagebox.showinfo('Success', "Record Deleted Successfully")
    screen.destroy()


def aproduct():

    global val,cur,con,productid_entry,product_name_entry,sname_entry,category_name_entry,date_entry,pprice_entry,sprice_entry,add_stock_entry,screen,table

    screen = Tk()
    screen.title("Add Product")
    screen.geometry("880x550")
    screen.config(bg="lightblue")

    #table name
    table="add_product"

    #Product frame
    product_frame = Frame(screen,width="750",height="370",bg="Navajo white",bd=8, relief='ridge')
    product_frame.place(x="50",y="120")


    #Product frame items
    #labels
    #1
    toy_label = Label(screen,text="TOY SHOP MANAGEMENT SYSTEM",fg="black",bg="lightblue",font=("Times New Roman",20,'underline'))
    toy_label.place(x="0",y="0")
    #2
    product_label = Label(screen,text="Add New Toy",fg="black",bg="lightblue",font=("Times New Roman",20))
    product_label.place(x="350",y="80")
    #3
    productid_label = Label(screen,text="Product ID :",fg="black",bg="Navajo white",font=("Times New Roman",12))
    productid_label.place(x="70",y="150")
    #4
    product_name_label = Label(screen,text="Product Name :",fg="black",bg="Navajo white",font=("Times New Roman",12))
    product_name_label.place(x="70",y="210")
    #5
    sname_label = Label(screen,text="Supplier Name :",fg="black",bg="Navajo white",font=("Times New Roman",12))
    sname_label.place(x="70",y="270")
    #6
    #category_name_label = Label(screen,text=" Catrgory :",fg="black",bg="Navajo white",font=("Times New Roman",12))
    #category_name_label.place(x="70",y="330")
    #7
    date_label = Label(screen,text="Stock Added Date:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    date_label.place(x="450",y="150")
    #8
    pprice_label = Label(screen,text="Purchase price :",fg="black",bg="Navajo white",font=("Times New Roman",12))
    pprice_label.place(x="450",y="210")
    #9
    sprice_label = Label(screen,text="Sales Price :",fg="black",bg="Navajo white",font=("Times New Roman",12))
    sprice_label.place(x="450",y="270")
    #10
    add_stock_label = Label(screen,text="Added Stock :",fg="black",bg="Navajo white",font=("Times New Roman",12))
    add_stock_label.place(x="260",y="330")


    #Entry
    #1
    productid_entry = Entry(screen,selectforeground="black",font=(12))
    productid_entry.place(x="200",y="150")
    #2
    product_name_entry = Entry(screen,selectforeground="black",font=(12))
    product_name_entry.place(x="200",y="210")

    con = mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")
    cur = con.cursor()

    option=[]
    sql="SELECT supplier_name FROM add_supplier"
    cur.execute(sql)
    ids=cur.fetchall()
    for i in ids:
        option.append(str(i[0]))

    sname_entry = ttk.Combobox(screen,font=(12))
    sname_entry['values']=option
    sname_entry.place(x="200",y="270")
    #4

    #category_name_entry = Entry(screen,selectforeground="black",font=(12))
    #category_name_entry.place(x="200",y="330")
    #5
    date_entry = DateEntry(screen,selectforeground="black",font=(12))
    date_entry.place(x="580",y="150")
    #6
    pprice_entry = Entry(screen,selectforeground="black",font=(12))
    pprice_entry.place(x="580",y="210")
    #7
    sprice_entry = Entry(screen,selectforeground="black",font=(12))
    sprice_entry.place(x="580",y="270")
    #8
    add_stock_entry = Entry(screen,selectforeground="black",font=(12))
    add_stock_entry.place(x="400",y="330")

    #Buttons
    #1
    SubmitBtn = Button(screen, text="SUBMIT", font=( 'arial', 14, 'bold'), width=10,command=addproduct)
    SubmitBtn.place(x=120, y=400, relwidth=0.18, relheight=0.08)

    deleteBtn = Button(screen, text="DELETE", font=('arial', 14, 'bold'), width=10,command=delete)
    deleteBtn.place(x=330, y=400, relwidth=0.18, relheight=0.08)
    #2
    quitBtn = Button(screen, text='Quite', font=( 'arial', 14, 'bold'), width=10, command=screen.destroy)
    quitBtn.place(x=550, y=400, relwidth=0.18, relheight=0.08)

    screen.mainloop()
