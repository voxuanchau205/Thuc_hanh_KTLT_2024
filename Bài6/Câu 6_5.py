class StringReverser:
     def_init_(self, input_string):
         self.input_string input_string -
     def reverse_words(self):
         words = self.input_string.split()
         reversed_words = words[::-1]
         return ' '.join(reversed_words)
def main():
     input_string input ("Enter string: ").strip() =
     reverse StringReverser ( input_string ) =
     output_string reverser.reverse_words () =
     print (f"String after reversing from: (output_string)")
if_name_=="_main_":
     main()
