
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("300x450")
root.title("Calculator")
#root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="7",  font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)


b = Button(f, text="6",font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="5",font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="4",font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="3", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="1", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)


b = Button(f, text="0", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="/", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text=".",font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)


b = Button(f, text="C", font="lucida 35 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()