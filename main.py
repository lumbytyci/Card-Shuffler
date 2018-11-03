import tkinter as tk
import tkinter.font as tkFont

from PIL import Image, ImageTk

class CardShuffler:
    root = tk.Tk()

    def __init__(self):
    
        #custom font created for the main menu buttons
        main_menu_fonts = tkFont.Font(size=25, family="Arial Bold")

        self.master = self.root
        self.root.title("Random Card Shuffler and Picker")
        self.frame = tk.Frame(self.master, width=1280, height=720, background="#eee")

        # Loading the main logo
        main_logo = ImageTk.PhotoImage(Image.open("resources/images/aces.png"))
        main_logo_container = tk.Label(image=main_logo)
        main_logo_container.image = main_logo

        start_button = tk.Button(fg="#fff", font=main_menu_fonts, borderwidth = 0, text = 'START', width = 20, bg="#222", command = lambda: self.start_game(self.frame), padx = 5, pady = 5)
        end_button = tk.Button(fg="#fff", font=main_menu_fonts, borderwidth = 0, text = 'EXIT', width = 20, bg="#222", command = self.close_windows, padx = 5, pady = 5)
        
        main_logo_container.place(in_=self.frame, anchor="c", relx=.6, rely=.3)
        start_button.place(in_=self.frame, anchor="c", relx=.5, rely=.4)
        end_button.place(in_=self.frame, anchor="c", relx=.5, rely=.55)
        self.frame.pack(fill="both", expand=True)
        

    def start_game(self, frame):
        # Destroy the main menu frame and start the game
        self.frame.destroy()
        
        # Creating the new frame where all the content will go
        main_frame = tk.Frame(self.master, width=1280, height=720, background="#eee")
       

       
       
       
       
       
        main_frame.pack(fill="both", expand=True)
        
        
    def close_windows(self):
        self.master.destroy()



CardShuffler().root.mainloop()
    