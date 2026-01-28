import tkinter
global_logo = None
"""
window
"""
note_app_interface = tkinter.Tk()
note_app_interface.title("Secret Notes ")
note_app_interface.minsize(width = 425 , height = 750)
note_app_interface.config(bg="light grey")
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
Secret Text 
"""
secret_text = tkinter.Text(bg = "white",fg = "black",highlightbackground = "light grey",insertbackground="blue",highlightthickness=0)
secret_text.place(width = 350 , x = 30 , y = 215)

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
                                         ,width = 12,highlightthickness=0,highlightbackground = "light grey")
save_and_encrypt_button.place(x = 140 , y = 605)

"""
Decrypt Button 
"""
decrypt_button = tkinter.Button(text = "Decrypt", fg = "black", bg = "light grey",font = ("Arial,10")
                                ,relief="flat",borderwidth=0 ,overrelief="ridge",width = 8,highlightbackground = "light grey")
decrypt_button.place(x = 162 , y = 640)



note_app_interface.mainloop()   
