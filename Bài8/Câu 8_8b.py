# Radio button form part
frame radio tk. LabelFrame (root, text="Lựa chọn", padx=10, pady=10) 
frame_radio.grid(row=1, column=0, padx=20, pady=20)
# Create a variable to store the selected value of the radio button
was tk. IntVar()
# Radio buttons
tk. Radiobutton (frame_radio, text="First", variable=var, value=1).grid(row=0, column=0, sticky="w")
tk. Radiobutton (frame_radio, text="Second", variable=var, value=2).grid(row=0, column=1, sticky="w") 
tk. Radiobutton (frame_radio, text="Third", variable=var, value=3).grid(row=0, column=2, sticky="w")
# Button to display radio button selection information
btn_show_choice tk. Button (frame_radio, text="Click Me", command=show_radio_choice) 
btn_show_choice.grid(row=1, columnspan=10, pady-10)
# Start interface loop
root.mainloop()
