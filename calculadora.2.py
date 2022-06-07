from tkinter import *
#back-end
def entrada(valor):
    lb1['text']+=valor
def resultado():
    x=eval(lb1['text'])
    lb1['text']=x

#window
calc= Tk()

#widgets
lb1=Label(calc, text=' ', font='Arial 26')
bt1=Button(calc, text='1', font='Arial 26', command=lambda: entrada('1'))
bt2=Button(calc, text='2', font='Arial 26', command=lambda: entrada('2'))
bt3=Button(calc, text='3', font='Arial 26', command=lambda: entrada('3'))
bt4=Button(calc, text='4', font='Arial 26', command=lambda: entrada('4'))
bt5=Button(calc, text='5', font='Arial 26', command=lambda: entrada('5'))
bt6=Button(calc, text='6', font='Arial 26', command=lambda: entrada('6'))
bt7=Button(calc, text='7', font='Arial 26', command=lambda: entrada('7'))
bt8=Button(calc, text='8', font='Arial 26', command=lambda: entrada('8'))
bt9=Button(calc, text='9', font='Arial 26', command=lambda: entrada('9'))
bt0=Button(calc, text='0', font='Arial 26', command=lambda: entrada('0'))
bt001=Button(calc, text='+', font='Arial 26', command=lambda: entrada('+'))
bt002=Button(calc, text='-', font='Arial 26', command=lambda: entrada('-'))
bt003=Button(calc, text='/', font='Arial 26', command=lambda: entrada('/'))
bt004=Button(calc, text='*', font='Arial 26', command=lambda: entrada('*'))
bt005=Button(calc, text='.', font='Arial 26', command=lambda: entrada('.'))
bt006=Button(calc, text='=', font='Arial 26', command=lambda: resultado ('='))


#layout
lb1.grid(row=0, column=1, sticky=NSEW)
bt1.grid(row=1, column=0, sticky=NSEW)
bt2.grid(row=1, column=1, sticky=NSEW)
bt3.grid(row=1, column=2, sticky=NSEW)
bt4.grid(row=2, column=0, sticky=NSEW)
bt5.grid(row=2, column=1, sticky=NSEW)
bt6.grid(row=2, column=2, sticky=NSEW)
bt7.grid(row=3, column=0, sticky=NSEW)
bt8.grid(row=3, column=1, sticky=NSEW)
bt9.grid(row=3, column=2, sticky=NSEW)
bt0.grid(row=4, column=1, sticky=NSEW)
bt001.grid(row=1, column=3, sticky=NSEW)
bt002.grid(row=2, column=3, sticky=NSEW)
bt003.grid(row=3, column=3, sticky=NSEW)
bt004.grid(row=4, column=3, sticky=NSEW)
bt005.grid(row=4, column=2,sticky=NSEW)
bt006.grid(row=4, column=0, sticky=NSEW)

#run
calc.mainloop()