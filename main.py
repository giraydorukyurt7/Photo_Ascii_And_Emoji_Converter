import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Photo Ascii And Emoji Converter")  #title
        self.root.geometry("600x1000")                       #window size
        self.root.iconbitmap(r'images/logo/logo.png')       #icon
        
        #Menubar
        self.menubar = tk.Menu(self.root)                   #creating a menubar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)                        #First menu
        self.filemenu.add_command(label="Open Image", command=self.open_image)
        self.filemenu.add_command(label="CLOSE", command=self.on_closing)       #Filemenu element #1
        self.filemenu.add_separator()                                           #The line between elements
        self.filemenu.add_command(label="CLOSE Without Question", command=exit) #Filemenu element #2
        self.menubar.add_cascade(menu=self.filemenu, label="File")              #add filemenu to menubar  
        self.root.config(menu=self.menubar)

        #Scrollbar
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side = tk.RIGHT, fill =tk.Y)

        # Text for test image   
        self.label = tk.Label(self.root, text="Test Image", font=('Arial',30))
        self.label.pack(padx=10,pady=30)
        # Placeholder for image
        self.image_label = tk.Label(self.root)
        self.image_label.pack()
        # Adding a default image
        self.default_image_path = 'test_image.jpg'
        self.load_image(self.default_image_path)
        self.current_image_path = self.default_image_path #track current image path
        # Button for user to open an image from their computer 
        self.button_import_image = tk.Button(text="Import Image", command=self.open_image)
        self.button_import_image.pack()

        # Text for pixelated image
        self.label = tk.Label(self.root, text="Pixelated Image")
        self.label.pack(padx=10,pady=30)
        # Placeholder for pixelated image
        self.image_label_pixelated = tk.Label(self.root)
        self.image_label_pixelated.pack()
        # Button for pixelating the current image.
        self.button_pixelate_image = tk.Button(text="Pixelate Image", command=self.pixelator)
        self.button_pixelate_image.pack()


        self.root.mainloop() #starts the loop for the program to start
    
    def load_image(self, image_path):
        self.image = Image.open(image_path)
        new_size = (300, 300)
        self.image = self.image.resize(new_size, Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo
        self.current_image = self.image.copy()  # Store the currently opened image
        self.current_image_path = image_path    # Update the current image path
        

    def open_image(self):
        print("Import image button has been clicked.")
        file_path= filedialog.askopenfilename(
            filetypes=[("Image files","*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
        )
        if file_path:
            self.load_image(file_path)
        else:
            self.load_image(self.default_image)
    
    def pixelator(self):
        print("Pixelate Image button has been clicked.")
        pixelated_image         = self.current_image
        self.pixelated_photo    = ImageTk.PhotoImage(pixelated_image)
        self.image_label_pixelated.config(image=self.pixelated_photo)
        self.image_label_pixelated.image = self.pixelated_photo

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit"):
            self.root.destroy()


MyGUI()






#todo;
#-print rgb values of a single pixel
#
#
#
#