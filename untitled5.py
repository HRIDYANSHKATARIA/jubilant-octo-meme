from tkinter import *
from tkinter import ttk.Combobox

root = Tk()

root.title("Classes")
root.geometry("900x600")

class CreateElements:
    def __init__(self):
        print("init function check")
        
    def createbutton():
        label = Label(root,text="A New Label Is Created Using Class",fg="red")
        label.pack()
        button = Button(root,text="Click Me",command=self.message)
        button.pack(padx=20,pady=10)
        
     def createinput():
         label = Label(root,text="A New Label Is Created Using Class",fg="red")
         label.pack()
         input = Entry(root,text="write something")
         input.pack(padx=20,pady=10)
         
     def createdp():
         label = Label(root,text="A New Label Is Created Using Class",fg="red")
         label.pack()
         drp = ttk.Combobox(root,state="readonly"values="1","2","3","4")
         drp.pack(padx=20,pady=10)
         
    def createnewelements(self):
       if(element == "Input"):
           createinput()
       elif(element == "Button"):
           createbutton()
       elif(element == "Combobox"):
           createdp()
       
           
        
    def message(self):
        messagebox.showinfo("Show Info","You clicked the button created using class")
        
obj_CreateElements = CreateElements()

dropdown = ttk.Combobox(root,state="readonly"values="Input","Button","Combobox")
dropdown.pack()

btn = Button(root,text="clck to elementS dynamically",command=obj_CreateElements.createnewelements) 
btn.pack(padx=20,pady=10) 

element = dropdown.get()

root.mainloop()
