import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
import pymysql

user = ""
def prod_to_login(root):
    root.destroy()
    from login_copy import login_call
    login_call()

def prducts_top(frame_prod):
    Frame_login = Frame(frame_prod, bg="orange")
    Frame_login.place(x=0, y=0, width=1600, height=50)

    btn2 = Button(Frame_login, text="Product", cursor="hand2",command=lambda:prod_call(user),
                  font=("times new roman", 10), fg='white', bg='orangered', bd=0, width=15, height=1)
    btn2.place(x=30, y=10)


    btn2 = Button(Frame_login, text=user_name, font=('times new roman', 10), bg='orangered', fg='white', bd=0,
                  width=15, height=1)
    btn2.place(x=1180, y=13)

    btn2 = Button(Frame_login, text="Logout", command=lambda: prod_to_login(root), cursor="hand2",
                  font=("times new roman", 10), fg='white', bg='orangered', bd=0, width=12, height=1)
    btn2.place(x=1400, y=13)

    btn2 = Button(Frame_login, text="Cart", cursor="hand2",command=cart_call,
                  font=("times new roman", 10), fg='white', bg='orangered', bd=0, width=12, height=1)
    btn2.place(x=1300, y=13)


def cart_top(cart_root):
    Frame_login = Frame(cart_root, bg="orange")
    Frame_login.place(x=0, y=0, width=1600, height=50)

    btn2 = Button(Frame_login, text="Product", cursor="hand2",command=lambda:prod_call(user),
                  font=("times new roman", 10), fg='white', bg='orangered', bd=0, width=15, height=1)
    btn2.place(x=30, y=13)
    lb1 = Label(Frame_login, text="Total Price:", font=('times new roman', 12),bg="orange",fg='white', bd=1,
                  width=15, height=1)
    lb1.place(x=1170, y=13)
    data = mycursor.execute('select sum(pprise) from cart where email=%s',(user))
    records = mycursor.fetchall()
    lb22 = Label(Frame_login, text=records[0], font=('times new roman', 12), bg='orangered', fg='white', bd=0,
                  width=10, height=1)
    lb22.place(x=1295, y=13)
    btn2 = Button(Frame_login, text="Logout", command=lambda: prod_to_login(root), cursor="hand2",
                  font=("times new roman", 10), fg='white', bg='orangered', bd=0, width=12, height=1)
    btn2.place(x=1400, y=13)


class DynamicGrid(tk.Frame):
    def __init__(self, parent, *var, **kwargs):
        tk.Frame.__init__(self, parent, *var, **kwargs)
        self.text = tk.Text(self, wrap="char", borderwidth=0, highlightthickness=0,
                            state="disabled")
        self.text.place(height=900, width=1600, x=0, y=40)
        self.boxes = []

    def add_box(self, var, color=None):
        box = tk.Frame(self.text, bd=1, width=492, height=200)
        self.boxes.append(box)
        self.text.configure(state="normal")
        self.text.window_create("end", window=box)
        self.text.configure(state="disabled")
        label1 = tk.Label(box, text="Product Name:", font=('times new roman', 15)
                          , fg='black').place(x=20, y=20)
        label2 = tk.Label(box, text=var[1], font=('times new roman', 15)
                          , fg='black').place(x=230, y=20)
        label3 = tk.Label(box, text="Product description:", font=('times new roman', 15)
                          , fg='black').place(x=20, y=60)
        label4 = tk.Label(box, text=var[3], font=('times new roman', 15)
                          , fg='black').place(x=230, y=60)
        label5 = tk.Label(box, text="Price:", font=('times new roman', 15)
                          , fg='black').place(x=20, y=100)
        label6 = tk.Label(box, text=var[2], font=('times new roman', 15)
                          , fg='black').place(x=230, y=100)
        bt1=tk.Radiobutton(box,variable=rad, value=var[0]).place(x=300, y=150)
        addcart = tk.Button(box, text="Add to cart", font=('times new roman', 15),command=add_cart
                          , fg='black').place(x=340, y=140)
        box = tk.Frame(self.text, bd=5, relief=tk.RAISED, width=10, height=200,)
        self.boxes.append(box)
        self.text.configure(state="normal")
        self.text.window_create("end", window=box)
        self.text.configure(state="disabled")


