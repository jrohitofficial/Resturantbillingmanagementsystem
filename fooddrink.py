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