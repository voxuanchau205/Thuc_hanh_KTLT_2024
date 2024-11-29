def copy_file(source_file, destination_file):
    try:
       with open (source_file, 'r') as src:
            content = src.read()
       with open (destination_file, 'w') as dest:
            dest.write(content)
       print (f"Copied contents from (source_file)' to (destination_file)' thanh cong)
    except FileNotFoundError:
       print (f" Source file (source_file), does not exist. Please check again.")
    except Exception as e:
       print (f"An error occurred: (e)")
def main():
    source_file input ("Enter source file name: ").strip()
    destination_file input("Enter destination file name: ").strip()
    copy_file (source_file, destination_file)
if_name_ =="_main_":
    main()
