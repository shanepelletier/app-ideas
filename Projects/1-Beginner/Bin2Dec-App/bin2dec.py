import re

def is_valid_binary(string):
    for character in string:
        if character != "0" and character != "1":
            return False
    return True

binary_text = input("Please enter up to 8 bits to be converted into a decimal number: ")

if not binary_text:
    print("ERROR! Must enter at least one bit.")
    # Somehow exit the program...

if len(binary_text) > 8:
    print("ERROR! Must enter less than eight bits")

if not is_valid_binary(binary_text):
    print("ERROR! Must only contain 0s or 1s")

decimal_number = 0

for index, digit in enumerate(binary_text):
    # TIL that you can reassign variables with different data types like in Rust. I wonder if this works with the static type analyzers too...
    digit = int(digit)
    decimal_number += digit * index ** 2

print(decimal_number)