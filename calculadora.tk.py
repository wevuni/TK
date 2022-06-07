from struct import pack
from tkinter import *
#back-end
def somar():
    lb1['text'] = (int(in1.get())+int(in2.get()))

    
#window
janela= Tk()
#widgets
lb1= Label(janela, text='Calculadora!', font='Arial 26')
in1= Entry()
in2= Entry()
bt1= Button(janela, text='Somar', font='Arial 26', command=somar)

#layout
lb1.pack()
in1.pack()
in2.pack()
bt1.pack()
#run
janela.mainloop()