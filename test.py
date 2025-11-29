import tkinter
from tkinter import *
import time
root = tkinter.Tk()
root.geometry("400x400")

frame = Frame(root)
frame.pack()
  
leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

bag = []



def show():
    root.withdraw()

    show_window = Toplevel(root)
    show_window.geometry("400x400")
    show_window.title("Vissa innehållet")
    listbox = Listbox(show_window, width=30, height=10)
    listbox.pack(pady=10)

    for item in bag:
        listbox.insert(END, item)
    def exit():
        show_window.destroy()
        root.deiconify()

    Button(show_window, text="Tillbaks", command=exit).pack(pady=10)

def save():
    
    root.withdraw()

    save_window = Toplevel(root)
    save_window.geometry("400x200")
    save_window.title("Spara nåt i påsen")
    if len(bag) >= 10:
        label = Label(save_window, text='Du kan inte har mer än 10 grejer i påsen!!', font=(10), bg='red')
        label.pack()
    else:
        entry = Entry(save_window)
        entry.pack()

    def exit():
        try:
            bag.append(entry.get().lower())
            save_window.destroy()
            root.deiconify()
            update()
        except NameError:
            save_window.destroy()
            root.deiconify()

    Button(save_window, text="Spara", command=exit, bg='green').pack(pady=10)

def remove():
    root.withdraw()

    remove_window = Toplevel(root)
    remove_window.geometry("400x400")
    remove_window.title("Ta bort nåt ur påsen")

    listbox = Listbox(remove_window)
    listbox.pack(pady=10)

    for item in bag:
        listbox.insert(END, item)

    label = Label(remove_window, text='Skriv vad du vill ta bort ur påsen')
    label.pack()
    entry = Entry(remove_window)
    entry.pack()

    def exit():
        bag.remove(entry.get().lower())
        remove_window.destroy()
        root.deiconify()
        update()

    def exit_nosave():
        remove_window.destroy()
        root.deiconify()

    Button(remove_window, text="Ta bort", command=exit, bg='red').pack(pady=10)
    Button(remove_window, text="Tillbaks", command=exit_nosave, bg='green').pack(pady=10)

def search():
    
    root.withdraw()

    search_window = Toplevel(root)
    search_window.geometry("400x200")
    search_window.title("Söka nåt i påsen")

    label = Label(search_window, text='Skriv vad du vill söka i påsen')
    label.pack()

    entry = Entry(search_window)
    entry.pack()

    def exit():
        try:
            search_window.withdraw()
            show_window = Toplevel(root)
            show_window.geometry("400x400")
            show_window.title("Sök resultat")
            listbox = Listbox(show_window, width=30, height=10)
            listbox.pack(pady=10)
            for thing in bag:
                if thing.startswith(entry.get().lower()):
                    listbox.insert(END, thing)
            def exit_home():
                search_window.destroy()
                show_window.destroy()
                root.deiconify()
            Button(show_window, text="Tillbaks", command=exit_home).pack(pady=10)

        except NameError:
            search_window.destroy()
            root.deiconify()

    Button(search_window, text="Sök", command=exit).pack(pady=10)


label = Label(frame, text = 'Vällkommen till påse. Klicka på knapparna för att göra nåt med påsen')
label.pack()

label1 = Label(leftframe, text = 'Plats kvar i påsen:').pack()

label2 = Label(leftframe, text=10-len(bag), font=(20), pady=25)
label2.pack()

def update():

    label2.config(text=10-len(bag))



button1 = Button(rightframe, text = 'Visa innehållet', command = show)
button1.pack(padx= 100, pady= 25)

button2 = Button(rightframe, text = 'Spara', command = save)
button2.pack(padx= 100, pady= 25)

button3 = Button(rightframe, text = 'Ta bort', command = remove)
button3.pack(padx= 100, pady= 25)

button4 = Button(rightframe, text = 'Sök', command = search)
button4.pack(padx= 100, pady= 25)

button5 = Button(rightframe, text = 'Exit', bg='red', command = root.destroy)
button5.pack(padx= 100, pady= 25)


root.mainloop()