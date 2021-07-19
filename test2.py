from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import db
import dbtest
import sqlite3
from tkinter import messagebox

def display():

    root=Tk()
    root.geometry("1000x600")
    txt1 = Label(root, text="Enter The Image ID", fg='black', font=("Helvetica", 18))
    txt1.place(x=100, y=200)
    txt1.configure(background='dark olive green')

    passw = StringVar
    pin = Entry(root, textvariable=passw, width=50)
    pin.place(x=420, y=205)

    log_btn = Button(root, text="SUBMIT", fg='black', command=lambda: connect(pin.get()))
    log_btn.place(x=300, y=260)
    log_btn.config(height=5, width=50, background='green')

    log_btn = Button(root, text="EXIT", fg='black', command=root.destroy)
    log_btn.place(x=795, y=500)
    log_btn.config(height=3, width=20, background='red')

    root.mainloop()

def connect(pin):

    with sqlite3.connect("digiVault.db") as dbtest:
        cursor = dbtest.cursor()
    find_user = "SELECT * FROM img_path WHERE img_id ='"+pin+"'"
    cursor.execute(find_user)
    results = cursor.fetchall()

    #print(results[0])
    if results[0][1] == pin:
        print('hi')
        pin=results
        a=(results[0][0])
    picdisplay(a)

def picdisplay(results):
    im =Image.open(results)
    im.show()




def addfile():

    class Window(Frame):
        x=filedialog.askopenfile().name
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            self.pack(fill=BOTH, expand=1)

            load = Image.open(self.x)
            load = load.resize((250, 250), Image.ANTIALIAS)

            render = ImageTk.PhotoImage(load,master=master)

            img = Label(self, image=render)

            img.image = render

            img.place(x=0, y=0)
            mypass = Label(self, text='Enter the image ID')
            mypass.place(x=0,y=280)

            password = Entry(self, width=50)
            password.place(x=0, y=300)

            mypassButton = Button(self, text=" SUBMIT ", fg="black", bg="yellow",
                                  command=lambda: dbtest.adding(Window.x, password.get()))
            mypassButton.place(x=50, y=350)

    root = Tk()
    app = Window(root)
    root.wm_title("Image_Display")
    root.geometry("500x500")
    root.mainloop()

    #root.mainloop()

def addfiles():
     root = Tk()
     root.geometry("1000x600")
     root.title("DigiVault")

     head = Label(root, text="WELCOME to the DigiVault :)", fg='black', font=("Helvetica", 22, "bold"))
     head.place(x=280, y=45)
     head.configure(background='dark olive green')

     btn2 = Button(root, text="OPEN IMAGE", fg='black', command=addfile)
     btn2.place(x=280, y=150)
     btn2.config(height=5, width=50, background='green')

     log_btn = Button(root, text="EXIT", fg='black', command=root.destroy)
     log_btn.place(x=795, y=500)
     log_btn.config(height=3, width=20, background='red')

     root.mainloop()

def editanddisplay():
    root = Tk()
    root.geometry("1000x600")

    head = Label(root, text="WELCOME to the DigiVault :)", fg='black', font=("Helvetica", 36, "bold"))
    head.place(x=180, y=45)
    head.configure(background='dark olive green')

    log_btn = Button(root, text="DISPLAY FILES", fg='black', command=display)
    log_btn.place(x=300, y=200)
    log_btn.config(height=5, width=50, background='yellow')

    log_btn2 = Button(root, text="ADD FILES", fg='black', command=addfiles)
    log_btn2.place(x=300, y=300)
    log_btn2.config(height=5, width=50, background='green')

    log_btn = Button(root, text="EXIT", fg='black', command=root.destroy)
    log_btn.place(x=795, y=500)
    log_btn.config(height=3, width=20, background='red')

    root.mainloop()

def match(username,password):
    print(username,password)

    with sqlite3.connect("digiVault.db") as db:
        cursor = db.cursor()
    find_user = "SELECT * FROM user WHERE username ='"+username+"' and password ='"+password+"'"
    cursor.execute(find_user)

    results =cursor.fetchall()

    print(results[0][3])
    print(results[0][5])
    if results[0][3]==username and results[0][5]==password:
        #username,password = results
        messagebox.showinfo("DigiVault", "LOGIN SUCCESSFUL")
        editanddisplay()
    else:
        messagebox.showinfo("DigiVault", "LOGIN UNSUCCESSFUL")
    #editanddisplay()


