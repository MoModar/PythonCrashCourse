# TRY IT YOURSELF
# 10-6. Addition Calculator:

while True:
    print("\nEnter to numbers and i will try to add them together :)")
    x = input("First number: ")
    y = input("Second number: ")
    try:
        addition = int(x) + int(y)
        print("The addition is: " + str(addition))
    except ValueError:
        print("\nEnter a number instead please!\n")