class Example(object):
    def __init__(self,frame1_root):
       
        self.frame1_root = frame1_root
        self.dg = DynamicGrid(self.frame1_root, width=1000, height=900)

        self.dg.pack(side="top", fill="both", expand=True)
        prducts_top(self.frame1_root)
        # add a few boxes to start
        self.data = mycursor.execute('select * from data')
        self.records = mycursor.fetchall()
        for product in self.records:
            self.dg.add_box(product)

class DynamicGrid1(tk.Frame):
    def __init__(self, parent, *var, **kwargs):
        tk.Frame.__init__(self, parent, *var, **kwargs)
        self.text = tk.Text(self, wrap="char", borderwidth=0, highlightthickness=0,
                            state="disabled")
        self.text.place(height=900, width=1600, x=0, y=40)
        self.boxes = []

    def add_box(self, var, color=None):
        box = tk.Frame(self.text,width=492,bd=5, relief=tk.RAISED, height=200)
        self.boxes.append(box)
        self.text.configure(state="normal")
        self.text.window_create("end", window=box)
        self.text.configure(state="disabled")
        label1 = tk.Label(box, text="Product Name:", font=('times new roman', 15)
                          , fg='black').place(x=20, y=20)
        label2 = tk.Label(box, text=var[2], font=('times new roman', 15)
                          , fg='black').place(x=230, y=20)

        label5 = tk.Label(box, text="Price:", font=('times new roman', 15)
                          , fg='black').place(x=20, y=60)
        label6 = tk.Label(box, text=var[3], font=('times new roman', 15)
                          , fg='black').place(x=230, y=60)
        bt1=tk.Radiobutton(box,variable=del1, value=var[1]).place(x=300, y=150)
        addcart = tk.Button(box, text="Delete Product", font=('times new roman', 15),command=deleteprod
                          , fg='black').place(x=340, y=140)
        box = tk.Frame(self.text, bd=5, relief=tk.RAISED,height=200)
        self.boxes.append(box)
        self.text.configure(state="normal")
        self.text.window_create("end", window=box)
        self.text.configure(state="disabled")


def add_cart():
    data_cart = mycursor.execute('select * from data where id=%s',rad.get())
    records = mycursor.fetchall()
    data_cart = mycursor.execute('insert into cart values(%s,%s,%s,%s)',(user,records[0][0],records[0][1],records[0][2]))
    messagebox.showinfo(title="Success", message=f"Product added successfully into cart")
    mydb.commit()


def deleteprod():
    data = mycursor.execute('delete from cart where pid=%s and email=%s',(del1.get(),user))
    messagebox.showinfo(title="Success", message=f"your product successfully deleted")
    mydb.commit()
    cart_call()


class cart(object):
    def __init__(self,cart_root):
        self.cart_root = cart_root

        self.dg = DynamicGrid1(self.cart_root, width=1000, height=900)

        self.dg.pack(side="top", fill="both", expand=True)
        cart_top(self.cart_root)
        # add a few boxes to start
        self.data = mycursor.execute('select * from cart where email=%s',(user))
        self.records = mycursor.fetchall()
        for product in self.records:
            self.dg.add_box(product)


def prod_call(arg):
    global user
    global user_name
    user = arg
    global mydb, mycursor
    mydb = pymysql.connect(host='localhost', user='root', password='root')
    mycursor = mydb.cursor()
    mycursor.execute('use e_commerce')
    name = mycursor.execute('select firstname from registration_copy where email=%s',user)
    user_name = mycursor.fetchall()
    global pro_frame
    pro_frame = tk.Frame(root)
    pro_frame.place(x=0, y=0, width=1600, height=900)
    global rad
    rad = tk.StringVar()
    rad.set(0)
    Example(pro_frame)
    

def cart_call():
    pro_cart = tk.Frame(root)
    global del1
    del1 = tk.StringVar()
    del1.set(0)
    pro_cart.place(x=0, y=0, width=1600, height=900)
    cart(pro_cart)

def prod_home(arg):
    global root
    root = Tk()
    root.state('zoomed')
    root.title("One-Click Pick")
    prod_call(arg)
    root.mainloop()

if __name__ == '__main__':
    from login_copy import database
    database()
    prod_home(user)
