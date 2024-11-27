    result =0
    prev_value=0
    for char in reversed (roman): 
          current_value = self.roman_values.get(char)
          if current_value < prev_value: 
              result = current_value
          else:
              result += current_value
          prev_value current_value
    return result
 def main(): 
   converter RomanToInt()
   roman_number = input ("Enter Roman numbers: ").upper().strip()
   if not roman_number or any (c not in converter.roman_values ​​for c in roman_number): 
     print("Invalid Roman numeral.")
     return
   try:
     integer_value = converter.convert (roman number)
     print (f"Roman number (roman_number), converted to integer is: (integer_value}")
   except Exception as e:
     print (f"An error occurred: (e)")
 if_name_=="_main_":
     main()
