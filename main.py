import tkinter

note_app_interface = tkinter.Tk()
note_app_interface.title("Secret Notes ")
note_app_interface.minsize(width = 425 , height = 750)
note_app_interface.config(bg="white")
note_app_interface.wm_iconbitmap("logo_image.gif")
logo = tkinter.PhotoImage(file = "logo_image.gif")
logo_image = tkinter.Label(image = logo,bg = "white")
logo_image.place(width = 410 ,height = 125)
note_app_interface.mainloop()
