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

Date_of_Order.set(time.strftime("%y/%m/%d"))

# Function Declaration

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Total_of_Food.set("")
    Total_of_Drinks.set("")
    ServiceCharge.set("")
    textReceipt.delete("1.0", END)


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

    variable1.set(0)
    variable2.set(0)
    variable3.set(0)
    variable4.set(0)
    variable5.set(0)
    variable6.set(0)
    variable7.set(0)
    variable8 .set(0)
    variable9 .set(0)
    variable10 .set(0)
    variable11 .set(0)
    variable12 .set(0)
    variable13 .set(0)
    variable14 .set(0)
    variable15 .set(0)
    variable16 .set(0)


    textCocktail.configure(state=DISABLED)
    textIcedTea.configure(state=DISABLED)
    textHotChocolate.configure(state=DISABLED)
    textOrangeJuice.configure(state=DISABLED)
    textMilkShake.configure(state=DISABLED)
    textMountainDew.configure(state=DISABLED)
    textSting.configure(state=DISABLED)
    textCobra.configure(state=DISABLED)
    textFriedChicken.configure(state=DISABLED)
    textKareKAre.configure(state=DISABLED)
    textCrispyPata.configure(state=DISABLED)
    textSinigangBaboy.configure(state=DISABLED)
    textSinigangHipon.configure(state=DISABLED)
    textBicolExpress.configure(state=DISABLED)
    textAsparagusTofu.configure(state=DISABLED)
    textChickenSisig.configure(state=DISABLED)

