from tkinter import *
celsius=Tk()
fr1=Frame(celsius)
fr2=Frame(celsius)
#back-end
def convert():
    r=float(in1.get())*1.8+32
    lb3['text']=r
#widgets
lb1=Label(fr1, text='C°', font='Arial 16')
in1=Entry(fr1)
lb2=Label(fr2, text='Fahrenheit', font='Arial 16')
lb3=Label(fr2, text='  -  ', font='Arial 16')
bt1_fr1= Button(fr1, text='Converter', font='Arial 16', command=convert)
fr1.pack()
#layout

#fr1
lb1.grid(row=0, column=0, sticky=NSEW)
in1.grid(row=0,column=1, sticky=NSEW)
bt1_fr1.grid(row=3, column=0, sticky=NSEW)

#fr2
lb2.grid(row=1,column=0, sticky=NSEW)
lb3.grid(row=1, column=1, sticky=NSEW)



#run
celsius.mainloop()