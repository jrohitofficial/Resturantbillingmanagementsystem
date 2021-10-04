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