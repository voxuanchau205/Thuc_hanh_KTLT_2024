def read_file(file_name):
      try:
          with open(file_name, 'r') as file: 
              content = file.read()
          print("File content:") print (content)
      except FileNotFoundError:
          print (f"File '(file_name)' does not exist. Please check the file name again. except Exception as e:
          print (f"An error occurred: {e}")
def main():
      file_name = input ("Enter file name to read: ").strip()
      read_file(file_name)
if_name_"_main_":
       mani()   