def login():
    root = Tk()
    root.geometry("1000x600")

    head = Label(root, text="LOGIN Page", fg='black', font=("Helvetica", 36, "bold"))
    head.place(x=300, y=45)
    head.configure(background='dark olive green')

    txt1 = Label(root, text="Enter your Username", fg='white', font=("Helvetica", 18))
    txt1.place(x=100, y=150)
    txt1.configure(background='dark olive green')

    u_name = StringVar
    username = Entry(root, textvariable=u_name, width=50)
    username.place(x=420, y=155)

    txt1 = Label(root, text="Enter your Password", fg='white', font=("Helvetica", 18))
    txt1.place(x=100, y=200)
    txt1.configure(background='dark olive green')

    passw = StringVar
    password = Entry(root,show="*",textvariable=passw, width=50)
    password.place(x=420, y=205)

    log_btn = Button(root, text="SUBMIT", fg='black', command=lambda: match(username.get(),password.get()))
    log_btn.place(x=250, y=300)
    log_btn.config(height=5, width=50, background='green')

    log_btn = Button(root, text="EXIT", fg='black', command=root.destroy)
    log_btn.place(x=795, y=500)
    log_btn.config(height=3, width=20, background='red')

    root.mainloop()

def signup():
    root = Tk()
    root.geometry("1000x600")
    head = Label(root, text="Sign-up Page", fg='black', font=("Helvetica", 36, "bold"))
    head.place(x=400, y=45)
    head.configure(background='dark olive green')

    txt1 = Label(root, text="Enter your Name", fg='white', font=("Helvetica", 18))
    txt1.place(x=100, y=150)
    txt1.configure(background='dark olive green')

    name=StringVar
    path1 = Entry(root, textvariable=name, width=50)
    path1.place(x=420, y=155)

    txt2 = Label(root, text="Enter your Age", fg='white', font=("Helvetica", 18))
    txt2.place(x=100, y=200)
    txt2.configure(background='dark olive green')

    age = StringVar
    path2 = Entry(root, textvariable=age, width=50)
    path2.place(x=420, y=205)

    txt3 = Label(root, text="Enter your Date of ur Birth", fg='white', font=("Helvetica", 18))
    txt3.place(x=100, y=250)
    txt3.configure(background='dark olive green')

    dob = StringVar
    path3 = Entry(root, textvariable=dob, width=50)
    path3.place(x=420, y=255)

    txt4 = Label(root, text="Enter your Username", fg='white', font=("Helvetica", 18))
    txt4.place(x=100, y=300)
    txt4.configure(background='dark olive green')

    u_name = StringVar
    path4 = Entry(root, textvariable=u_name, width=50)
    path4.place(x=420, y=305)

    txt5 = Label(root, text="Enter your Email", fg='white', font=("Helvetica", 18))
    txt5.place(x=100, y=350)
    txt5.configure(background='dark olive green')

    email = StringVar
    path5 = Entry(root, textvariable=email, width=50)
    path5.place(x=420, y=355)

    txt6 = Label(root, text="Enter the password", fg='white', font=("Helvetica", 18))
    txt6.place(x=100, y=400)
    txt6.configure(background='dark olive green')

    passw = StringVar
    path6 = Entry(root, textvariable=passw, width=50)
    path6.place(x=420, y=405)

    button1 = Button(root, text="SUBMIT", fg='black', command=lambda: db.add(path1.get(),path2.get(),path3.get(),path4.get(),path5.get(),path6.get()))
    button1.place(x=250, y=460)
    button1.config(height=5, width=50, background='yellow')

    log_btn = Button(root, text="EXIT", fg='black', command=root.destroy)
    log_btn.place(x=795, y=500)
    log_btn.config(height=3, width=20, background='red')

    root.mainloop()



root=Tk()
root.geometry("1000x600")

head = Label(root, text="WELCOME TO DigiVault", fg='black', font=("Helvetica", 36, "bold"))
head.place(x=200, y=45)
head.configure(background='dark olive green')


log_btn = Button(root, text="LOGIN", fg='black',command=login)
log_btn.place(x=300, y=200)
log_btn.config(height=5, width=50, background='yellow')

log_btn = Button(root, text="SIGNUP", fg='black',command=signup)
log_btn.place(x=300, y=300)
log_btn.config(height=5, width=50, background='green')

log_btn = Button(root, text="EXIT", fg='black',command=root.destroy)
log_btn.place(x=795, y=500)
log_btn.config(height=3, width=20, background='red')

root.mainloop()
