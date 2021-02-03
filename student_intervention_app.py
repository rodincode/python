from tkinter import *
lst=["What's the students age::" ,
     "Is the mother educated::" ,
     "Is the father educated::" ,
     "For how much time does your ward travel::" ,
     "How many hours does your ward study::" ,
     "How many failures::" ,
     "How are the family relations::" ,
     "How much free time does your ward get::" ,
     "How many hours does your ward go out::" ,
     "How much alchohol does the father consume::" ,
     "How much alcohol does the mother consume::" ,
     "How is the ward's health::" ,
     "How many absences::" ,
     "Is the school LPS::" ,
     "Is the school VIVEK::" ,
     "Is the sex Female::" ,
     "Do you live in a rural area::" ,
     "Do you live in an urban area::" ,
     "Are there more then 3 members in your family::" ,
     "Are there less than 3 members in your family::" ,
     "Are the parents apart::" ,
     "Are the parents together::" ,
     "Does your mother stay at home::" ,
     "Does your mother work in health sector" ,
     "Does your mother have a job other than staying at home or healthcare or services or teacher::" ,
     "Does your mother work in service sector::" ,
     "Is your mother a teacher::" ,
     "Does your father stay at home::" ,
     "Does your father work in health sector" ,
     "Does your father have a job other than staying at home or healthcare or services or teacher::" ,
     "Does your father work in service sector::" ,
     "Is your father a teacher::" ,
     "Was there a particular reason of joining this school::" ,
     "Was the reason that the school was near home::" ,
     "Was the reason the school's reputation::" ,
     "Was there some other reason::" ,
     "Is the guardian father::" ,
     "Is the guardian mother::" ,
     "Do you have some other guardian apart from parents::" ,
     "You dont have education support from school::" ,
     "You have educational support from school::" ,
     "The family doesnt support you::" ,
     "The family supports you::" ,
     "Do you take extra classes::" ,
     "Do you don't take extra classes::" ,
     "Do you do extra curricular activities::" ,
     "Do you not take extra curricular activities.::" ,
     "You didnt attend nursery::" ,
     "You attended nursery::" ,
     "You dont want to take higher education::" ,
     "You want to take higher education::" ,
     "You dont have internet access::" ,
     "You have internet access::" ,
     "You are not in a relationship::" ,
     "You are in a relationship::" ]
print(len(lst))
root=Tk()
root.title("Student app")
root.geometry("800x600")
#value of checkpoints
#fix yes/no for some entries
def main_func():
    global lst, var1, var2
    print(var1.get())
    print(var2.get())

def check():
    global lst, var1, var2
    print("Hello", name.get())
    root1=Tk()
    display=Label(root1, text=name.get())
    display.pack()
    f1 = Frame(root1)
    f1.pack(side=LEFT)
    for i in range(27):
        school=Label(f1, text=lst[i])
        school.grid(row=i, column=0)
        var1=IntVar()
        var2=IntVar()
        if ("Is" in lst[i]) or ("Was" in lst[i]) or ("Does" in lst[i]) or ("Do" in lst[i]) or ("Are" in lst[i]):
            check11=Checkbutton(f1, text="yes", variable=var1)
            check11.grid(row=i, column=1)
            check12=Checkbutton(f1, text="no", variable=var2)
            check12.grid(row=i, column=2)
        else:
            value = Entry(f1)
            value.grid(row=i,column = 1)

    f2 = Frame(root1)
    f2.pack(side=RIGHT)
    for i in range(27,55):
        school=Label(f2, text=lst[i])
        school.grid(row=i, column=0)
        var1=IntVar()
        var2=IntVar()
        if ("Is" in lst[i]) or ("Was" in lst[i]):
            check11=Checkbutton(f2, text="yes", variable=var1)
            check11.grid(row=i, column=1)
            check12=Checkbutton(f2, text="no", variable=var2)
            check12.grid(row=i, column=2)
        else:
            value = Entry(f2)
            value.grid(row = i,column = 1)
    button1=Button(f2, text="predict", command=main_func)
    button1.grid(row=i+1, column=1)
    #scroll_bar = Scrollbar(root1,command = root1.yveiw)
 
    #scroll_bar.grid(row=1, column=100)
    #root1.config(yscrollcommand=scroll_bar.set)

    root1.mainloop()
name=Label(root, text="Name", fg="black")
name.pack()
name=Entry(root)
name.pack()
Class=Label(root, text="Class", fg="black")
Class.pack()
Class=Entry(root)
Class.pack()
button=Button(root, text="Submit", command=check)
button.pack()
scroll_bar = Scrollbar(root)
 
scroll_bar.pack( side = RIGHT,
                fill = Y)
root.mainloop()

