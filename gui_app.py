from tkinter import *

root = Tk()
root.title("AWESOME APP")
root.geometry("600x300")
root['bg'] = "#abc"
x= Label(root,text="I am Barack Obama")
x.configure(font='Arial',bg="black", foreground="red")
x.pack()
root.mainloop()