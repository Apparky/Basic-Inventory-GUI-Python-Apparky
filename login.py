import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("The Grocery Store  |  APPARKY")
main.resizable(0, 0)


def Exit():
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()


main.protocol("WM_DELETE_WINDOW", Exit)


def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()


lbl1 = Label(main)
lbl1.place(relx=0, rely=0, width=1366, height=768)
image = PhotoImage(file="./images/main.png")
lbl1.configure(image=image)

btn1 = Button(main)
btn1.place(relx=0.316, rely=0.446, width=146, height=90)
btn1.configure(relief="flat")
btn1.configure(overrelief="flat")
btn1.configure(activebackground="#ffffff")
btn1.configure(cursor="hand2")
btn1.configure(foreground="#ffffff")
btn1.configure(background="#ffffff")
btn1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/1.png")
btn1.configure(image=img2)
btn1.configure(command=emp)

btn2 = Button(main)
btn2.place(relx=0.566, rely=0.448, width=146, height=90)
btn2.configure(relief="flat")
btn2.configure(overrelief="flat")
btn2.configure(activebackground="#ffffff")
btn2.configure(cursor="hand2")
btn2.configure(foreground="#ffffff")
btn2.configure(background="#ffffff")
btn2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
btn2.configure(image=img3)
btn2.configure(command=adm)

main.mainloop()
