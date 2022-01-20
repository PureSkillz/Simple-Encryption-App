"""
32 - 126 inclusive
to hex: hex(num)[2:]
to dec: int(hex, 16)
"""


import random
from tkinter import *


def encode():
    message = en.get()
    key_value = random.randint(1, 95)
    while key_value == 32 or key_value == 63:  # avoids letters just getting bigger/smaller
        key_value = random.randint(1, 95)
    receive = [el for el in message]
    processing = [chr(ord(el) + key_value) for el in receive]  # sets new values
    new = [str(hex(key_value)[2]) if key_value > 15 else "0"]  # sets the first half of the hex value of the key at the beginning
    for el in processing:
        if ord(el) > 126:
            new.append(chr(ord(el) - 95))  # loop if necessary
        else:
            new.append(el)
    new.append(str(hex(key_value)[-1]))  # sets the second half of the hex value of the key at the end
    en_done.delete(0, END)
    en_done.insert(0, "".join(new))
    # return "".join(new)


def decode():
    message = de.get()
    key_value = int(message[0] + message[-1], 16)  # reads the hex value of the key
    message = [el for el in message[1:-1]]
    processing = [ord(el) - key_value for el in message]
    new = []
    for el in processing:
        if el < 32:
            el += 95
        new.append(chr(el))
    de_done.delete(0, END)
    de_done.insert(0, "".join(new))
    # return "".join(new)


if __name__ == "__main__":
    tk = Tk()
    tk.geometry("600x300")
    tk.title("Encryption app")
    icon = PhotoImage(file='lock.png')
    tk.iconphoto(True, icon)
    tk.config(background="#198258")
    Label(tk, text="Encryption App", font=('Helvetica', 18, 'bold'), bg='#000000', fg="#ffffff").place(x=220, y=10)
    # first half - encrypt
    en = Entry(tk, font=("Helvetica", 14), width=42)
    en.place(x=40, y=60)
    Label(tk, text="In:", bg="#198258", font=('Helvetica', 12, 'bold')).place(x=10, y=60)
    # second half - encrypt
    en_done = Entry(tk, font=("Helvetica", 14), width=42)
    en_done.place(x=40, y=90)
    Label(tk, text="Out:", bg="#198258", font=('Helvetica', 12, 'bold')).place(x=0, y=90)
    Button(tk, text="Encrypt", bg="black", fg="white", command=encode).place(x=530, y=70)
    # split
    # first half - decrypt
    de = Entry(tk, font=("Helvetica", 14), width=42)
    de.place(x=40, y=180)
    Label(tk, text="In:", bg="#198258", font=('Helvetica', 12, 'bold')).place(x=10, y=180)
    # second half - encrypt
    de_done = Entry(tk, font=("Helvetica", 14), width=42)
    de_done.place(x=40, y=210)
    Label(tk, text="Out:", bg="#198258", font=('Helvetica', 12, 'bold')).place(x=0, y=210)
    # end
    Button(tk, text="Decrypt", bg="black", fg="white", command=decode).place(x=530, y=190)
    tk.mainloop()