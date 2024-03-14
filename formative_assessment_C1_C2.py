# question1
print("****************************************")
print("*       My Personal Information        *")
print("****************************************")
name = input("1. Name  :  ")
matric_num = input("2. Matric Number :  ")
class_name = input("3. Class  :  ")
phone_num = input ("4. Phone Numbers : ")
print("****************************************")

print("_________________________________________")
# question2
def seconds_to_minutes(seconds):
    minutes = seconds // 60
    # double baris tu kegunaan sik abis baki nya
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds

def main():
    seconds = int(input("Enter the number of seconds: "))
    minutes, remaining_seconds = seconds_to_minutes(seconds)
    print(f"{seconds} seconds is {minutes} minutes and {remaining_seconds} seconds.")

if __name__ == "__main__":
    main()
print("_________________________________________")

print("_________________________________________")
# question3
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

# a) i1 + (i2 * i3)
result_a = i1 + (i2 * i3)
print("a) Result:", result_a)

# b) i1 * (i2 + i3)
result_b = i1 * (i2 + i3)
print("b) Result:", result_b)

# c) i1 / (i2 + i3)
result_c = i1 / (i2 + i3)
print("c) Result:", result_c)

# d) i1 // (i2 + i3)
result_d = i1 // (i2 + i3)
print("d) Result:", result_d)

# e) i1 / i2 + i3
result_e = i1 / i2 + i3
print("e) Result:", result_e)

# f) i1 // i2 + i3
result_f = i1 // i2 + i3
print("f) Result:", result_f)

# g) 3 + 4 + 5 / 3
result_g = 3 + 4 + 5 / 3
print("g) Result:", result_g)

# h) 3 + 4 + 5 // 3
result_h = 3 + 4 + 5 // 3
print("h) Result:", result_h)

# i) (3 + 4 + 5) / 3
result_i = (3 + 4 + 5) / 3
print("i) Result:", result_i)

# j) (3 + 4 + 5) // 3
result_j = (3 + 4 + 5) // 3
print("j) Result:", result_j)

# k) d1 + (d2 * d3)
result_k = d1 + (d2 * d3)
print("k) Result:", result_k)

# l) d1 + d2 * d3
result_l = d1 + d2 * d3
print("l) Result:", result_l)

# m) d1 / d2 - d3
result_m = d1 / d2 - d3
print("m) Result:", result_m)

# n) d1 / (d2 - d3)
result_n = d1 / (d2 - d3)
print("n) Result:", result_n)

# o) d1 + d2 + d3 / 3
result_o = d1 + d2 + d3 / 3
print("o) Result:", result_o)

# p) (d1 + d2 + d3) / 3
result_p = (d1 + d2 + d3) / 3
print("p) Result:", result_p)

# q) d1 + d2 + (d3 / 3)
result_q = d1 + d2 + (d3 / 3)
print("q) Result:", result_q)

# r) 3 * (d1 + d2) * (d1 - d3)
result_r = 3 * (d1 + d2) * (d1 - d3)
print("r) Result:", result_r)
print("_________________________________________")


print("_________________________________________")
# question4
def cm_to_inches(cm):
    inches = cm / 2.54
    return inches

def main():
    length_cm = float(input("Enter a length in centimeters (cm): "))
    
    if length_cm < 0:
        print("Invalid entry. Length must be non-negative.")
    else:
        inches = cm_to_inches(length_cm)
        print(f"{length_cm} centimeters is equal to {inches} inches.")

if __name__ == "__main__":
    main()



# question5
def login(password):
    correct_password = "password10"
    attempts = 5

    while attempts > 0:
        user_input = input("Enter the password: ")
        if user_input == correct_password:
            print("You are logged in to the system.")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong password. You have {attempts} attempts left.")
            else:
                print("You are blocked from the system after five unsuccessful tries.")
                return

def main():
    login("password10")

if __name__ == "__main__":
    main()
print("_________________________________________")

print("_________________________________________")
# question6
def triangle(height):
    for i in range(height, 0, -1):
        print(" " * (height - i) + "*" * (2 * i - 1))

def main():
    height = int(input("Enter the height of the upside-down triangle: "))
    triangle(height)

if __name__ == "__main__":
    main()
print("_________________________________________")


print("_________________________________________")
# question7
def main():
    integers = input("Enter a list of integers separated by spaces: ").split()
    integers = [int(i) for i in integers]  # Convert strings to integers

    print("Total number of items in the list: ", len(integers))

    print("Last item in the list: ", integers[-1])

    print("List in reverse order: ", integers[::-1])

    if 5 in integers:
        print("Yes")
    else:
        print("No")

    remaining_items = integers[1:-1]
    remaining_items.sort()
    print("Sorted list after removing first and last items:", remaining_items)

if __name__ == "__main__":
    main()
print("_________________________________________")

print("_________________________________________")
# question8
def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users:
        if users[username] == password:
            print("You are now logged in to the system.")
        else:
            print("Invalid password.")
    else:
        print("Invalid username. You are not a valid user of the system.")

def main():
    users = {
        "bobo": "cimung2",
        "annur": "deksya.my",
        "abby": "ruran.com",
        "dina": "bedah.my",
        "christine": "emelda.com",
        "sarol": "anip",
        "theresia": "there.my",
        "jo": "jojo.com",
        "arrisha": "arrisha.com",
        "ikaa":"shk.03"
    }

    login(users)

if __name__ == "__main__":
    main()
print("_________________________________________")