from tkinter import *

root=Tk()
fr1=Frame(root)
fr2=Frame(root)
fr3=Frame(root)

#widgets
#frame 1
lb1=Label(fr1, text='Dados Pessoais', font='Arial 14')
lb2=Label(fr1, text='Nome:', font='Arial 12')
lb3=Label(fr1, text='CPF:', font='Arial 12')
lb4=Label(fr1, text='Telefone:', font='Arial 12')
#frame2
lb5=Label(fr2, text='Endereço:', font='Arial 14')
lb6=Label(fr2, text='Bairro:', font='Arial 12')
lb7=Label(fr2, text='Rua:', font='Arial 12')
lb8=Label(fr2, text='Cidade:', font='Arial 12')
lb9=Label(fr2, text='Nº', font='Arial 12')
#frame 1
in1=Entry(fr1)
in2=Entry(fr1)
in3=Entry(fr1)
#frame 2
in4=Entry(fr2)
in5=Entry(fr2)
in6=Entry(fr2)
in7=Entry(fr2)
#frame 3
bt1=Button(fr3, text='Gravar Dados', font='Arial 12')
bt2=Button(fr3, text='Listar Dados', font='Arial 12')
#layout
fr1.grid(row=0, column=0)
fr2.grid(row=0, column=1)
fr3.grid(row=2, column=0)
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
in1.grid(row=1, column=1)
lb3.grid(row=2, column=0)
in2.grid(row=2, column=1)
lb4.grid(row=3, column=0)
in3.grid(row=3, column=1)
#frame 2
lb5.grid(row=0, column=0)
lb6.grid(row=1, column=0)
in4.grid(row=1, column=1)
lb7.grid(row=2, column=0)
in5.grid(row=2, column=1)
lb8.grid(row=3, column=0)
in6.grid(row=3, column=1)
lb9.grid(row=4, column=0)
in7.grid(row=4, column=1)
#frame 3
bt1.grid(row=0, column=0)
bt2.grid(row=0, column=1)











#run
root.mainloop()