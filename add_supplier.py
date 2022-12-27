from tkinter import *
from tkinter import messagebox
import mysql.connector

def add_sup():
    supplier_id =supplierid_entry .get()
    supplier_name = sname_entry.get()
    mobile_no = mo_no_entry.get()
    adhar_no = adharno_entry.get()
    address=address_entry.get()

    con = mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")
    cur = con.cursor()
    addsupplier = "INSERT INTO add_supplier(supplier_id,supplier_name, mobile_no, adhar_no, address) VALUES(%s,%s,%s,%s,%s)"
    val= (supplier_id,supplier_name, mobile_no, adhar_no, address)
    try:
        cur.execute(addsupplier, val)
        con.commit()
        messagebox.showinfo('Success', "Supplier added successfully")
        screen.destroy()
    except:
        messagebox.showinfo("Error", "Can't add data into Database")


    print(supplier_id)
    print(supplier_name)
    print(mobile_no)
    print(adhar_no)
    print(address)

def delete():
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")
    cur = con.cursor()

    cur.execute("DELETE FROM add_supplier WHERE supplier_id="+supplierid_entry.get())
    con.commit()
    messagebox.showinfo('Success', "Record Deleted Successfully")
    screen.destroy()



def a_supplier():
    global con ,cur ,table,supplierid_entry,sname_entry,mo_no_entry,adharno_entry,address_entry,screen
    screen = Tk()
    screen.title("Add Supplier")
    screen.geometry("900x550")
    screen.config(bg="lightblue")

    #table name
    table="add_supplier"

    #Add Supplier frame
    addsupplier_frame = Frame(screen,width="600",height="350",bg="Navajo white",bd=8, relief='ridge')
    addsupplier_frame.place(x="150",y="120")

    #Add Supplier frame items
    #labels
    #1
    toy_label = Label(screen,text="TOY SHOP MANAGEMENT SYSTEM",fg="black",bg="lightblue",font=("Times New Roman",20,'underline'))
    toy_label.place(x="0",y="0")
    #2
    addsupplier_label = Label(screen,text="Add New Supplier",fg="black",bg="lightblue",font=("Times New Roman",20))
    addsupplier_label.place(x="350",y="80")
    #3
    supplierid_label = Label(screen,text="Supplier ID:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    supplierid_label.place(x="290",y="150")
    #4
    sname_label = Label(screen,text="Supplier Name:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    sname_label.place(x="290",y="200")
    #5
    mo_no_label = Label(screen,text="Mobile No:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    mo_no_label.place(x="290",y="250")
    #6
    adharno_label = Label(screen,text="Adhar No:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    adharno_label.place(x="290",y="300")
    #7
    address_label = Label(screen,text="Address:",fg="black",bg="Navajo white",font=("Times New Roman",12))
    address_label.place(x="290",y="350")

    #Entry
    #1
    supplierid_entry = Entry(screen,selectforeground="black",font=(12))
    supplierid_entry.place(x="450",y="150")
    #2
    sname_entry = Entry(screen,selectforeground="black",font=(12))
    sname_entry.place(x="450",y="200")
    #3
    mo_no_entry = Entry(screen,selectforeground="black",font=(12))
    mo_no_entry.place(x="450",y="250")
    #4
    adharno_entry = Entry(screen,selectforeground="black",font=(12))
    adharno_entry.place(x="450",y="300")
    #5
    address_entry = Entry(screen,selectforeground="black",font=(12))
    address_entry.place(x="450",y="350")

    #Buttons
    #1
    SubmitBtn = Button(screen, text="SUBMIT", font=( 'arial', 14, 'bold'), width=10, command=add_sup)
    SubmitBtn.place(x=170, y=400, relwidth=0.18, relheight=0.08)

    deleteBtn = Button(screen, text="DELETE", font=('arial', 14, 'bold'), width=10, command=delete)
    deleteBtn.place(x=370, y=400, relwidth=0.18, relheight=0.08)
    # 2
    quitBtn = Button(screen, text="Quit",font=( 'arial', 14, 'bold'), width=10, command=screen.destroy)
    quitBtn.place(x=570, y=400, relwidth=0.18, relheight=0.08)

    screen.mainloop()
