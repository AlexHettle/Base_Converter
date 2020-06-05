from tkinter import *
#This function takes in a base-10 number and converts it to binary,
#octal, and hexadecimal. Function uses built-in functions to convert.
def convert(deci):
    sign=""
    DecimalLabel.configure(text=("Decimal:",deci))
    if(deci<0):
        deci*=-1
        sign="-"
    BinaryLabel.configure(text=" Binary: "+sign+(bin(deci)[2:]))
    OctalLabel.configure(text="  Octal: "+sign+(oct(deci)[2:]))
    HexLabel.configure(text="    hex: "+sign+(hex(deci)[2:]))
#Used when user inputs an invalid number.
def invalid():
    DecimalLabel.configure(text="Invalid entry, cannot convert")
    BinaryLabel.configure(text="")
    OctalLabel.configure(text="")
    HexLabel.configure(text="")
#used to turn the original number inputted by the user into base 10 form, and
#then run through the convert function.
def descision(Num,Base):
    if Num=="":
        Num="0"
    try:
        #int(num,n) can be used to convert num of base n into a base 10 number
        Num=int(Num,Base)
        convert(Num)
    except:
        invalid()
#These four functions are used depending on what base the original number is.
#It takes in the original number and what base it is and then prepares it to 
#be run through the convert() function
def entrydecimal():
    DecimalNum=The_Entry.get()
    The_Entry.delete(0,END)
    descision(DecimalNum,10)
def entrybinary():
    BinaryNum=The_Entry.get()
    The_Entry.delete(0,END)
    descision(BinaryNum,2)
def entryoctal():
    OctalNum=The_Entry.get()
    The_Entry.delete(0,END)
    descision(OctalNum,8)
def entryhex():
    HexNum=The_Entry.get()
    The_Entry.delete(0,END)
    descision(HexNum,16)
#This chunk of code sets up the GUI
window=Tk()
window.title("Base Converter")
window.geometry("400x220")
window.configure(bg="#98eb7f")
title=Label(text="BASE CONVERTER",font=("fixedsys",30),bg="#98eb7f")
The_Entry=Entry(window,width=20,borderwidth=10)
The_Entry.place(x=120,y=60)
title.pack(side=TOP)
DecimalButton=Button(window,text="Decimal",padx=10,pady=7,bg="#92d7b9",font=("fixedsys",5),command=entrydecimal)
DecimalButton.place(x=35,y=60)
BinaryButton=Button(window,text="Binary",padx=14,pady=7,bg="#92d7b9",font=("fixedsys",5),command=entrybinary)
BinaryButton.place(x=35,y=100)
OctalButton=Button(window,text="Octal",padx=18,pady=7,bg="#92d7b9",font=("fixedsys",5),command=entryoctal)
OctalButton.place(x=35,y=140)
HexButton=Button(window,text="Hex",padx=26,pady=7,bg="#92d7b9",font=("fixedsys",5),command=entryhex)
HexButton.place(x=35,y=180)
DecimalLabel=Label(text="",font=("fixedsys",5),bg="#98eb7f")
DecimalLabel.place(x=160,y=105)
BinaryLabel=Label(text="",font=("fixedsys",5),bg="#98eb7f")
BinaryLabel.place(x=160,y=135)
OctalLabel=Label(text="",font=("fixedsys",5),bg="#98eb7f")
OctalLabel.place(x=160,y=165)
HexLabel=Label(text="",font=("fixedsys",5),bg="#98eb7f")
HexLabel.place(x=160,y=195)
window.mainloop()
