from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector
from mysql.connector import Error
import os
import sys
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('Add Book')
        self.canvas = Canvas(self,width=500, height=500)
        self.img = ImageTk.PhotoImage(Image.open("res/add book.png"))
        self.canvas.create_image(0, 0,anchor=NW, image=self.img)
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        #verifying Input
        def b_q():
            if len(b.get()) == 0 or len(c.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                g = 'YES'
                try:
                    self.conn = mysql.connector.connect(host='localhost',port ="3306",
                                                   database='library',
                                                   user='root',
                                                   password='tuan30092001')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into book(name,author,availability) values (%s,%s,%s)",[b.get(),c.get(),g])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another book?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Books.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Error","Check The Details")
        #creating input box and label
        Label(self, text='').pack()
        Label(self, text='Book Details:',bg='#3888FF',fg='black',font=('Courier new', 20, 'bold')).place(x=150, y=70)
        Label(self, text='').pack()
        Label(self, text='Book Name:',bg='#B3FFDB',fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=b, width=30).place(x=170, y=182)
        Label(self, text='Book Author:',bg='#B3FFDB',fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=c, width=30).place(x=170, y=232)
        Button(self, text="Submit",bg='#3333FF', command=b_q).place(x=245, y=300)
Add().mainloop()