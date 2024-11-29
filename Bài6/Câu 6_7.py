import math
class Circle:
    def_init_(self, radius):
          self.radius = radius
    def calculate_area(self):
          return math.pi * (self.radius ** 2)
    def perimeter(self):
          return 2 * math.pi * self.radius
def main():
    radius float(input("Enter radius of circle: ").strip())
    circle Circle (radius)
    area = circle.tinh_dien_tich()
    circumference circle.calculate_perimeter()
    print(f"dien tich hinh tron la: {area:.2f}")
    print (f"Circumference of circle is: (circumference:.2f}")
if_nam_==_ main_":
    main()
