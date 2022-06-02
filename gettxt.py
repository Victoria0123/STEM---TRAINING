from tkinter import *
root = Tk ()

#create a task function
def myClick():
    My_Label = Label(root,text="Hey you clicked me!")
    My_Label . pack ()
 
#create a frame
My_Button = Button(root, text="click me", command=myClick, fg="#00FFFF", bg="black")

#Pack it--shove it in the window
My_Button.pack()
root.mainloop()