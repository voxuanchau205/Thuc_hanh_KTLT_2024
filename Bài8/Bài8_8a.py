import tkinter as tk
from tkinter import messagebox
* Function to display personal information
def show_personal_info():
    name = entry_name.get()
    dob entry_dob.get()
    mssv = entry_mssv.get()
    major = entry_major.get()
    messagebox.showinfo("Personal information", f"Full name: {name}\nDate of birth: {dob}\nStudent ID: {mssv}\nMajor:
# Function to handle when the user clicks on the "Click Me" button
def show_radio_choice():
   choice var.get()
   messagebox.showinfo("Choice information", f"You have selected number: {choice}")
# Generation of key numbers
root = tk.Tk()
root.title("Personal Info & Radio Button")
# Personal information form section
frame_info = tk. LabelFrame (root, text="Personal information", padx=10, pady=10)
frame info.grid(row=0, column=0, padx=20, pady=20)
# Label and Entry for Full Name
tk.Label (frame info, text="Họ tên:").grid(row=0, column=0, sticky="e")
entry_name = tk.Entry (frame_info)
entry_name.grid(row=0, column=1)
# Label and Entry for Date of Birth
tk. Label (frame_info, text="Ngày sinh (dd/mm/yyyy):").grid(row=l, column=0, sticky="e")
entry_dob = tk. Entry(frame_info)
entry_dob.grid(row=l, column=1)
Label and Entry for MSSV
tk. Label (frame info, text="MSSV:").grid(row=2, column=0, sticky="e")
entry_mssv tk.Entry(frame_info)
entry_mssv.grid(row=2, column=1)
#Label and Entry for Field of Study
tk. Label (frame_info, text="Ngành học:").grid(row=3, column=0, sticky="e")
entry_major = tk. Entry(frame_info)
entry_major.grid(row=3, column=1)
* Button to display personal information
btn_show_info tk. Button (frame_info, text="Show info", command=show_personal_info)
btn_show_info.grid(row=4, columnspan=2, pady=10)
