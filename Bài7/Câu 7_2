def count_file_details (file_name):
    try:
        with open(file_name, 'r') as file:
             num_lines = 0
             num_words=0
             num_characters = 0
             for line in file:
                 num_lines += 1
                 num_characters += len (line)
                 num_words += len(line.split())
        print (f"Number of lines in file: {num_lines)")
        print (f"Number of words in file: (num_words)")
        print (f"Number of characters in file: (num_characters)")
    except FileNotFoundError:
        print (f"The file (file_name)' does not exist. Please check the file name again.")
    except Exception as e:
        print (f"An error occurred: (e)")
def main():
    file_name = input("Enter the file name to check: ").strip()
    count_file_details (file_name)
if_name_ =="_main_":
   main()