def TotalofUnit():
    Unit1 = float(cocktail.get())
    Unit2 = float(iced_tea.get())
    Unit3 = float(hot_chocolate.get())
    Unit4 = float(orange_juice.get())
    Unit5 = float(milkshake.get())
    Unit6 = float(mountain_dew.get())
    Unit7 = float(sting.get())
    Unit8 = float(cobra.get())

    Unit9 = float(fried_chicken.get())
    Unit10 = float(kare_kare.get())
    Unit11 = float(crispy_pata.get())
    Unit12 = float(sinigang_baboy.get())
    Unit13 = float(sinigang_hipon.get())
    Unit14 = float(bicol_express.get())
    Unit15 = float(asparagus_tofu.get())
    Unit16 = float(chicken_sisig.get())

    Prices_Drinks = (Unit1 * 50) + (Unit2 * 45) + (Unit3 * 60) + (Unit4 * 35) + (Unit5 * 70) + (Unit6 * 40) + (Unit7 * 55) + (Unit8 * 75)

    Prices_Food = (Unit9 * 490) + (Unit10 * 450) + (Unit11 * 350) + (Unit12 * 400) + (Unit13 * 500) + (Unit14 * 250) + (Unit15 * 650) + (Unit16 * 370)



    DrinksPrices = "P" + str('%.2f' % Prices_Drinks)
    FoodsPrices = "P" + str('%.2f' % Prices_Food)
    Total_of_Food.set(FoodsPrices)
    Total_of_Drinks.set(DrinksPrices)
    SC = "P" + str('%.2f' % 1.59)
    ServiceCharge.set(SC)

    Sub_Total_of_Unit = "P" + str('%.2f'%(Prices_Drinks + Prices_Food + 1.59))
    SubTotal.set(Sub_Total_of_Unit)

    Tax = "P" + str('%.2f'%((Prices_Drinks + Prices_Food + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT = ((Prices_Drinks + Prices_Food + 1.59) * 0.15)
    TC = "P" + str('%.2f'%(Prices_Drinks + Prices_Food + 1.59 + TT))
    TotalCost.set(TC)


def drinksCocktail():
    if variable1.get() == 1:
        textCocktail.configure(state=NORMAL)
        textCocktail.focus()
        textCocktail.delete('0', END)
        cocktail.set("")
    elif variable1.get() == 0:
        textCocktail.configure(state=DISABLED)
        cocktail.set("0")

def drinksIceTea():
    if variable2.get() == 1:
        textIcedTea.configure(state=NORMAL)
        textIcedTea.focus()
        textIcedTea.delete('0', END)
        iced_tea.set("")
    elif variable2.get() == 0:
        textIcedTea.configure(state=DISABLED)
        iced_tea.set("0")

def drinksHotChocolate():
    if variable3.get() == 1:
        textHotChocolate.configure(state=NORMAL)
        textHotChocolate.delete('0', END)
        textHotChocolate.focus()
    elif variable3.get() == 0:
        textHotChocolate.configure(state=DISABLED)
        hot_chocolate.set("0")

def drinksOrangeJuice():
    if variable4.get() == 1:
        textOrangeJuice.configure(state=NORMAL)
        textOrangeJuice.delete('0', END)
        textOrangeJuice.focus()
    elif variable4.get() == 0:
        textOrangeJuice.configure(state=DISABLED)
        orange_juice.set("0")

def drinksMilkShake():
    if variable5.get() == 1:
        textMilkShake.configure(state=NORMAL)
        textMilkShake.delete('0', END)
        textMilkShake.focus()
    elif variable5.get() == 0:
        textMilkShake.configure(state=DISABLED)
        milkshake.set("0")

def drinksMountainDew():
    if variable6.get() == 1:
        textMountainDew.configure(state=NORMAL)
        textMountainDew.delete('0', END)
        textMountainDew.focus()
    elif variable6.get() == 0:
        textMountainDew.configure(state=DISABLED)
        mountain_dew.set("0")

def drinksSting():
    if variable7.get() == 1:
        textSting.configure(state=NORMAL)
        textSting.delete('0', END)
        textSting.focus()
    elif variable7.get() == 0:
        textSting.configure(state=DISABLED)
        sting.set("0")

def drinksCobra():
    if variable8.get() == 1:
        textCobra.configure(state=NORMAL)
        textCobra.delete('0', END)
        textCobra.focus()
    elif variable8.get() == 0:
        textCobra.configure(state=DISABLED)
        cobra.set("0")

def foodsFriedChicken():
    if variable9.get() == 1:
        textFriedChicken.configure(state=NORMAL)
        textFriedChicken.delete('0', END)
        textFriedChicken.focus()
    elif variable9.get() == 0:
        textFriedChicken.configure(state=DISABLED)
        fried_chicken.set("0")

def foodsKareKare():
    if variable10.get() == 1:
        textKareKAre.configure(state=NORMAL)
        textKareKAre.delete('0', END)
        textKareKAre.focus()
    elif variable10.get() == 0:
        textKareKAre.configure(state=DISABLED)
        kare_kare.set("0")

def foodsCrispyPata():
    if variable11.get() == 1:
        textCrispyPata.configure(state=NORMAL)
        textCrispyPata.delete('0', END)
        textCrispyPata.focus()
    elif variable11.get() == 0:
        textCrispyPata.configure(state=DISABLED)
        crispy_pata.set("0")

def foodsSinigangBaboy():
    if variable12.get() == 1:
        textSinigangBaboy.configure(state=NORMAL)
        textSinigangBaboy.delete('0', END)
        textSinigangBaboy.focus()
    elif variable12.get() == 0:
        textSinigangBaboy.configure(state=DISABLED)
        sinigang_baboy.set("0")

def foodsSinigangHipon():
    if variable13 .get() == 1:
        textSinigangHipon.configure(state=NORMAL)
        textSinigangHipon.delete('0',END)
        textSinigangHipon.focus()
    elif(variable13.get() == 0):
        textSinigangHipon.configure(state=DISABLED)
        sinigang_hipon.set("0")

def foodsBicolExpress():
    if variable14 .get() == 1:
        textBicolExpress.configure(state=NORMAL)
        textBicolExpress.delete('0', END)
        textBicolExpress.focus()
    elif variable14.get() == 0:
        textBicolExpress.configure(state=DISABLED)
        bicol_express.set("0")

def foodsAsparagusTofu():
    if variable15.get() == 1:
        textAsparagusTofu.configure(state=NORMAL)
        textAsparagusTofu.delete('0', END)
        textAsparagusTofu.focus()
    elif variable15.get() == 0:
        textAsparagusTofu.configure(state=DISABLED)
        asparagus_tofu.set("0")

def foodsChickenSisig():
    if variable16 .get() == 1:
        textChickenSisig.configure(state=NORMAL)
        textChickenSisig.delete('0',END)
        textChickenSisig.focus()
    elif(variable16.get() == 0):
        textChickenSisig.configure(state=DISABLED)
        chicken_sisig.set("0")

def Receipt():
    textReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)


    textReceipt.insert(END, 'Receipt Ref:\t\t\t'+Receipt_Ref.get() + '\t' + Date_of_Order.get() + '\n')
    textReceipt.insert(END, 'Unit\t\t\t\t'+"Total of Unit \n")
    textReceipt.insert(END, 'Cocktail:\t\t\t\t\t' + cocktail.get() + '\n')
    textReceipt.insert(END, 'Iced Tea:\t\t\t\t\t' + iced_tea.get()+'\n')
    textReceipt.insert(END, 'Hot Chocolate:\t\t\t\t\t' + hot_chocolate.get()+'\n')
    textReceipt.insert(END, 'Orange Juice:\t\t\t\t\t' + orange_juice.get()+'\n')
    textReceipt.insert(END, 'Milk Shake:\t\t\t\t\t' + milkshake.get()+'\n')
    textReceipt.insert(END, 'Mountain Dew:\t\t\t\t\t' + mountain_dew.get()+'\n')
    textReceipt.insert(END, 'Sting:\t\t\t\t\t' + sting.get()+'\n')
    textReceipt.insert(END, 'Cobra:\t\t\t\t\t' + cobra.get()+'\n')
    textReceipt.insert(END, 'Fried Chicken:\t\t\t\t\t' + fried_chicken.get()+'\n')
    textReceipt.insert(END, 'Kare Kare:\t\t\t\t\t' + kare_kare.get()+'\n')
    textReceipt.insert(END, 'Crispy Pata:\t\t\t\t\t' + crispy_pata.get()+'\n')
    textReceipt.insert(END, 'Sinigang baboy:\t\t\t\t\t' + sinigang_baboy.get()+'\n')
    textReceipt.insert(END, 'Sinigang Hipon:\t\t\t\t\t' + sinigang_hipon.get()+'\n')
    textReceipt.insert(END, 'Bicol Express:\t\t\t\t\t' + bicol_express.get()+'\n')
    textReceipt.insert(END, 'Asparagus Tofu:\t\t\t\t\t' + asparagus_tofu.get()+'\n')
    textReceipt.insert(END, 'Chicken Sisig:\t\t\t\t\t' + chicken_sisig.get()+'\n')
    textReceipt.insert(END, 'Total of Drinks:\t\t\t\t' + Total_of_Drinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    textReceipt.insert(END, 'Total of Foods:\t\t\t\t' + Total_of_Food.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    textReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


# Drinks
Cocktail = Checkbutton(Drinks_Function, text='Cocktail', variable=variable1, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksCocktail).grid(row=0, sticky=W)
IcedTea = Checkbutton(Drinks_Function, text='Iced Tea', variable=variable2, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksIceTea).grid(row=1, sticky=W)
HotChocolate = Checkbutton(Drinks_Function, text='Hot Chocolate', variable=variable3, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksHotChocolate).grid(row=2, sticky=W)
OrangeJuice = Checkbutton(Drinks_Function, text='Orange Juice', variable=variable4, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksOrangeJuice).grid(row=3, sticky=W)
MilkShake = Checkbutton(Drinks_Function, text='Milk Shake', variable=variable5, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksMilkShake).grid(row=4, sticky=W)
MountainDew = Checkbutton(Drinks_Function, text='Mountain Dew', variable=variable6, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksMountainDew).grid(row=5, sticky=W)
Sting = Checkbutton(Drinks_Function, text='Sting', variable=variable7, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='sky blue', command=drinksSting).grid(row=6, sticky=W)
Cobra = Checkbutton(Drinks_Function, text='Cobra', variable=variable8, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
bg='sky blue', command=drinksCobra).grid(row=7, sticky=W)
# Drink Entry

textCocktail = Entry(Drinks_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=cocktail)
textCocktail.grid(row=0,column=1)

textIcedTea = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=iced_tea)
textIcedTea.grid(row=1,column=1)

textHotChocolate = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=hot_chocolate)
textHotChocolate.grid(row=2,column=1)

textOrangeJuice= Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=orange_juice)
textOrangeJuice.grid(row=3,column=1)

textMilkShake = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=milkshake)
textMilkShake.grid(row=4,column=1)

