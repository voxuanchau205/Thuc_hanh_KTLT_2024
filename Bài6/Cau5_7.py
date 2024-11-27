import numpy as np
# Define data types for structured arrays
data_type [('name', 'S15'), ('height', float), ('class', int)]
* Student data
students_details = [
   ('Phung Thanh Do (Mixigaming)', 165, 5),
   ('Lam Dinh Khoa (Rambo)', 170, 6),
   ('Tran Thai Linh (Nhims)', 156, 5),
   ('Nguyen Van Thuan (Snake)', 165.5, 5)
* Create structured arrays
students np.array (students_details, dtype=data_type)
* Print the original array
print("Original array:")
print (students)
* Sort array by height
sorted_students np.sort(students, order='chiều cao')
# Print the sorted array
print("\nSorted array by height:")
print(sorted_students)
