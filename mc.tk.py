from tkinter import *
#window
mc=Tk()
fr1=Frame(mc)
fr2=Frame(mc)
mc.grid_rowconfigure(0, weight=3)
mc.grid_columnconfigure(0, weight=3)
def somar():
    r=(float(in2.get())) / ((float(in1.get()))*(float(in1.get())))

    if r < 18.5:
        lb4['text']='Peso Baixo'
    if r >18.5 and r<24.9:
        lb4['text']='Peso Normal'
    if r >24.9 and r<29.9:
        lb4['text']='Sobrepeso'
    if r >30.0 and r<35.0:
        lb4['text']='Obesidade 1'
    if r >35.0 and r<40.0:
        lb4['text']='Obesidade 2'
    if r >=40.0:
        lb4['text']='Obesidade 3'
#widgets
lb1= Label(fr1, text='Cálculo MC', font='Arial 20')
lb2= Label(fr1, text='Altura', font='Arial 20')
lb3= Label(fr1, text='Peso', font='Arial 20')
lb4= Label(fr2, text='Status', font='Arial 20')
in1=Entry(fr1)
in2=Entry(fr1)
bt1= Button(fr2, text='Calcular', font='Arial 20', command=somar)
fr1.pack()
fr2.pack()

#layout
lb1.grid(row=0, column=0, sticky=EW)
lb2.grid(row=1, column=0, sticky=NSEW)
in1.grid(row=2, column=0, sticky=NSEW)
lb3.grid(row=3, column=0, sticky=NSEW)
in2.grid(row=4, column=0, sticky=NSEW)
bt1.grid(row=5, column=0, sticky=NSEW)
lb4.grid(row=6, column=0, sticky=NSEW)

#run 
Tk=mainloop()