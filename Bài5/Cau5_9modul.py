
from search_module import binary_search
n = int (input("Decimal number of elements in the list: "))
lst=[]
for i in range(): 
  element = int(input("Tower of (i+1)th element: "))
  lst.append(element)
print("ds sau khi sap xep:" lst)
lst.sort()
value = int (input("Enter the element to search for: "))
found = binary_search(lst, value)
if found:
   print("The element (value) was found in the list.")
else:
  print("The (value) was not found in the list.")
