from tkinter import *
from tkinter import messagebox
import os,sys
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date
from PIL import ImageTk,Image #PIL -> Pillow
py = sys.executable

# return book

class ret(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title("Return")
        self.maxsize(420,280)
        self.canvas = Canvas(self,width=500, height=417)
        self.img = ImageTk.PhotoImage(Image.open("res/ret.png"))
        self.canvas.create_image(0, 0,anchor=NW, image=self.img)
        self.canvas.pack(fill = BOTH)
        self.canvas.pack()
        self.cal = 0
        a = StringVar()

        def qui():
            if len(a.get()) == '0':
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',port ="3306",
                                                   database='library',
                                                   user='root',
                                                   password='tuan30092001')
                    self.mycursor = self.conn.cursor()

                    self.mycursor.execute("Select book_id from issue_book where return_date = '' and book_id = %s",[a.get()])
                    temp = self.mycursor.fetchone()
                    if temp:
                        self.mycursor.execute("update book set availability ='YES' where book_id = %s", [a.get()])
                        self.conn.commit()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("update issue_book set return_date = %s where book_id = %s", [idate,a.get()])
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo('Info', 'Succesfully Returned')
                        d = messagebox.askyesno("Confirm", "Return more books?")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'ret.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued")
                except Error:
                    messagebox.showerror("Error","Something Goes Wrong")
        Label(self, text='Return Book',bg='#B3FFDB', fg='red',font=('arial', 35, 'bold')).pack()
        Label(self, text='Enter Book ID', font=('Comic Scan Ms', 15, 'bold')).place(x=20, y=120)
        Entry(self, textvariable=a, width=40).place(x=165, y=124)
        Button(self, text="Return", bg='#3333FF', width=25, command=qui).place(x=180, y=180)
ret().mainloop()