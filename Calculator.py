from tkinter import *

def click(event):
    text=event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


window = Tk()
window.title("Calculator")
window.geometry("650x700")

scvalue = StringVar()
scvalue.set("")
screen = Entry(window, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, pady=20, padx=20)

#------------------------------------------------------------------------------------------------------
frame = Frame(window, bg="grey")
b = Button(frame, text="9", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="8", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="7", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="+", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)
frame.pack()

#------------------------------------------------------------------------------------------------------
frame = Frame(window, bg="grey")
b = Button(frame, text="6", padx=29, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="5", padx=29, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="4", padx=29, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="-", padx=30, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)
frame.pack()

#------------------------------------------------------------------------------------------------------
frame = Frame(window, bg="grey")
b = Button(frame, text="3", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="2", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="1", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="*", padx=30, pady=22, font="lucida 31 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)
frame.pack()

#------------------------------------------------------------------------------------------------------
frame = Frame(window, bg="grey")
b = Button(frame, text="C", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="0", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(frame, text="=", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)
b = Button(frame, text="/", padx=28, pady=22, font="lucida 30 bold")
b.pack(side="left", padx=18, pady=5)
b.bind("<Button-1>", click)
frame.pack()

window.mainloop()