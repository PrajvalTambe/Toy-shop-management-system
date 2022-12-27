from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def bill1():
    customer_id = customerid_entry.get()
    customer_name = c_name_entry.get()
    product_name = product_name_entry.get()
    date = date_entry.get()
    mobile_no = mo_no_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    total = total_entry.get()

    con = mysql.connector.connect(host="localhost", user="root", password="root",database="mydb")
    cur=con.cursor()

    billinfo = "INSERT INTO bill(customer_id,customer_name, product_name, date, mobile_no, price, quantity, total) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (customer_id, customer_name,product_name, date, mobile_no, price, quantity, total)
    try:
        cur.execute(billinfo, val)
        con.commit()
        messagebox.showinfo('Success', "Bill added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(customer_id)
    print(customer_name)
    print(product_name)
    print(date)
    print(mobile_no)
    print(price)
    print(quantity)
    print(total)

def mul():
       num1 = int(price_entry.get())
       num2 = int(quantity_entry.get())
       result = num1 * num2
       total_entry.insert(END, str(result))

def Display():
    customer_id = customerid_entry.get()
    customer_name = c_name_entry.get()
    mobile_no = mo_no_entry.get()
    product_name = product_name_entry.get()
    date = date_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    total = total_entry.get()

    Label(Frame_2, text='Receipt\t', bg='white', font=('Century 18 bold')).place(x="120", y="0")

    Label(Frame_2, text='Customer Id\t:    '+customer_id, bg='white',font=('Century 12')).place(x="10",y="30")
    Label(Frame_2, text='Customer Name\t:    '+customer_name, bg='white', font=('Century 12')).place(x="10",y="60")
    Label(Frame_2, text='Mobile No\t:    ' + mobile_no, bg='white', font=('Century 12')).place(x="10",y="90")
    Label(Frame_2, text='Product Name\t:    '+product_name, bg='white', font=('Century 12')).place(x="10",y="120")
    Label(Frame_2, text='Date\t\t:    '+date, bg='white', font=('Century 12')).place(x="10",y="150")
    Label(Frame_2, text='Price\t\t:    '+price, bg='white', font=('Century 12')).place(x="10",y="200")
    Label(Frame_2, text='Quantity\t\t:    '+quantity, bg='white', font=('Century 12')).place(x="10",y="230")
    Label(Frame_2, text='Total\t\t:    '+total, bg='white', font=('Century 12')).place(x="10",y="260")


def bill():
    global screen,Frame_2,table,cur,con,customerid_entry,c_name_entry,category_entry,product_name_entry,date_entry,mo_no_entry,price_entry,quantity_entry,total_entry

    screen = Tk()
    screen.title("Add Customer")
    screen.geometry("1200x550")
    screen.config(bg="lightblue")

    #table name
    table="bill"

    #Customer frame items
    bill_frame = Frame(screen, width="750", height="370", bg="Navajo white", bd=8, relief='ridge')
    bill_frame.place(x="50", y="90")

    Frame_2 = LabelFrame(screen, width=350, height=370, bg='white', relief='ridge', bd=8,
                        text='Bill Receipt', font=('arial', 15, 'bold'))
    Frame_2.place(x='810',y='90')

    #labels
    #1
    toy_label = Label(screen,text="TOY SHOP MANAGEMENT SYSTEM",bg="lightblue",fg="black",font=("Times New Roman",20,'underline'))
    toy_label.place(x="0",y="0")
    #2
    customer_label = Label(screen,text="Customer Bill",bg="lightblue",fg="black",font=("Times New Roman",20))
    customer_label.place(x="350",y="50")
    #3
    customerid_label = Label(screen,text="Customer ID :",bg="Navajo white",fg="black",font=("Times New Roman",12))
    customerid_label.place(x="80",y="110")
    #4
    c_name_label = Label(screen,text="Customer Name :",bg="Navajo white",fg="black",font=("Times New Roman",12))
    c_name_label.place(x="80",y="155")
    #5
    mo_no_label = Label(screen,text="Mobile no :",bg="Navajo white",fg="black",font=("Times New Roman",12))
    mo_no_label.place(x="80",y="200")
    #6
    product_name_label = Label(screen,text="Product Name :",bg="Navajo white",fg="black",font=("Times New Roman",12))
    product_name_label.place(x="80",y="245")
    #7
    date_label = Label(screen,text="Date :",bg="Navajo white",fg="black",font=("Times New Roman",12))
    date_label.place(x="470",y="110")
    #9
    price_label = Label(screen,text="Price :",bg="Navajo white",fg="black",font=("Times New Roman",12))
    price_label.place(x="470",y="155")
    #10
    quantity_label = Label(screen,text="Quantity :",bg="Navajo white",fg="black",font=("Times New Roman",12))
    quantity_label.place(x="470",y="200")
    #11
    total_label = Label(screen,text="Total :",bg="Navajo white",fg="black",font=("Times New Roman",12))
    total_label.place(x="470",y="245")

    #Entry
    #1
    customerid_entry = Entry(screen,selectforeground="black",font=(12))
    customerid_entry.place(x="210",y="110")
    #2
    c_name_entry = Entry(screen,selectforeground="black",font=(12))
    c_name_entry.place(x="210",y="155")
    #3
    mo_no_entry = Entry(screen,selectforeground="black",font=(12))
    mo_no_entry.place(x="210",y="200")
    #4
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")
    cur = con.cursor()

    option = []
    sql = "SELECT product_name FROM add_product"
    cur.execute(sql)
    ids = cur.fetchall()
    for i in ids:
        option.append(str(i[0]))

    product_name_entry = ttk.Combobox(screen,font=('arial', 12), width=18)
    product_name_entry['values'] = option
    product_name_entry.place(x="210",y="245")
    #5
    date_entry = DateEntry(screen,selectforeground="black",font=(12),width=18)
    date_entry.place(x="600",y="110")
    #6
    price_entry = Entry(screen,selectforeground="black",font=(12))
    price_entry.place(x="600",y="155")
    #7
    quantity_entry = Entry(screen,selectforeground="black",font=(12))
    quantity_entry.place(x="600",y="200")
    #8
    total_entry = Entry(screen,selectforeground="black",font=(12))
    total_entry.place(x="600",y="245")

    #Buttons
    #1
    bill_btn = Button(screen,text="  Bill  ", font=( 'arial', 14, 'bold'), width=10,command=mul)
    bill_btn.place(x="400",y="300")

    #2
    quit_btn = Button(screen,text="Quit", font=( 'arial', 14, 'bold'), width=10, command=screen.destroy)
    quit_btn.place(x="600",y="380")
    #3
    submit_btn = Button(screen, text="  Submit  ", font=( 'arial', 14, 'bold'), width=10,command=bill1)
    submit_btn.place(x="200", y="380")
    Receipt_btn = Button(screen, text="  Receipt  ", font=( 'arial', 14, 'bold'), width=10,command=Display)
    Receipt_btn.place(x="400", y="380")

    screen.mainloop()
