from tkinter import *
root=Tk ()
def myClick():
    myLabel=Label(root, text="Hey you clicked")
    myLabel.pack()
MyB = Button(root, text="Click Me!", command=myClick)    
MyB.pack()
root.mainloop()