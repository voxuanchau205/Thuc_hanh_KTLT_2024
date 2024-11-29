def write_list_to_file(file_name, data_list):
   try:
       with open(file_name, 'w') as file:
              for item in data_list:
                 file.write(item+'\n')
       print (f"Successfully wrote list contents to file '{file_name}'.")
   except Exception as e:
       print (f"An error occurred while writing to file: {e}")
def main():
   data_list = [
        "Line 1",
        "Line 2",
        "Line 3",
        "Line 4",
        "Line 5"
   file_name input ("Enter the file name you want to write to: ").strip()
   write_list_to_file(file_name, data_list)
if _name_ == "_main_":
   main()
