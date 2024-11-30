import numpy as np
data_type = [('name', 'S15'), ('height', float), ('class', int)]
# Student data
students_details = [
    (b'd', 48.5, 5),
    (b'a', 52.5, 6),
    (b'c', 42.1, 5),
    (b'e', 40.11, 5),
    (b'f', 54.0, 6),
    (b'g', 45.0, 5)
# Create structured array
students np.array (students_details, dtype=data_type)
# Print the original array
print("Original array:")
print (students)
* sort array by layer first and height later
sorted_students np.sort (students, order=['class', 'height'])
# Print the sorted array
print("Array after sorting by class and height:")
print (sorted_students)
