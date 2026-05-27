from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)



window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=110, pady=110)

my_label = Label(text="My Label", font=("Arial", 24, "bold"))
my_label.config(text="new text")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

button = Button(text="Click here", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click here", command=button_clicked)
button2.grid(column=2, row=0)

input = Entry(width=10)
# print(input.get())
input.grid(column=3, row=3)







window.mainloop()