from tkinter import *
 
from tkinter import messagebox
pencere = Tk()
 
pencere.title(1)
pencere.geometry("320x175")
 
# grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()
 
L1 = Label(uygulama, text="İfade Girin")
L1.grid(padx="110", pady=10)
 
E1 = Entry(uygulama, bd=2)
E1.grid(padx=100, pady=3)
 
# formu çiz
pencere.mainloop()

