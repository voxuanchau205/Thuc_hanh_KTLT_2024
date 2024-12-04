from tkinter import *
window = Tk()
window.title("welcome to LikeGeek app") window.geometry('350x200')
lbl = Label (window, text="Hello", font=("VNI-Thufap2", 12), fg="red", bg="blue") 
lbl.grid(column=3, row=0)
def clicked():
     lbl.configure (text="Button pressed!!", font= 12, fg="black", bg="yellow")
btn = Button(window, text="Click Me", font=12, fg="red", command=clicked) 
btn.grid(column=5, row=3)
window.mainloop()