textMountainDew = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, textvariable=mountain_dew)
textMountainDew.grid(row=5,column=1)

textSting = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=sting)
textSting.grid(row=6,column=1)

textCobra = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=cobra)
textCobra.grid(row=7,column=1)
# Foods

FriedChicken = Checkbutton(Food_Function,text="Fried Chicken\t\t\t ",variable=variable9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsFriedChicken).grid(row=0,sticky=W)
KareKare = Checkbutton(Food_Function,text="Kare kare",variable=variable10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsKareKare).grid(row=1,sticky=W)
CrispyPata = Checkbutton(Food_Function,text="Crispy Pata ",variable=variable11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsCrispyPata).grid(row=2,sticky=W)
SinigangBaboy = Checkbutton(Food_Function,text="Sinigang Baboy ",variable=variable12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsSinigangBaboy).grid(row=3,sticky=W)
SinigangHipon = Checkbutton(Food_Function,text="Sinigang Hipon ",variable=variable13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsSinigangHipon).grid(row=4,sticky=W)
BicolExpress = Checkbutton(Food_Function,text="Bicol Express ",variable=variable14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsBicolExpress).grid(row=5,sticky=W)
AsparagusTofu = Checkbutton(Food_Function,text="Asparagus Tofu ",variable=variable15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsAsparagusTofu).grid(row=6,sticky=W)
ChickenSisig = Checkbutton(Food_Function,text="Chicken Sisig ",variable=variable16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='sky blue',command=foodsChickenSisig).grid(row=7,sticky=W)

