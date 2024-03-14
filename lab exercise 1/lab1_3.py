def calculate_monthly_payment(car_price, down_payment, loan_period):
    # Calculate loan amount
    loan_amount = car_price - down_payment

    # Check if down payment is at least 10% of the car price
    if down_payment < car_price * 0.1:
        print("You are not eligible for the bank loan.")
        return None

    # Calculate total interest
    interest_rate = 0.027  # 2.7% annual interest rate
    total_interest = interest_rate * loan_amount * loan_period

    # Convert loan period from years to months
    loan_period_months = loan_period * 12

    # Calculate monthly installment
    monthly_payment = (loan_amount + total_interest) / loan_period_months

    return monthly_payment

def main():
    car_price = 90000  # Full specs price of Proton X50
    down_payment = float(input("Please enter your downpayment: "))
    loan_period_years = int(input("How long you want to make a loan in years (1 to 9 years only): "))

    monthly_payment = calculate_monthly_payment(car_price, down_payment, loan_period_years)
    if monthly_payment is not None:
        print("You need to pay RM {:.2f} monthly as your payment.".format(monthly_payment))

if __name__ == "__main__":
    main()
