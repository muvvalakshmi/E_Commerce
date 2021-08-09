from tkinter import *
# from PIL import ImageTk
from tkinter import messagebox
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("One-Click Pick Login")
        self.root.geometry("500x600")
        self.root.state("zoomed")
        self.root.resizable(True, True)
        self.loginform()


    def loginform(self):

        Frame_login = Frame(self.root, bg="light grey")
        Frame_login.place(x=0, y=0, height=1366, width=1600)

        # self.img=ImageTk.PhotoImage(file="background.jpg")
        # img=Label(Frame_login,image=self.img).place(x=0,y=0)#width=1366,height=700

        mainlab = Label(Frame_login, text="One-Click Pick", font=("Goudy old style", 25)
                       , fg="black", bg='light grey')
        mainlab.place(x=670, y=80)

        frame_input = Frame(self.root, bd=5,relief=RAISED,bg="white")
        frame_input.place(x=620, y=160, width=330, height=450)

        lebel1 = Label(frame_input, text="Login", font=('times new roman', 20), fg="black"
                       , bg='white')
        lebel1.place(x=30, y=5)

        lebel2 = Label(frame_input, text="Email", font=("Goudy old style", 15)
                       , fg="black", bg='white')
        lebel2.place(x=30, y=60)

        self.email_txt = Entry(frame_input, font=("times new roman", 15), bg='white')
        self.email_txt.place(x=30, y=95, width=270, height=35)

        lebel3 = Label(frame_input, text="Password", font=("Goudy old style", 15)
                       , fg="black", bg='white')
        lebel3.place(x=30, y=140)

        self.password = Entry(frame_input, font=("times new roman", 15), show='*', bg='white')
        self.password.place(x=30, y=175, width=270, height=35)

        btn1 = Button(frame_input, text="Forgot password?", command=lambda: login_to_forgot(self.root), cursor='hand2',
                      font=('calibri', 10)
                      , bg='orange', fg='black', bd=1)
        btn1.place(x=110, y=230)
        
        btn2 = Button(frame_input, text="Login", command=self.login, cursor='hand2',
                      font=("times new roman", 14), bg="orangered", fg="black", bd=1, width=24, height=1)
        btn2.place(x=40, y=270)
        lebel4 = Label(frame_input, text="*** New to One-Click Pick ? ***",
                       font=("times new roman", 12), fg="black", bg='lightgrey', width=30)
        lebel4.place(x=27, y=335)

        btn3 = Button(frame_input, text="New User Registration", command=lambda :login_to_reg(self.root),
                      cursor="hand2", font=('times new roman', 14), bg='orangered', fg='black', bd=1, width=24,
                      height=1)
        btn3.place(x=40, y=390)

    def login(self):
        if self.email_txt.get() == "" or self.password.get() == "":
            messagebox.showerror("error", "all fields are required", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='root',
                                      database='e_commerce')
                cur = con.cursor()
                x = cur.execute('select * from registration_copy where email=%s and password=%s',
                            (self.email_txt.get(), self.password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('error', 'Invalid Username and Password', parent=self.root)
                    self.loginclear()
                    self.email_txt.focus()
                else:
                    if self.email_txt.get() == "admin@gmail.com":
                        login_to_admin(self.root)
                    else:
                        global login_user
                        login_user = self.email_txt.get()
                        login_to_home(self.root)
                        con.close()
            except Exception as es:
                messagebox.showerror('error', f'Error Due to : {str(es)}', parent=self.root)


    def regclear(self):
        self.entry.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)

    def loginclear(self):
        self.email_txt.delete(0, END)
        self.password.delete(0, END)


def login_to_home(root):
    root.destroy()
    from product_page import prod_home
    prod_home(login_user)


def login_to_reg(root):
    root.destroy()
    from register_copy import reg_call
    reg_call()


def login_to_forgot(root):
    root.destroy()
    from forgot_password import forgot_call
    forgot_call()


def login_to_admin(root):
    root.destroy()
    from admin_page import admin_call
    admin_call()
    

def login_call():
    root = Tk()
    ob = Login(root)
    root.mainloop()


def database():
    global mydb, mycursor
    mydb = pymysql.connect(host='localhost', user='root', password='root')
    mycursor = mydb.cursor()
    mycursor.execute('create database if not exists e_commerce')

    mycursor.execute('use e_commerce')
    mycursor.execute("create table if not exists Registration_copy (FirstName varchar(50), LastName varchar(50),"
                     " Password varchar(20), Email varchar(50), Mobile bigint(20))")
    mycursor.execute('create table if not exists data(id INT,name VARCHAR(100),phone FLOAT(9,2),descr VARCHAR(100))')
    mycursor.execute("create table if not exists cart (Email varchar(30), pid int(5),"
                           "pname varchar(100),pprise float(10,2))")
    sql = "insert into registration_copy values (%s,%s,%s,%s,%s)"
    value = ("admin", "admin", "admin123", "admin@gmail.com", "9999999999")
    mycursor.execute(sql, value)
    mydb.commit()


if __name__ == '__main__':
    database()
    login_call()
