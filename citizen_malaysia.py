
yes = input("Are you Citizen of Malaysia?  :")
age = float(input("Please enter your age :"))

if yes and age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote in Malaysia.")
