from tkinter import *
#from PIL import  ImageTk,Image
import sqlite3
from tkinter import messagebox

def p():
    print('HI')
#root = Tk()
#root.geometry("400x400")

# Database

# Create a database or connect to one
conn = sqlite3.connect('digiVault.db')

#Create cursor
c = conn.cursor()
#c.execute("CREATE TABLE img_path(img_file text, img_id text)")
#c.execute("CREATE TABLE file_path(file text)")
#c.execute("CREATE TABLE new_img(pic BLOB)")

#c.execute("INSERT INTO photo VALUES('C:\\Users\\nanug\\ycharmProjects\\pythonProject\\Dubai.JPG')")
#c.execute("SELECT * photo")
c.execute("SELECT * FROM file_path")
conn.commit()
print(c.fetchall())

#c.execute("CREATE TABLE user(name text,age integer,dob text,username text,email text,password text)")
#conn.commit()

c.execute("SELECT * from user")
conn.commit()
print(c.fetchall())
def add(name,age,dob,username,email,password):
    messagebox.showinfo("DigiVault", "LOGIN SUCCESSFUL")

    conn = sqlite3.connect('digiVault.db')

    # Create cursor
    c = conn.cursor()

    #insert into tables
    c.execute("INSERT INTO user VALUES (?,?,?,?,?,?)",(name,age,dob,username,email,password))


    conn.commit()
    conn.close()
#root.mainloop()