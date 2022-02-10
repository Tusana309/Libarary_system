from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
from PIL import ImageTk,Image #PIL -> Pillow
py=sys.executable


#add user

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500, 400)
        self.minsize(500, 400)
        self.title('Add User')
        self.canvas = Canvas(self,width=500, height=417)
        self.img = ImageTk.PhotoImage(Image.open("res/admin.png"))
        self.canvas.create_image(0, 0,anchor=NW, image=self.img)
        self.canvas.pack(fill = BOTH)
#creating variables Please chech carefully
        u = StringVar()
        n = StringVar()
        p = StringVar()


        def insert():
            try:
                self.conn = mysql.connector.connect(host='localhost',port ="3306",
                                                   database='library',
                                                   user='root',
                                                   password='tuan30092001')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(user,name,password) values (%s,%s,%s)",[u.get(), n.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "User Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another user?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'Reg.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")
#label and input
        Label(self, text='User Details', bg='#3888FF', fg='black', font=('Courier new', 25, 'bold')).place(x=130, y=22)
        Label(self, text='Username:', bg='#B3FFDB', font=('Courier new', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=u, width=30).place(x=200, y=84)
        Label(self, text='Name:', bg='#B3FFDB', font=('Courier new', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=n, width=30).place(x=200, y=132)
        Label(self, text='Password:', bg='#B3FFDB', font=('Courier new', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=p, width=30).place(x=200, y=182)
        Button(self, text="Submit", bg = '#3333FF', width=15, command=insert).place(x=230, y=220)
reg().mainloop()