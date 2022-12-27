from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

def add_stock():
    product_id =productid_entry.get()
    #category = category_entry.get()
    product_name = pname_entry.get()
    current_stock = cstock_entry.get()
    new_stock=nstock_entry.get()

    con = mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")
    cur = con.cursor()
    addStock = "INSERT INTO add_stock(product_id, category, product_name, current_stock, new_stock) VALUES(%s,%s,%s,%s,%s)"
    val = (product_id, product_name, current_stock, new_stock)
    try:
        cur.execute(addStock, val)
        con.commit()
        messagebox.showinfo('Success', "Stock added successfully")
        screen.destroy()
    except:
        messagebox.showinfo("Error", "Can't add data into Database")


    print(product_id)

    print(product_name)
    print(current_stock)
    print(new_stock)

def a_stock():
    global con,cur,table,productid_entry,category_entry,pname_entry,cstock_entry,nstock_entry,screen

    screen = Tk()
    screen.title("Add Stock")
    screen.geometry("900x550")
    screen.config(bg="lightblue")

    # table name
    table = "add_stock"

    #Add Stock frame
    addstock_frame = Frame(screen,width="600",height="300",bg="Navajo white",bd=8, relief='ridge')
    addstock_frame.place(x="150",y="120")

    #Add Stock frame items
    #labels
    #1
    toy_label = Label(screen,text="TOY SHOP MANAGEMENT SYSTEM",fg="black",bg="lightblue",font=("Times New Roman",20,'underline'))
    toy_label.place(x="0",y="0")
    #2
    addstock_label = Label(screen,text="Add Product Stock",fg="black",bg="lightblue",font=("Times New Roman",20))
    addstock_label.place(x="350",y="80")
    #3
    productid_label = Label(screen,text="Product ID:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    productid_label.place(x="270",y="150")
    #4
    #category_label = Label(screen,text="Category:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    #category_label.place(x="270",y="200")
    #5
    pname_label = Label(screen,text="Product Name:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    pname_label.place(x="270",y="200")
    #6
    cstock_label = Label(screen,text="Current Stock:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    cstock_label.place(x="270",y="250")
    #7
    nstock_label = Label(screen,text="New Stock:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    nstock_label.place(x="270",y="300")


    #Entry
    #1
    productid_entry = Entry(screen,selectforeground="black",font=(12))
    productid_entry.place(x="420",y="150")
    #2
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")
    cur = con.cursor()

    option = []
    sql = "SELECT product_name FROM add_product"
    cur.execute(sql)
    ids = cur.fetchall()
    for i in ids:
        option.append(str(i[0]))

    pname_entry = ttk.Combobox(screen,font=(12))
    pname_entry['values']=option
    pname_entry.place(x="420",y="200")
    #3
    cstock_entry = Entry(screen,selectforeground="black",font=(12))
    cstock_entry.place(x="420",y="250")
    #4
    nstock_entry = Entry(screen,selectforeground="black",font=(12))
    nstock_entry.place(x="420",y="300")

    #Buttons
    #1
    save_btn = Button(screen, text="SUBMIT",font=( 'arial', 14, 'bold'), width=10,command= add_stock)
    save_btn.place(x=260, y=350, relwidth=0.18, relheight=0.08)
    #2
    clear_btn =Button(screen, text="Quit",font=( 'arial', 14, 'bold'), width=10, command=screen.destroy)
    clear_btn.place(x=500, y=350, relwidth=0.18, relheight=0.08)
    screen.mainloop()
