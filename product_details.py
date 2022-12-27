from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb=mysql.connector.connect(host="localhost",user="root",password="root",database='mydb')
mycursor=mydb.cursor()
mydb.commit()

Table = "add_product"

def product_d():
    screen = Tk()
    screen.title("Product Details")
    screen.geometry("900x550")
    screen.config(bg="lightblue")

    Canvas1 = Canvas(screen)
    Canvas1.config(bg="lightblue")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(screen, bg="orange", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Product Details", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(screen, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-15s%-20s%-30s%-20s%-20s%-20s%-20s" % ('Prod_ID', 'Prod_Name', 'Sup_Name', 'Date','Purches_P','Sales_p','Added_stock'), bg='black',
          fg='white').place(
        relx=0.07, rely=0.1)
    Label(labelFrame,
          text="-------------------------------------------------------------------------------------------------------------------------------------",
          bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from add_product "
    val = (Table)
    try:
        mycursor.execute(getBooks)
        myresult = mycursor.fetchall()
        mydb.commit()
        for i in myresult:
            Label(labelFrame, text="%-20s%-30s%-30s%-25s%-24s%-25s%-30s" % (i[0], i[1], i[2], i[3], i[4],i[5],i[6]), bg='black',
                  fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(screen, text="Quit", font=( 'arial', 14, 'bold'), width=10, command=screen.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    screen.mainloop()
