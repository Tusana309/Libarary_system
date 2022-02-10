from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image #PIL -> Pillow
from mysql.connector import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Remove User")
        self.canvas = Canvas(self,width=1366, height=768)
        self.img = ImageTk.PhotoImage(Image.open("res/rem.png"))
        self.canvas.create_image(0, 0,anchor=NW, image=self.img)

        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',port ="3306",
                                                   database='library',
                                                   user='root',
                                                   password='tuan30092001')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where id = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","User Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error","Something goes wrong")
        Label(self, text = "User Id: ",bg='#B3FFDB',fg='black',font=('Courier new', 15, 'bold')).place(x = 5,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 160,y = 44)
        Button(self, text='Remove', width=15,bg='#3333FF', font=('arial', 10),command = ent).place(x=200, y = 90)



Rem().mainloop()