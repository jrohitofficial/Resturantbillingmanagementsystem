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

txtDisplay = Entry(Calculator_Function, width=45, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")