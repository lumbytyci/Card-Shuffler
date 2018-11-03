import tkinter as tk
import tkinter.font as tkFont




class CardShuffler:
    root = tk.Tk()

    def __init__(self):
    
        main_menu_fonts = tkFont.Font(size=25, family="Arial Bold")

        self.master = self.root
        self.root.title("Random Card Shuffler and Picker")
        self.frame = tk.Frame(self.master, width=1280, height=720, background="#eee")
       
        self.start_button = tk.Button(fg="#0080FF", font=main_menu_fonts, borderwidth = 0, text = 'START', width = 20, bg="#aaa", command = lambda: self.start_game(self.frame), padx = 5, pady = 5)
        self.end_button = tk.Button(fg="#4C516D", font=main_menu_fonts, borderwidth = 0, text = 'EXIT', width = 20, bg="#aaa", command = self.close_windows, padx = 5, pady = 5)
        

        self.start_button.place(in_=self.frame, anchor="c", relx=.5, rely=.4)
        self.end_button.place(in_=self.frame, anchor="c", relx=.5, rely=.55)
        self.frame.pack(fill="both", expand=True)
        

    def start_game(self, frame):
        self.frame.destroy()

        main_frame = tk.Frame(self.master, width=1280, height=720, background="#eee")
        main_frame.pack(fill="both", expand=True)
        
        
    def close_windows(self):
        self.master.destroy()



CardShuffler().root.mainloop()
    