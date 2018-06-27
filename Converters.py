#Main screen

#Currency converter
def currency():
    user_choice = input("Dollars to Euros? choose D. \nDollars to Pounds? choose P. \nDollars to Chinese Yuan? choose C. \nDollars to Japanese Yen? choose J. \nExit? choose E. ")
    while user_choice != "E".lower():
        if user_choice == "D".lower():
            Dollars_to_Euros()
            user_choice = input("Do you want to convert again? ")
            
        elif user_choice == "P".lower():
            Dollars_to_Pounds()
            user_choice = input("Do you want to convert again? ")
                        
        elif user_choice == "C".lower():
            Dollars_to_Chinese()
            user_choice = input("Do you want to convert again? ")
            
        elif user_choice == "J".lower():
            Dollars_to_Japanese()
            user_choice = input("Do you want to convert again? ")
            
        else:
            user_choice = ("Do you want to try something else? ")
            
    print("Thanks for using my converter!!")
            


def Dollars_to_Euros():
    d = float(eval(input("Please enter the current dollar amount  :\n")))
    formula = d/1.18
    print("%d Amount in Dollars, results in %d Euros" %(d,formula))
        
def Dollars_to_Pounds():
    d = float(eval(input("Please enter the current dollar amount   :\n")))
    formula = d/1.35
    print("%d Amount in Dollars, results in %d Pounds"  %(d,formula))
    
def Dollars_to_Chinese():
    d = float(eval(input("Please enter the current dollar amount   :\n")))
    formula = d/0.16
    print("%d Amount in Dollars, results in %d Yuan"  %(d,formula))
    
def Dollars_to_Japanese():
    d = float(eval(input("Please enter the current dollar amount   :\n")))
    formula = d/0.0091
    print("%d Amount in Dollars, results in %d Yen"  %(d,formula))
    
    
currency()
#Temperature Converter
def temperature():
	user_choice = input("If you want to convert Celsius to Fahrenehit, choose C. \nIf you want to convert Fahrenheit to Celsius choose F. \nIf you want to quit, choose Q ")

	while user_choice != "q":
		if user_choice == "c":
			# call the Celsius to Fahrenheit function, ask if they want to repeat calculation
			Celsius_to_Fahrenheit()
			user_choice = input("Do you want to convert again? ")

		elif user_choice == "f":
			# call the Fahrenheit to Celsius function, ask if the user wants to repeat calculation
			Fahrenheit_to_Celsius()
			user_choice = input("Do you want to convert again? ")

		elif user_choice !="c" and user_choice !="f":
			# invalid character
			user_choice = input("Please enter a valid character ")
            

		else:
			# ask if they wish to repeat calculation
			user_choice = ("Do you want to try again? ")

	print("Thanks and now exiting this converter!!")

def Celsius_to_Fahrenheit():
	c = eval(input("Please enter the current temperature in Celsius  :\n"))
	f = (9/5) * c + 32
	print("%d degrees in Celsius result in %d degrees Fahrenheit" %(c,f))

def Fahrenheit_to_Celsius():
	f = eval(input("Please enter the current temperature in Fahrenheit  :\n"))
	c = (f-32) * 5/9
	print("%d degrees in Fahrenehit result in %d degrees Celsius" %(f,c))

temperature()

#units converter
def measurements():
    user_choice = input("What would you like to convert?\n Ounces to Grams, choose O\n Miles to Kilometers, choose M\n Feet to Meters, choose A\n If you are done, choose E ")
    while user_choice != "E".lower():
        if user_choice == "O".lower():
            #Ounces to grams
            Ounces_to_Grams()
            user_choice = input("Do you want to convert again? ")
            
        elif user_choice == "M".lower():
            #Miles to kilometers
            Miles_to_Kilometers()
            user_choice = input("Do you want to convert again? ")
            
        elif user_choice == "A".lower():
            #Feet to meters
            Feet_to_Meters()
            user_choice = input("Do you want to convert again? ")
            
        else:
            user_choice = ("Do you want to try again? ")
            
    print("Thanks and now exiting this converter!!")
    
def Ounces_to_Grams():
    g = eval(input("Please enter the amount of ounces  :\n"))
    h = g * 28.3495
    print("%d Ounces results in %d Grams" %(g,h))
    
def Miles_to_Kilometers():
    g = eval(input("Please enter the amount of miles  :\n"))
    h = g * 1.60934
    print("%d Miles results in %d Kilometers" %(g,h))
    
def Feet_to_Meters():
    g = eval(input("Please enter the amount of feet  :\n"))
    h = g * 0.3048
    print("%d Feet results in %d Meters" %(g,h))
    
    
    
    
measurements()
    
        
