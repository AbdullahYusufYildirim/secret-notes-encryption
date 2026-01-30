# =====================
# IMPORTS
# =====================
import tkinter
import base64
from cryptography.fernet import Fernet
import hashlib
from tkinter import messagebox
import os


# =====================
# CRYPTO FUNCTIONS
# =====================
def encrypt_and_save():
    if title_entry.get() == "" or secret_text.get("1.0", "end-1c") == "" or master_key_entry.get() == "":
        messagebox.showerror(
            title="Error",
            icon="error",
            message="Please fill in all fields:\nTitle, secret note, and master key"
        )
        return

    secret = secret_text.get("1.0", "end-1c")
    password = master_key_entry.get()

    hashed = hashlib.sha256(password.encode()).digest()
    key = base64.urlsafe_b64encode(hashed)
    f = Fernet(key)

    token = f.encrypt(secret.encode())

    with open("noten.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{title_entry.get()}:\n")
        file.write(token.decode() + "\n\n")

    title_entry.delete(0, "end")
    secret_text.delete("1.0", "end")
    master_key_entry.delete(0, "end")


def decrypt_and_show():
    if secret_text.get("1.0", "end-1c") == "" or master_key_entry.get() == "":
        messagebox.showerror(
            title="Error",
            icon="error",
            message="Please fill in all fields:\nSecret note and master key"
        )
        return

    password = master_key_entry.get()
    hashed = hashlib.sha256(password.encode()).digest()
    key = base64.urlsafe_b64encode(hashed)
    f = Fernet(key)

    token_str = secret_text.get("1.0", "end-1c")
    token_bytes = token_str.encode()

    try:
        decrypted = f.decrypt(token_bytes)
        result = decrypted.decode()
    except:
        fake_bytes = os.urandom(len(token_str) // 2)
        result = fake_bytes.hex()

    secret_text.delete("1.0", "end")
    secret_text.insert("1.0", result)


# =====================
# UI SETUP
# =====================
note_app_interface = tkinter.Tk()
note_app_interface.title("Secret Notes")
note_app_interface.minsize(width=425, height=750)
note_app_interface.config(bg="light grey")

global_logo = tkinter.PhotoImage(file="kaka.png")
note_app_interface.iconphoto(True, global_logo)

logo_image = tkinter.Label(image=global_logo, bg="light grey")
logo_image.place(x=160, y=15, width=100, height=100)

title_label = tkinter.Label(
    text="Enter your title",
    fg="black",
    bg="light grey",
    font=("Arial", 18)
)
title_label.place(x=147, y=115)

title_entry = tkinter.Entry(
    relief="flat",
    bg="white",
    fg="black",
    highlightthickness=0
)
title_entry.place(width=300, x=53, y=150)

secret_label = tkinter.Label(
    text="Enter your secret",
    fg="black",
    bg="light grey",
    font=("Arial", 18)
)
secret_label.place(x=136, y=185)

secret_text = tkinter.Text(
    bg="white",
    fg="black",
    highlightthickness=0
)
secret_text.place(width=350, x=30, y=215)

master_key_label = tkinter.Label(
    text="Enter Master Key",
    fg="black",
    bg="light grey",
    font=("Arial", 16)
)
master_key_label.place(x=145, y=540)

master_key_entry = tkinter.Entry(
    relief="flat",
    bg="white",
    fg="black",
    highlightthickness=0
)
master_key_entry.place(width=300, x=58, y=570)

save_button = tkinter.Button(
    text="Save & Encrypt",
    width=12,
    command=encrypt_and_save
)
save_button.place(x=140, y=605)

decrypt_button = tkinter.Button(
    text="Decrypt",
    width=8,
    command=decrypt_and_show
)
decrypt_button.place(x=162, y=640)


# =====================
# MAIN LOOP
# =====================
note_app_interface.mainloop()
