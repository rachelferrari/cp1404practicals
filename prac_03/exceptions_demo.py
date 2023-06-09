"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")

# When will a ValueError occur?
# When numerator and denominator is not an integer

# When will a ZeroDivisionError occur?
# When the denominator is 0

# Could you change the code to avoid the possibility of a ZeroDivisionError
is_valid_input = False

while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator <= 0:
            print("Cannot divide by zero!")
        else:
            is_valid_input = True
            fraction = numerator / denominator
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
print("Finished.")