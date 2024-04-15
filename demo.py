import bcrypt
from tkinter import *
from tkinter import messagebox

password = b'thisismypassword'
hashed = bcrypt.hashpw(password,bcrypt.gensalt())

def validate_password():
  inputed_password = bytes(password_input.get(), encoding='utf-8')
  hashed_inputed_password = bcrypt.checkpw(inputed_password,hashed)
  if hashed_inputed_password:
    messagebox.showinfo('Information', 'Login successful')
  else:
    messagebox.showerror('Error', 'Invalid password')

root = Tk()

root.geometry('600x400')


password_label = Label(root, text='Enter password')
password_label.grid(row=0,column=0)
password_input = Entry(root)
password_input.grid(row=0, column=1)
button = Button(root, text='Submit', command=validate_password)
button.grid(row=1,column=1)


root.mainloop()
