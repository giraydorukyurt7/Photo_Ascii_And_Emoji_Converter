import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Photo Ascii And Emoji Converter")  #title
        self.root.geometry("600x600")                       #window size
        self.root.iconbitmap(r'images/logo/logo.png')       #icon
        
        #############
        self.menubar = tk.Menu(self.root)                   #creating a menubar

        self.filemenu = tk.Menu(self.menubar, tearoff=0)                        #First menu
        self.filemenu.add_command(label="CLOSE", command=self.on_closing)       #Filemenu element #1
        self.filemenu.add_separator()                                           #The line between elements
        self.filemenu.add_command(label="CLOSE Without Question", command=exit) #filemenu element #2


        self.menubar.add_cascade(menu=self.filemenu, label="File") #add filemenu to menubar
        
        self.root.config(menu=self.menubar)
        #############

        self.label = tk.Label(self.root, text="Test Image", font=('Arial',30))
        self.label.pack(padx=10,pady=30)

        self.image = Image.open('test_image.jpg')                           #load image
        new_size = (300,300)                                    
        self.image = self.image.resize(new_size, Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)                         #convert image
        self.image_label = tk.Label(self.root, image=self.photo)            #create label for photo 
        self.image_label.pack()                                             #pack

        self.button1 = tk.Button(text="import image")
        self.button1.pack()



        self.root.mainloop() #starts the loop for the program to start
    

    
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit"):
            self.root.destroy()


MyGUI()




#todo;
#-make user upload photo
#-print rgb values of a single pixel
#
#
#
#