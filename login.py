from tkinter import *
from tkinter import messagebox

def validation():

    if user_entry.get()=="Toy" and password_entry.get()=="123":
        messagebox.showinfo("Information","Sucessfully Login")
        shifting_form()
    else:
        messagebox.showinfo("Error","Your Password is Incorrect")


def shifting_form():
    screen.destroy()
    import main


# -----GUI
screen = Tk()

# -----Variables
email = StringVar()
password = StringVar()

# -----Screen GUI
screen.geometry("550x350")

screen.config(bg="navajowhite")
screen.title("Login or Registration")

# Login Title
title = Label(text="LOG IN", font=("Algerian", 40, "italic"), pady="5", bg="navajowhite", fg="Black").pack(pady="30")


# login frame widgets
# 1
user_label = Label(width="15", padx="5", pady="5", text="Username :-", bg="navajowhite", fg="black",
                    font=("Times New Roman", 20, 'italic'))
user_label.place(x="0", y="120")
# 2
user_entry = Entry(textvariable=email, width="26", selectbackground="gainsboro", selectforeground="black",
                    font=("Cambria", 15, "italic"))
user_entry.place(x="200", y="130")
# 3
password_label = Label(width="15", padx="5", pady="5", text="Password :-", bg="navajowhite", fg="black",
                       font=("Times New Roman", 20, 'italic'))
password_label.place(x="0", y="180")
# 4
password_entry = Entry(textvariable=password, show="*", width="29", selectbackground="gainsboro",
                       selectforeground="black", font=("Calibri", 15, "italic"))
password_entry.place(x="200", y="190")
# 5
login_btn = Button(text="Log In", width="23", font=("Times New Roman", 18, "italic"), bg="rosybrown", fg="black",
                   command=validation)
login_btn.place(x="140", y="250")

screen.mainloop()
