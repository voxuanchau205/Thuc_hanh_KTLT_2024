import math
def Tinh (R):
   # Check radius validity
   if R <= 0:
      return "Invalid radius! Please enter a positive radius."
   # Calculate perimeter and area
   chu_vi = 2 * math.pi *R
   dien_tich = math.pi*R** 2
   return chu_vi , dien_tich
# Enter radius from keyboard
try:
   R= float(input("Enter radius R: "))
   ket_qua= Tinh(R)
   if isinstance (ket_qua, tuple):
     print (f"chu vi hinh tron: (ket_qua[0]:.2f}")
     print (f"dien tich hinh tron: (ket_qua [1]:.2f}")
   else:
     print(ket_qua)
except ValueError:
   print("Please enter a valid number.")
