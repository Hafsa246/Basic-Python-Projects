from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Height converter (Feet to Metres)")
window.configure(background="black")
window.geometry("500x400")
window.resizable(width=True, height=True)


# working of convert button
def convert():
    value = float(feetbuttonentry.get())
    metre = value * 0.3048
    meterbuttonvalue.set("%.4f" % metre)


# working of clear button 
def clear():
    feetbuttonvalue.set("")
    meterbuttonvalue.set("")


# feet Button
feetbutton = Label(window, text = "Feet", bg="purple", fg="white", width=10, height=2)
feetbutton.grid(column=0, row=0, padx=15, pady=15)

feetbuttonvalue = DoubleVar()
feetbuttonentry = Entry(window, textvariable=feetbuttonvalue, width=20)
feetbuttonentry.grid(column=1, row=0) 
feetbuttonentry.delete(0, 'end')


# meter button 
meterbutton = Label(window, text = "Metre", bg="red", fg="white", width=10, height=2)
meterbutton.grid(column=0, row=1)

meterbuttonvalue = DoubleVar()
meterbuttonentry = Entry(window, textvariable=meterbuttonvalue, width=20)
meterbuttonentry.grid(column=1, row=1, pady=30) 
meterbuttonentry.delete(0, 'end')

# convert button 
convert_btn = Button(window, text="Convert", bg="blue", fg="white", width=15, height=2, command=convert)
convert_btn.grid(column=0, row=3, padx=15)

# clear button 
convert_btn = Button(window, text="Clear", bg="light blue", fg="black", width=15, height=2, command=clear)
convert_btn.grid(column=1, row=3, padx=15)

window.mainloop()