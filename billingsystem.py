from tkinter import *
import time
import random
import tkinter.messagebox

root =Tk()
root.geometry("1400x750+0+0")
root.title(" BisKIRAN Restaurant KTM ")
root.configure(background='Black')

Tops = Frame(root, bg='dark Red', bd=25, pady=20, relief=GROOVE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 30, 'bold'), text='BisKIRAN Restaurant KTM ', bd=15, bg='sky blue',
                fg='dark blue', justify=CENTER)
lblTitle.grid(row=0)



ReceiptCal_Function = Frame(root, bg='dark blue', bd=10, relief=GROOVE)
ReceiptCal_Function.pack(side=LEFT)

Buttons_Function = Frame(ReceiptCal_Function, bg='dark Red', bd=3, relief=GROOVE)
Buttons_Function.pack(side=TOP)

Calculator_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=6, relief=GROOVE)
Calculator_Function.pack(side=BOTTOM)

Receipt_Function = Frame(ReceiptCal_Function, bg='dark blue', bd=4, relief=GROOVE)
Receipt_Function.pack(side=BOTTOM)

MenuFrame = Frame(root, bg='dark blue', bd=32, relief=GROOVE)
MenuFrame.pack(side=RIGHT)
Total_Function = Frame(MenuFrame, bg='sky blue', bd=4)
Total_Function.pack(side=BOTTOM)
Drinks_Function = Frame(MenuFrame,bg='sky blue',bd=4)
Drinks_Function.pack(side=TOP)


Drinks_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Drinks_Function.pack(side=LEFT)
Food_Function = Frame(MenuFrame, bg='sky blue', bd=4, relief=GROOVE)
Food_Function.pack(side=RIGHT)
# variables

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()
variable10 = IntVar()
variable11 = IntVar()
variable12 = IntVar()
variable13 = IntVar()
variable14 = IntVar()
variable15 = IntVar()
variable16 = IntVar()

Date_of_Order = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Total_of_Food = StringVar()
Total_of_Drinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

cocktail = StringVar()
iced_tea = StringVar()
hot_chocolate = StringVar()
orange_juice = StringVar()
milkshake = StringVar()
mountain_dew = StringVar()
sting = StringVar()
cobra = StringVar()

fried_chicken = StringVar()
kare_kare = StringVar()
crispy_pata = StringVar()
sinigang_baboy = StringVar()
sinigang_hipon = StringVar()
bicol_express = StringVar()
asparagus_tofu = StringVar()
chicken_sisig = StringVar()

cocktail.set("0")
iced_tea.set("0")
hot_chocolate.set("0")
orange_juice.set("0")
milkshake.set("0")
mountain_dew.set("0")
sting.set("0")
cobra.set("0")

fried_chicken.set("0")
kare_kare.set("0")
crispy_pata.set("0")
sinigang_baboy.set("0")
sinigang_hipon.set("0")
bicol_express.set("0")
asparagus_tofu.set("0")
chicken_sisig.set("0")