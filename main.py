import tkinter as tk
import tkinter.font as tkFont
from cards import *

from PIL import Image, ImageTk


 # Generate a deck of cards from our cards.py library
deck = generate_deck()

# Dict that holds card images and their names
card_images = {}

# Loading all images to a dictionary
for card in deck:
    image = Image.open("resources/images/" + card.getNameForImage() + ".png")
    image = image.resize((70, 100), Image.ANTIALIAS)
    card_images.update({card.getNameForImage() : image})

class CardShuffler:
    root = tk.Tk()

    def __init__(self):
    
        self.root.resizable(False, False) # Prevent root from being resizable
        self.root.iconbitmap("resources/cards_icon.ico")
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
        main_frame = tk.Frame(self.master, width=1280, height=720, background="#ccc")
        card_frame = tk.Frame(main_frame, height = 800, width = 900, bg = "#eee", borderwidth=2)
       
        # x_add = 10
        # y_add = 10
        # y_counter = 0
        # for card in deck:
        #     y_counter += 1
        #     card_image = ImageTk.PhotoImage(card_images[card.getNameForImage()])
        #     card_image_container = tk.Label(image=card_image)
        #     card_image_container.image = card_image

        #     card_image_container.place(in_=card_frame, x=x_add % 800, y=y_add)
        #     x_add += 80
        #     y_add += (110 if y_counter % 10 == 0 else 0)
        self.display_card_images(card_frame, deck)
        card_frame.pack(side="top", anchor="w")
        main_frame.pack()
        main_frame.pack_propagate(0)


        
    def close_windows(self):
        self.master.destroy()

    def display_card_images(self, frame, deck):
        x_add = 10
        y_add = 10
        y_counter = 0
        for card in deck:
            y_counter += 1
            card_image = ImageTk.PhotoImage(card_images[card.getNameForImage()])
            card_image_container = tk.Label(image=card_image)
            card_image_container.image = card_image

            card_image_container.place(in_=frame, x=x_add % 800, y=y_add)
            x_add += 80
            y_add += (110 if y_counter % 10 == 0 else 0)



CardShuffler().root.mainloop()
    