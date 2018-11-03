import tkinter as tk
import tkinter.font as tkFont
from cards import *
import random
from tkinter import messagebox

from PIL import Image, ImageTk


 # Generate a deck of cards from our cards.py library
deck = generate_deck()

sampled_deck = []

# Dict that holds card images and their names
card_images = {}

# Loading all images to a dictionary
for card in deck:
    image = Image.open("resources/images/" + card.getNameForImage() + ".png")
    image = image.resize((70, 100), Image.ANTIALIAS)
    card_images.update({card.getNameForImage() : image})

class CardShuffler:
    root = tk.Tk()
    card_frame = None
    card_number_spinner = None

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
        self.card_frame = tk.Frame(main_frame, height = 800, width = 900, bg = "#eee", borderwidth=2)
       
        # Display all 52 cards
        self.display_card_images(self.card_frame, deck)

        shuffle_button = tk.Button(text="Shuffle Deck", command=lambda: self.shuffle_cards(self.card_frame, main_frame));
        shuffle_button.place(in_=main_frame, anchor="c", x=1000, y=50)

        # Creating and setting the default value of the sample spinbox
        spinner_def_value = tk.StringVar(self.root)
        spinner_def_value.set("52")
        self.card_number_spinner = tk.Spinbox(main_frame, width = 10, from_=5, to=52, textvariable=spinner_def_value)
        self.card_number_spinner.place(in_=main_frame, anchor="c", x=1150, y=50)

        self.card_frame.pack(side="top", anchor="w")
        main_frame.pack()
        main_frame.pack_propagate(0)

    def shuffle_cards(self, frame, main_frame):
        frame.destroy();
        new_frame = tk.Frame(main_frame, height = 800, width = 900, bg = "#eee", borderwidth=2)
        
        # Shufle the deck
        random.shuffle(deck)

        # Pick a sample of the deck, based on the spinner value (5 to 52) cards
        sample_size = 52
        if self.card_number_spinner.get().isdigit() == False:
            messagebox.showerror("Sample Error", "Card sample size is invalid, 52 was used.")
        elif (int(self.card_number_spinner.get()) < 5) or (int(self.card_number_spinner.get()) > 52):
            messagebox.showerror("Sample Error", "Card sample size is invalid, 52 was used.")
        else:
            sample_size = int(self.card_number_spinner.get())

        sampled_deck = random.sample(deck, sample_size)

        self.display_card_images(new_frame, sampled_deck)        

        new_frame.pack(side="top", anchor="w")
        self.card_frame = new_frame

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
    