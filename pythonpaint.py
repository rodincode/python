from tkinter import *
from tkinter import ttk, colorchooser
#import PIL
#from PIL import Image, ImageDraw
#https://stackoverflow.com/questions/52146562/python-tkinter-paint-how-to-paint-smoothly-and-save-images-with-a-different
root = Tk()
root.title("PyPaint")


def paint(a):
    global lastx, lasty
    if lastx and lasty:
        cv.create_line(lastx,lasty, a.x, a.y,width = penwidth,smooth = True, capstyle = ROUND)
    lastx,lasty = a.x,a.y

def reset(a):
    lastx = None
    lasty = None

def changeWidth(a):
    penwidth = a

def clear():
    cv.delete(ALL)

def change_bg():
    global color_bg
    color_bg = colorchooser.askcolor(color=color_bg)[1]
    cv['bg'] = color_bg

def change_fg():
    global color_fg
    color_fg = colorchooser.askcolor(color=color_fg)[1]

def widgets():
    controls = Frame(root, padx =5, pady =5)
    Label(controls, text="PenWidth: ").grid(row=0,column=0)
    slider = ttk.Scale(controls, from_ = 5 , to = 100, command=changeWidth)
    slider.set(penwidth)  #NOT WORKING
    slider.grid(row=0,column=1, ipadx=30)
    controls.pack(side=TOP)

penwidth = 4
lastx = None
lasty = None
color_fg = 'black'
color_bg = 'white'
#image = PIL.Image.new('RBG',(640,480),'white')
#draw = ImageDraw.Draw(image)
cv = Canvas(root, width = 600 , height = 400, bg=color_bg)
widgets()
cv.bind('<B1-Motion>',paint)
cv.bind('<ButtonRelease-1>',reset)
cv.pack(fill=BOTH,expand=True)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
colormenu = Menu(menu)
menu.add_cascade(label= "Colors", menu = colormenu)
colormenu.add_command(label="Brush Color",command=change_fg)
colormenu.add_command(label="Background Color", command= change_bg)
optionmenu= Menu(menu)
menu.add_cascade(label= "Controls", menu = optionmenu)
colormenu.add_command(label="Clear Canvas",command=clear)
colormenu.add_command(label="Exit", command= root.destroy)


root.mainloop()