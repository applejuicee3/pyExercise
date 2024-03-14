temperature = input ("what is the temperature :")

temperature = float(temperature)

if temperature <= 37.5 :
    print("normal")
    
elif temperature <= 38 :
    print("fever")
    
else:
    print("You have covid-19")



