temperature = float(input("Please enter your temperature :"))
forecast = input("What is the forecast :")

if temperature < 80 and forecast != "rain":
    print("go outside!")
    
else:
    print("stay inside!")