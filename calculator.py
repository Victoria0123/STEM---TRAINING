from tkinter import *
root = Tk ()

#create text field space
e1=Entry(root, width=50, bg="blue", fg="red")
e1.pack()
e1.insert(0, "Enter first no")

#second input
e2=Entry(root, width=50, bg="white", fg="black")
e2.pack()
e2.insert(0, "Enter second no")

#create a task function
def myClick():
    f_no=float(e1.get())
    s_no=float(e2.get())
    sub=f_no-s_no
    add=f_no+s_no
    div=f_no/s_no
    mult=f_no*s_no
   
    Ans=f_no*s_no
    My_Label = Label(root,text=Ans)
    My_Label.pack ()
 
#create a frame
My_Button = Button(root, text="calculate", command=myClick, fg="blue", bg="white")

#Pack it--shoveit in the window
My_Button.pack()
root.mainloop()







