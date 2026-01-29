import tkinter
import base64
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
title_entry = tkinter.Entry(relief="flat",borderwidth=0,bg = "white",fg = "black",highlightbackground = "light grey",insertbackground="blue",highlightthickness=0)
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
def decrypt():
    global samples
    string_64 = secret_text.get("1.0","end-1c")  #şifrelenmş mesAjı string_64 değerine atadık
    bytes_base64 = string_64.encode("utf-8")  # base 64 stringini base 64 e çevir
    bytes_Strings_sample = base64.b64decode(bytes_base64)  # base 64 ü byte a çevier
    samples = bytes_Strings_sample.decode("utf-8")  # ascii ile bytı a normal stringe çevir
    secret_text.delete("1.0","end-1c")
    secret_text.insert("1.0",samples)
    print(samples)

"""
Secret Text 
"""
secret_text = tkinter.Text(note_app_interface,bg = "white",fg = "black",highlightbackground = "light grey",insertbackground="blue",highlightthickness=0)
secret_text.place(width = 350 , x = 30 , y = 215)

def encrypt():
    encode_string = secret_text.get("1.0","end-1c")
    encode_string_bytes = encode_string.encode("utf-8")  # metn, ascii formatında byte a çevir
    base64_bytes = base64.b64encode(encode_string_bytes) # byte dan base 64 e
    base64_string = base64_bytes.decode("utf-8")  #base 64 tekrar ascii string



    with open("noten.txt", mode="a", encoding="utf-8") as my_note_content:
        my_note_content.write(f"{title_entry.get()} : \n")
        my_note_content.write(f"  {base64_string}\n\n")
        my_note_content.flush()
        os.fsync(my_note_content.fileno())

"""
Enter Master Key Label 
"""
master_key_label = tkinter.Label(text = "Enter Master Key", fg = "black",bg = "light grey", font = ("Arial",16,))
master_key_label.place(x = 145 , y = 540)
"""
Master Key Entry
"""
master_key_entry = tkinter.Entry(relief="flat",borderwidth=0,fg = "black", bg = "white",highlightbackground = "light grey",insertontime=100,
                                 insertbackground="blue",highlightthickness=0)
master_key_entry.place(width = 300 ,x = 58,y = 570)
"""
Save & Encrypt Button
"""
save_and_encrypt_button = tkinter.Button(text = "Save & Encrypt", fg = "black", bg = "light grey",font = ("Arial,12")
                                         ,width = 12,highlightthickness=0,highlightbackground = "light grey",command = encrypt)
save_and_encrypt_button.place(x = 140 , y = 605)

"""
Decrypt Button 
"""
decrypt_button = tkinter.Button(text = "Decrypt", fg = "black", bg = "light grey",font = ("Arial,10")
                                ,relief="flat",borderwidth=0 ,overrelief="ridge",width = 8,highlightbackground = "light grey",command = decrypt)
decrypt_button.place(x = 162 , y = 640)


note_app_interface.mainloop()   
