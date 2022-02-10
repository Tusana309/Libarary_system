from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image #PIL -> Pillow
import os
import sys
import mysql.connector
from mysql.connector import Error
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add Student')
        self.canvas = Canvas(self,width=500, height=417)
        self.img = ImageTk.PhotoImage(Image.open("res/add student.jpg"))
        self.canvas.create_image(0, 0,anchor=NW, image=self.img)
        self.canvas.pack()
        n = StringVar()
        p = StringVar()
        a = StringVar()
#verifying input
        def asi():
            if len(n.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Name")
            elif len(p.get()) < 1:
                messagebox.showinfo("Oop's","Please Enter Your Phone Number")
            elif len(a.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Address")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',port ="3306",
                                                   database='library',
                                                   user='root',
                                                   password='tuan30092001')
                    self.myCursor = self.conn.cursor()
                    name1 = n.get()
                    pn1 = p.get()
                    add1 = a.get()
                    self.myCursor.execute("Insert into student(name,phone_number,address) values (%s,%s,%s)",[name1,pn1,add1])
                    self.conn.commit()
                    messagebox.showinfo("Done","Student Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another student?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Add_Student.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        Label(self, text='Student Details',bg='#3888FF', fg='white', font=('Courier new', 25, 'bold')).place(x=100, y=20)
        Label(self, text='Name:',bg='#B3FFDB', font=('Courier new', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=n, width=30).place(x=200, y=84)
        Label(self, text='Phone Number:',bg='#B3FFDB', font=('Courier new', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=p, width=30).place(x=200, y=132)
        Label(self, text='Address:',bg='#B3FFDB', font=('Courier new', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=a, width=30).place(x=200, y=182)
        Button(self, text="Submit",bg='#3333FF',width = 15,command=asi).place(x=230, y=220)

Add().mainloop()
