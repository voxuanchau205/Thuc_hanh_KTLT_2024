string-input("enter a string: ")
#remove all numbers from string
chuoi_moi= ''.join([ky_tu for ky_tu in chuoi if not ky_tu.isdigit()))
#reprint new string
print("new string:", new_string)
