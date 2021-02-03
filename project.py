from tkinter import *
import sqlite3 as sq

root = Tk()
root.geometry("600x400")
root.title("Notes")
root.config(bg="black")
canvas = Canvas(root)
scroll = Scrollbar(root, orient="vertical",command= canvas.yview)
scroll.pack(side=RIGHT,fill=Y)
frame = Frame(canvas,bg="blue")
frame.pack(side=TOP)
canvas.configure(yscrollcommand = scroll.set)
canvas.pack(fill=BOTH,expand = 1)
canvas.create_window((0,0), window = frame, anchor = 'nw')

def on_frame_resize(event= None):
    canvas.configure(scrollregion=canvas.bbox("all"))

root.bind('<Configure>',on_frame_resize)
# for i in range(20):
#     f1 = Frame(frame)
#     label = Label(f1,text="NOTES/REVIEW APP",fg="blue")
#     label.pack(side=TOP)
#     button = Button(f1, text="Add")
#     f1.pack()
#     button.pack()
# root.mainloop()
class Notes:
    def __init__(self,size):
        #self.root = root
        self.f1 = Frame(frame)
        self.f1.pack()
        self.label = Label(self.f1,text="NOTES/REVIEW APP",fg="blue")
        self.label.pack(side=TOP)
        self.button = Button(self.f1, text="Add",command=self.add_frame)
        self.button.pack()
        

    def add_frame(self):
        self.f2= Frame(root)
        self.f2.pack(padx=10, pady=20)
        self.label = Label(self.f2,text="Id: ",fg="blue")
        self.label.grid(row = 0, column= 0)
        self.id = Entry(self.f2)
        self.id.grid(row = 0, column= 1)
        self.label = Label(self.f2,text="Title: ",fg="blue")
        self.label.grid(row =1 , column = 0)
        self.title = Entry(self.f2)
        self.title.grid(row = 1, column = 1)
        self.label = Label(self.f2,text="content: ",fg="blue")
        self.label.grid(row = 2, column = 0)
        self.content = Entry(self.f2)
        self.content.grid(row = 2, column = 1)
        self.button = Button(self.f2, text="Submit",command=self.add_info)
        self.button.grid(row=4, column = 3)
        

    def add_info(self):
        id= self.id.get()
        title = self.title.get()
        content = self.content.get()
        data = sq.connect('myappdata.db')
        c =  data.cursor()
        c.execute("CREATE TABLE info(id integer PRIMARY KEY, title text, content)")
        c.execute("INSERT INTO info(id, title,content) VALUES (?,?,?)",(id,title,content))
        data.commit()
        #data.close()
        

x = Notes(400)



#ananyaj567@gmail.com
#kavyasachdeva05@gmail.com

#------------------------------------------------------------#

#--------------------------------------------------------------#

root.mainloop()

