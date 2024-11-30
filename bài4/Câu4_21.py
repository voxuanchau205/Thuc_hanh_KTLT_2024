def is_divisible_by_5 (binary_str):
# Convert binary string to integer
    decimal_value int (binary_str, 2)
    return decimal_value %5==0
Enter a string of binary numbers from the keyboard
input_string input ("Enter a string of 4-digit binary numbers, separated by commas")
binary_numbers = input_string.split(',')
divisible_by_5 [binary for binary in binary_numbers if is_divisible_by_5 (binar
# Print out the results
if divisible_by_5:
   print("Binary numbers divisible by 5:", ', '.join(divisible_by_5))
else:
   print("There is no binary number divisible by 5.")
