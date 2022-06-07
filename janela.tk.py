from tkinter import *
#back-end
def imprimir():
    lb1['text'] = in1.get()
    print(in1.get())

#window
janela = Tk()

#geometry
janela.geometry('400x300+100+100')
janela.config(bg='black')
janela.minsize(width=100, height=100)
janela.maxsize(width=600, height=600)
#widgets
lb1= Label(janela, text='Olá Mundo!', font='Arial 26')
in1= Entry(janela, font='Arieal 26')
bt1= Button(janela, text='Sair', font='Arial 26', command=quit)
bt2= Button(janela, text='Imprimir', font='Arial 26', command=imprimir)
#layout
lb1.pack()
in1.pack()
bt1.pack()
bt2.pack()

#rum
janela.mainloop()
