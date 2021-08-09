from tkinter import *
import tkinter.messagebox as MessageBox
import pymysql as mysql

con = mysql.connect(host='localhost', user='root', password='root')
cursor = con.cursor()
cursor.execute('use e_commerce')


def admin_to_login(root):
    root.destroy()
    from login_copy import login_call
    login_call()


def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    desc = e_desc.get()
    if (id == "" or name == "" or phone == "" or desc == ""):
        MessageBox.showerror("Insert Status ", "All fields are required")
    else:
        con = mysql.connect(host='localhost', user='root', password='root', database='e_commerce')
        cursor = con.cursor()
        cursor.execute('use e_commerce')
        prod_id_query = "select id from data where id=%s"
        prod_field = id
        prod_exist = cursor.execute(prod_id_query, prod_field)
        if prod_exist:
            MessageBox.showerror("Insert Status ", "ID is already existed")
        else:
            cursor.execute("insert into data values('" + id + "','" + name + "','" + phone + "','" + desc + "')")
            cursor.execute('commit')
            MessageBox.showinfo("Insert Status : ", "Inserted Successfully");
            e_id.delete(0, 'end')
            e_name.delete(0, 'end')
            e_desc.delete(0, 'end')
            e_phone.delete(0, 'end')
            # show()
            con.close();


def delete():
    id = e_id.get()
    if (e_id.get() == ""):
        MessageBox.showerror("Delete status : ", "ID is compulsory for delete")
    else:
        con = mysql.connect(host='localhost', user='root', password='root', database='e_commerce')
        cursor = con.cursor()
        cursor.execute('use e_commerce')
        prod_id_query = "select id from data where id=%s"
        prod_field = id
        prod_exist = cursor.execute(prod_id_query, prod_field)
        if prod_exist:
            cursor.execute("delete from data where id='" + e_id.get() + "'")
            cursor.execute('commit')
            cursor.execute("delete from cart where pid='" + e_id.get() + "'")
            cursor.execute('commit')
            e_id.delete(0, 'end')
            e_name.delete(0, 'end')
            e_desc.delete(0, 'end')
            e_phone.delete(0, 'end')
            MessageBox.showinfo("Delete Status : ", "Deleted Successfully")
            con.close()
        else:
            MessageBox.showerror("Insert Status ", "ID does not exist")


def update():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    desc = e_desc.get()
    if (id == "" or name == "" or phone == ""):
        MessageBox.showerror("Update status : ", "All fields are required")
    else:
        con = mysql.connect(host='localhost', user='root', password='root', database='e_commerce')
        cursor = con.cursor()
        cursor.execute('use e_commerce')
        prod_id_query = "select id from data where id=%s"
        prod_field = id
        prod_exist = cursor.execute(prod_id_query, prod_field)
        if prod_exist:
            cursor.execute(
                "update data set id='" + id + "',name='" + name + "', phone='" + phone + "', descr='" + desc + "' where id='" + id + "'")

            cursor.execute('commit')
            cursor.execute(
                "update cart set pid='" + id + "',pname='" + name + "', pprise='" + phone + "' where pid='" + id + "'")
            cursor.execute('commit')
            e_id.delete(0, 'end')
            e_name.delete(0, 'end')
            e_desc.delete(0, 'end')
            e_phone.delete(0, 'end')
            # show()
            MessageBox.showinfo("Update Status : ", "Updated Successfully")
            con.close()
        else:
            MessageBox.showerror("Insert Status ", "ID does not exist")


def show():
    con = mysql.connect(host='localhost', user='root', password='root', database='e_commerce')
    cursor = con.cursor()
    cursor.execute('use e_commerce')
    cursor.execute("select * from data")
    rows = cursor.fetchall()
    data_list.delete(0, data_list.size())
    for row in rows:
        insertData = str(row[0]) + '         ' + str(row[1]) + '         ' + str(row[2])
        data_list.insert(data_list.size() + 1, insertData)
    con.close()


def admin_page(root):
    root.title('ONCE-CLICK PICK')
    root.geometry('800x500')
    title = Label(root, text='ADMIN PANEL', font=('bold', 25))
    title.place(x=280, y=0)
    id = Label(root, text='Product ID : ', font=('bold', 10))
    id.place(x=20, y=60)
    name = Label(root, text='Product Name : ', font=('bold', 10))
    name.place(x=20, y=120)
    desc = Label(root, text='Product Desc : ', font=('bold', 10))
    desc.place(x=20, y=180)
    phone = Label(root, text='Product Price : ', font=('bold', 10))
    phone.place(x=20, y=240)

    global e_id,e_name,e_phone,e_desc
    e_id = Entry(root, width=35)
    e_id.place(x=150, y=60)
    e_name = Entry(root, width=35)
    e_name.place(x=150, y=120)
    e_desc = Entry(root, width=35)
    e_desc.place(x=150, y=180)
    e_phone = Entry(root, width=35)
    e_phone.place(x=150, y=240)
    insert1 = Button(root, text="Insert", font=('italic', 10), fg="black", bg="orange",width=10, command=lambda: [insert(), show()])
    insert1.place(x=20, y=300)
    delete1 = Button(root, text='Delete', font=('italic', 10), fg="black", bg="orange",width=10, command=lambda: [delete(), show()])
    delete1.place(x=150, y=300)
    update1 = Button(root, text='Update', font=('italic', 10), fg="black", bg="orange",width=10, command=lambda: [update(), show()])
    update1.place(x=280, y=300)
    logout = Button(root, text='LogOut', font=('italic', 10), fg="black", bg="orange",width=10,command=lambda:admin_to_login(root))
    logout.place(x=690, y=10)
    global data_list
    data_list = Listbox(root)
    data_list.place(x=400, y=60, width=380)
    show()


def admin_call():
    root = Tk()
    admin_page(root)
    root.mainloop()


if __name__ == "__main__":
    from login_copy import database
    database()
    admin_call()
