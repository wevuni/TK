from tkinter import *
#back-end
def somar():
    lb1['text']=lb1['text']+1
def subt():
     lb1['text']=lb1['text']-1
#criar a janela
root = Tk()
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)

#criar os widgets

bt1=Button(root, text='-',command=subt)
bt2=Button(root, text='+', command=somar)
lb1=Label(root, text=0)

#organizar os widgets
bt1.grid(row=0, column=0, sticky=NSEW)
bt2.grid(row=0, column=2, sticky=NSEW)
lb1.grid(row=0, column=1, sticky=NSEW)

#run
root.mainloop()