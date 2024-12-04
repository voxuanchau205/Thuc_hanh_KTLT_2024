def NewFile():
    print("New File!")
def OpenFile():
    print("OpenFile!")
def Exit():
    print("Đã Thoát!")
def InsText():
    print("InsText!")
def InsPic():
    print("InsPic")
def About():
    print("This is a simple example of a menu")
root Tk() =
menu = Menu (root)
root.config (menu=menu)
filemenu = Menu (menu)
menu.add cascade (label="File", menu=filemenu)
filemenu.add_command (label="New", command=NewFile)
filemenu.add_command (label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add command (label="Exit", command=root.quit)
Insertmenu Menu (menu)
menu.add_cascade (label="Insert", menu=Insertmenu)
Insertmenu.add command (label="Text", command=InsText)
Insertmenu.add_command (label="Picture", command=InsPic)
helpmenu = Menu (menu)
menu.add_cascade (label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
mainloop()
