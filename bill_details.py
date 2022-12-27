from tkinter import *
#from tkcalendar import DateEntry
import mysql.connector
from tkinter import messagebox


mydb=mysql.connector.connect(host="localhost",user="root",password="root",database='mydb')

mycursor=mydb.cursor()
mydb.commit()

Table = "bill"

def bill_d():
    screen = Tk()
    screen.title("Bill Details")
    screen.geometry("900x550")
    screen.config(bg="lightblue")
    Canvas1 = Canvas(screen)
    Canvas1.config(bg="lightblue")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(screen, bg="orange", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Bill Details", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(screen, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-15s%-20s%-20s%-20s%-20s%-20s%-20s%-15s" % ('Cust_ID', 'Cust_Name', 'MO_No','Prod_Name', 'Date','Price','Quantity','Total'), bg='black',
          fg='white').place(
        relx=0.07, rely=0.1)
    Label(labelFrame,
          text="----------------------------------------------------------------------------------------------------------------------------------",
          bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from bill"
    val = (Table)
    try:
        mycursor.execute(getBooks)
        myresult = mycursor.fetchall()
        mydb.commit()
        for i in myresult:
            Label(labelFrame, text="%-15s%-30s%-20s%-25s%-20s%-20s%-25s%-20s" % (i[0], i[1], i[2], i[3], i[4],i[5],i[6],i[7],), bg='black',
                  fg='white').place(
                relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(screen, text="Quit", bg='#f7f1e3', fg='black', command=screen.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    screen.mainloop()
