import tkinter
import base64
from cryptography.fernet import Fernet
import hashlib
from tkinter import messagebox
import os



global_logo = None

""" 
window
"""
note_app_interface = tkinter.Tk()
note_app_interface.title("Secret Notes ")
note_app_interface.minsize(width = 425 , height = 750)
note_app_interface.config(bg="light grey")
"""
encryptin func
"""


"""
decrypt func
"""
base64_string = None

"""
logo image 
"""
global_logo = tkinter.PhotoImage(file = "kaka.png")

note_app_interface.iconphoto(True,global_logo)



logo_image = tkinter.Label(image = global_logo ,bg = "light grey")
logo_image.place(x = 160 , y = 15 ,width =100 ,height = 100)

"""
Enter Your Title Label
"""
title_label = tkinter.Label(text = "Enter your title",fg = "black",bg = "light grey",font = ("Arial",18,))
title_label.place(x = 147 , y = 115 ,)
"""
Title Entry
"""
title_entry = tkinter.Entry(relief="flat",borderwidth=0,bg = "white",fg = "black",highlightbackground = "light grey"
                            ,insertbackground="blue",highlightthickness=0)
title_entry.place(width = 300 ,x = 53 ,y = 150)

"""
Enter Your Secret Label
"""
secret_label = tkinter.Label(text = "Enter your secret ", fg = "black",bg = "light grey", font = ("Arial",18,))
secret_label.place(x = 136 , y = 185)
"""
decrypt func
"""
samples = ""

"""
Secret Text 
"""
secret_text = tkinter.Text(note_app_interface,bg = "white",fg = "black",highlightbackground = "light grey",insertbackground="blue",highlightthickness=0)
secret_text.place(width = 350 , x = 30 , y = 215)




"""
Enter Master Key Label 
"""
master_key_label = tkinter.Label(text = "Enter Master Key", fg = "black",bg = "light grey", font = ("Arial",16,))
master_key_label.place(x = 145 , y = 540)
"""
Master Key Entry
"""
master_key_entry = tkinter.Entry(relief="flat",borderwidth=0,fg = "black", bg = "white",highlightbackground = "light grey",
                                 insertbackground="blue",highlightthickness=0)
master_key_entry.place(width = 300 ,x = 58,y = 570)
"""
message_box
"""

"""
"""
def encrypt_and_save(): #içine paswordu yaz fonksiyonu çalıştırmak için
    if title_entry.get() == "" or secret_text.get("1.0", "end-1c") == "" or master_key_entry.get() == "":
        messagebox.showerror(title="error", icon="error",
                             message="Please fill in all fields: \n title, secret note, and master key")
        return

    secret = secret_text.get("1.0", "end-1c")  # Gizli not
    pasword = master_key_entry.get()  # Parola
    hashed = hashlib.sha256(pasword.encode()).digest()  # yazılan paswordu 32 byts a çevir
    key = base64.urlsafe_b64encode(hashed)
    f = Fernet(key)
    token = f.encrypt(secret.encode())
    with open("noten.txt", mode="a", encoding="utf-8") as my_note_content:
        my_note_content.write(f"{title_entry.get()} : \n")
        my_note_content.write(token.decode() + "\n\n")
    title_entry.delete(0, "end")
    secret_text.delete("1.0", "end")
    master_key_entry.delete(0, "end")

def decrypt_and_show():
    if secret_text.get("1.0", "end-1c") == "" or master_key_entry.get() == "":
        messagebox.showerror(title = "error",icon = "error" , message = "Please fill in all fields: \n secret note, and master key")
        return
    user_password = master_key_entry.get()
    user_hashed = hashlib.sha256(user_password.encode()).digest()
    key2 = base64.urlsafe_b64encode(user_hashed)
    f2 = Fernet(key2)
    token_str = secret_text.get("1.0", "end-1c")
    token_bytes = token_str.encode()
    try :
        decrypted_bytes = f2.decrypt(token_bytes) # 🔓 ASIL ÇÖZME
        result = decrypted_bytes.decode() # bytes → str

    except :
        fake_bytes = os.urandom(len(token_str)// 2)
        result = fake_bytes.hex()

    secret_text.delete("1.0", "end")
    secret_text.insert("1.0",result)




"""
Save & Encrypt Button
"""
save_and_encrypt_button = tkinter.Button(text = "Save & Encrypt", fg = "black", bg = "light grey",font = ("Arial,12")
                                         ,width = 12,highlightthickness=0,highlightbackground = "light grey",command = encrypt_and_save)
save_and_encrypt_button.place(x = 140 , y = 605)

"""
Decrypt Button 
"""
decrypt_button = tkinter.Button(text = "Decrypt", fg = "black", bg = "light grey",font = ("Arial,10")
                                ,relief="flat",borderwidth=0 ,overrelief="ridge",width = 8,highlightbackground = "light grey"
                                ,command = decrypt_and_show)
decrypt_button.place(x = 162 , y = 640)



note_app_interface.mainloop()   
