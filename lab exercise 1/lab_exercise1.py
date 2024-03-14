# 1(a)
# Loop through numbers from 0 to 10
for i in range(11):
    square = i * i
    print(f"The square of {i} is {square}")
 
    
# 1(b)
# Initialize the sum variable
sum_even = 0

# Loop through numbers from 0 to 10
for i in range(0, 11, 2):  # Start from 0, step by 2 (to consider only even numbers)
    sum_even += i
print("The sum of all even numbers from 0 to 10 is:", sum_even)


# 2
def is_alphabetic(username):
    """Check if the username consists of alphabetical characters only."""
    return username.isalpha()

def is_numeric(password):
    """Check if the password consists of numeric characters only."""
    return password.isdigit()

def authenticate():
    """Authenticate the user based on username and password."""
    username = input("Enter username (alphabetical characters only): ")
    password = input("Enter password (at least 5 numeric characters): ")

    if not is_alphabetic(username):
        print("Error: Username must contain only alphabetical characters.")
        return False

    if len(password) < 5:
        print("Error: Password must be at least 5 characters long.")
        return False

    if not is_numeric(password):
        print("Error: Password must contain only numeric characters.")
        return False

    print("Authentication successful!")
    return True

# Main program
if __name__ == "__main__":
    authenticated = authenticate()
    if not authenticated:
        print("Authentication failed. Please try again.")


# 3
def calculate_monthly_payment(car_price, down_payment, loan_period):
    # Calculate the loan amount
    loan_amount = car_price - down_payment
    
    # Check if the down payment meets the minimum requirement
    if down_payment < car_price * 0.1:
        print("You are not eligible for the bank loan.")
        return None
    
    # Calculate total interest
    interest_rate = 0.027  # 2.7% interest rate
    total_interest = interest_rate * loan_amount * loan_period
    
    # Calculate monthly installment
    total_months = loan_period * 12
    monthly_installment = (loan_amount + total_interest) / total_months
    
    return monthly_installment

# Main program
if __name__ == "__main__":
    car_price = 103300  # Price of Proton X50 full specs
    down_payment = float(input("Enter down payment amount (minimum 10% of the car price): "))
    loan_period_years = int(input("Enter loan period in years: "))
    
    monthly_payment = calculate_monthly_payment(car_price, down_payment, loan_period_years)
    if monthly_payment is not None:
        print("Monthly payment: RM", format(monthly_payment, ".2f"))
