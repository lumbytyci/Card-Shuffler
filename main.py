import tkinter as tk
import tkinter.font as tkFont
from cards import *
import random
from tkinter import messagebox
from tkinter import ttk

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageTk


 # Generate a deck of cards from our cards.py library
deck = generate_deck()

# Set sample deck initially to deck
sampled_deck = deck

# Dict that holds card images and their names
card_images = {}



# Loading all images to a dictionary
for card in deck:
    image = Image.open("resources/images/" + card.getNameForImage() + ".png")
    image = image.resize((70, 100), Image.ANTIALIAS)
    card_images.update({card.getNameForImage() : image})

# Loading the default card image (backside)
default_card_image = Image.open("resources/images/red_back.png")
default_card_image = default_card_image.resize((70, 100), Image.ANTIALIAS)

class CardShuffler:
    root = tk.Tk()
    sampled_deck = deck
    card_frame = None
    card_number_spinner = None
    show_cards = True
    main_frame = None
    cmb_card_value = None
    cmb_card_symbol = None
    picking_counter_label = None
    picking_counter_val_label = None

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
        self.main_frame = tk.Frame(self.master, width=1280, height=720, background="#ccc")
        self.card_frame = tk.Frame(self.main_frame, height = 800, width = 900, bg = "#eee", borderwidth=2)
       
        # Display all 52 cards
        self.display_card_images(self.card_frame, deck, self.show_cards)


        shuffle_button = tk.Button(text="Shuffle Deck",width = 29, command=lambda: self.shuffle_cards(self.card_frame, self.main_frame));
        shuffle_button.place(in_=self.main_frame, anchor="c", x=1078, y=100)

        hide_button = tk.Button(text="Show/Hide Cards",width = 29, command=lambda: self.toggle_show_cards(self.card_frame, self.main_frame));
        hide_button.place(in_=self.main_frame, anchor="c", x=1078, y=145)

        pick_random_card_btn = tk.Button(text="Pick Random Card",width = 29, command=self.pick_random_card);
        pick_random_card_btn.place(in_=self.main_frame, anchor="c", x=1078, y=200)

        # Sample size label
        sample_label = tk.Label(text="Sample size: ")   
        sample_label.place(in_=self.main_frame, anchor="c", x=1000, y=50)

        # Sample size label
        sample_label = tk.Label(text="Choose a card: ")   
        sample_label.place(in_=self.main_frame, anchor="c", x=1010, y=420)

        # How many times did it pick randomly label
        main_menu_fonts = tkFont.Font(size=15, family="Arial Bold")
        self.picking_counter_label = tk.Label(text="Draw Counter: ", font=main_menu_fonts, bg="#ccc", fg="#222")   
        self.picking_counter_label.place(in_=self.main_frame, anchor="c", x=1045, y=620)

        # How many times did it pick randomly label
        self.picking_counter_val_label = tk.Label(text="", font=main_menu_fonts, bg="#ccc", fg="#222")   
        self.picking_counter_val_label.place(in_=self.main_frame, anchor="c", x=1185, y=620)

        self.cmb_card_value = ttk.Combobox(state='readonly', width = 10, values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        self.cmb_card_value.bind("<<ComboboxSelected>>", self.cmb_changed_event)
        self.cmb_card_value.grid(column=0, row=1)
        self.cmb_card_value.current(1)
        self.cmb_card_value.place(in_=self.main_frame, anchor="c", x=1010, y=460)

        self.cmb_card_symbol = ttk.Combobox(state='readonly', width = 10, values=["Heart", "Diamond", "Spade", "Club"])
        self.cmb_card_symbol.bind("<<ComboboxSelected>>", self.cmb_changed_event)
        self.cmb_card_symbol.grid(column=0, row=1)
        self.cmb_card_symbol.current(1)
        self.cmb_card_symbol.place(in_=self.main_frame, anchor="c", x=1145, y=460)
        
        search_for_card_btn = tk.Button(text="Search for Card",width = 29, command = self.search_for_card);
        search_for_card_btn.place(in_=self.main_frame, anchor="c", x=1078, y=500)

        search_for_card_experiment_btn = tk.Button(text="Search for Card Experiment",width = 29, command = self.search_for_card_experiment);
        search_for_card_experiment_btn.place(in_=self.main_frame, anchor="c", x=1078, y=550)

        # Creating and setting the default value of the sample spinbox
        spinner_def_value = tk.StringVar(self.root)
        spinner_def_value.set("52")
        self.card_number_spinner = tk.Spinbox(self.main_frame, width = 10, from_=5, to=52, textvariable=spinner_def_value)
        self.card_number_spinner.place(in_=self.main_frame, anchor="c", x=1150, y=50)

        self.card_frame.pack(side="top", anchor="w")
        self.main_frame.pack()
        self.main_frame.pack_propagate(0)

    def cmb_changed_event(self, eventObject):
        card_name = self.get_card_name_from_combobox()
        selected_card = None

        for card in deck:
            if card.getNameForImage() == card_name:
                selected_card = card
                break

        self.display_random_card(selected_card)


    def get_card_name_from_combobox(self):
        card_value = self.cmb_card_value.get()
        card_symbol = self.cmb_card_symbol.get()

        full_card_name = card_value + card_symbol
        card_name = ""
        if full_card_name[1].isdigit():
            card_name = full_card_name[0:3]
        else:
            card_name = full_card_name[0:2]

        return card_name    

    def search_for_card_experiment(self):

        # Get Card name from the combo box selection
        card_name = self.get_card_name_from_combobox()


        # Check if card is available in the sampled deck
        if not card_name in (card.getNameForImage() for card in self.sampled_deck):
             messagebox.showerror("Card Choice Invalid", "The chosen card is not available in the sampled deck!")
             return

        results = []
        # Search sampled deck for card
        for i in range (1,1001):
            search_counter = 1
            while random.choice(self.sampled_deck).getNameForImage() != card_name:
                search_counter += 1
            results.append(search_counter)

        
        plt.scatter(range(1,1001), results)
        plt.show()



    def search_for_card(self):
        
        # Get Card name from the combo box selection
        card_name = self.get_card_name_from_combobox()


        # Check if card is available in the sampled deck
        if not card_name in (card.getNameForImage() for card in self.sampled_deck):
             messagebox.showerror("Card Choice Invalid", "The chosen card is not available in the sampled deck!")
             return


        # Search sampled deck for card
        search_counter = 1

        while random.choice(self.sampled_deck).getNameForImage() != card_name:
            search_counter += 1

        self.picking_counter_val_label["text"] = str(search_counter)




    def display_random_card(self, card):
        
        card = Image.open("resources/images/" + card.getNameForImage() + ".png")
        card = card.resize((110, 160), Image.ANTIALIAS)
        card_image = ImageTk.PhotoImage(card)
        card_image_container = tk.Label(image=card_image, borderwidth=0, bg="#ccc")
        card_image_container.image = card_image
        card_image_container.place(in_=self.main_frame, x=1020, y=230)
        

    def pick_random_card(self):
        random_card = random.choice(self.sampled_deck)
        self.display_random_card(random_card)


    def toggle_show_cards(self, frame, main_frame):
        frame.destroy();
        new_frame = tk.Frame(main_frame, height = 800, width = 900, bg = "#eee", borderwidth=2)
        
        #Toggle show/hide by inverting the boolean
        self.show_cards = not self.show_cards
        
        self.display_card_images(new_frame, self.sampled_deck, self.show_cards)  
        new_frame.pack(side="top", anchor="w")
        self.card_frame = new_frame

    def shuffle_cards(self, frame, main_frame):
        frame.destroy();
        new_frame = tk.Frame(main_frame, height = 800, width = 900, bg = "#eee", borderwidth=2)
        
        # Shufle the deck
        random.shuffle(deck)

        # Pick a sample of the deck, based on the spinner value (5 to 52) cards
        sample_size = 52
        if self.card_number_spinner.get().isdigit() == False:
            messagebox.showerror("Sample Error", "Card sample size is invalid, 52 was used.")
        elif (int(self.card_number_spinner.get()) < 1) or (int(self.card_number_spinner.get()) > 52):
            messagebox.showerror("Sample Error", "Card sample size is invalid, 52 was used.")
        else:
            sample_size = int(self.card_number_spinner.get())
        self.sampled_deck = random.sample(deck, sample_size)


        self.display_card_images(new_frame, self.sampled_deck, self.show_cards)        

        new_frame.pack(side="top", anchor="w")
        self.card_frame = new_frame

    def close_windows(self):
        self.master.destroy()

    def display_card_images(self, frame, deck, showCards):
        x_add = 10
        y_add = 10
        y_counter = 0
        for card in deck:
            y_counter += 1
            if showCards == True:
                card_image = ImageTk.PhotoImage(card_images[card.getNameForImage()])
            else:
                card_image = ImageTk.PhotoImage(default_card_image)

            card_image_container = tk.Label(image=card_image)
            card_image_container.image = card_image
            card_image_container.place(in_=frame, x=x_add % 800, y=y_add)
            x_add += 80
            y_add += (110 if y_counter % 10 == 0 else 0)
        
CardShuffler().root.mainloop()
    