textFriedChicken=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=fried_chicken)
textFriedChicken.grid(row=0,column=1)

textKareKAre=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=kare_kare)
textKareKAre.grid(row=1,column=1)

textCrispyPata=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, textvariable=crispy_pata)
textCrispyPata.grid(row=2,column=1)

textSinigangBaboy=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=sinigang_baboy)
textSinigangBaboy.grid(row=3,column=1)

textSinigangHipon=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=sinigang_hipon)
textSinigangHipon.grid(row=4,column=1)

textBicolExpress=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=bicol_express)
textBicolExpress.grid(row=5,column=1)

textAsparagusTofu=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=asparagus_tofu)
textAsparagusTofu.grid(row=6,column=1)

textChickenSisig=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=chicken_sisig)
textChickenSisig.grid(row=7,column=1)

# ToTal Cost
lblTotalofDrinks=Label(Total_Function,font=('arial',14,'bold'),text='Total of Drinks\t',bg='sky blue',fg='black',justify=CENTER)
lblTotalofDrinks.grid(row=0,column=0,sticky=W)
textTotalofDrinks=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Drinks)
textTotalofDrinks.grid(row=0,column=1)

lblTotalofFood=Label(Total_Function,font=('arial',14,'bold'),text='Total of Foods  ',bg='sky blue',fg='black',justify=CENTER)
lblTotalofFood.grid(row=1,column=0,sticky=W)
textTotalofFood=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Food)
textTotalofFood.grid(row=1,column=1)

lblServiceCharge=Label(Total_Function,font=('arial',14,'bold'),text='Service Charge',bg='sky blue',fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
# Payment information

lblPaidTax=Label(Total_Function,font=('arial',14,'bold'),text='\tPaid Tax',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
textPaidTax=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=PaidTax)
textPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Total_Function,font=('arial',14,'bold'),text='\tSub Total',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
textSubTotal=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'), insertwidth=2,justify=RIGHT,textvariable=SubTotal)
textSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Total_Function,font=('arial',14,'bold'),text='\tTotal',bg='sky blue',bd=7,fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
textTotalCost=Entry(Total_Function,bg='white',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=TotalCost)
textTotalCost.grid(row=2,column=3)

# RECEIPT
textReceipt=Text(Receipt_Function,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
textReceipt.grid(row=0,column=0)


# BUTTONS
buttonTotal=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Total',bg='black',command=TotalofUnit).grid(row=0,column=0)
buttonReceipt=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Receipt',bg='black',command=Receipt).grid(row=0,column=1)
buttonReset=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Reset',bg='black',command=Reset).grid(row=0,column=2)
buttonExit=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Exit',bg='black',command=iExit).grid(row=0,column=3)


# Calculator Display




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




# Calculator
txtDisplay = Entry(Calculator_Function, width=45, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

# CALCULATOR BUTTONS
button7=Button(Calculator_Function, padx=16, pady=1, bd=7, fg='gold', font=('arial', 12, 'bold'), width=4, text='7',bg='black',command=lambda:btnClick(7)).grid(row=2,column=0)
button8=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='8',bg='black',command=lambda:btnClick(8)).grid(row=2,column=1)
button9=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='9',bg='black',command=lambda:btnClick(9)).grid(row=2,column=2)
buttonAdd=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='+',bg='black',command=lambda:btnClick('+')).grid(row=2,column=3)

button4=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='4',bg='black',command=lambda:btnClick(4)).grid(row=3,column=0)
button5=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='5',bg='black',command=lambda:btnClick(5)).grid(row=3,column=1)
button6=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='6',bg='black',command=lambda:btnClick(6)).grid(row=3,column=2)
buttonSub=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='-',bg='black',command=lambda:btnClick('-')).grid(row=3,column=3)

button1=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='1',bg='black',command=lambda:btnClick(1)).grid(row=4,column=0)
button2=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='2',bg='black',command=lambda:btnClick(2)).grid(row=4,column=1)
button3=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='3',bg='black',command=lambda:btnClick(3)).grid(row=4,column=2)
buttonMulti=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='*',bg='black',command=lambda:btnClick('*')).grid(row=4,column=3)

button0=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='0',bg='black',command=lambda:btnClick(0)).grid(row=5,column=0)
buttonClear=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='C',bg='black',command=btnClear).grid(row=5,column=1)
buttonEqual=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='=',bg='black',command=btnEquals).grid(row=5,column=2)
buttonDiv=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='/',bg='black',command=lambda:btnClick('/')).grid(row=5,column=3)

root.mainloop()

