import tkinter as tk


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, width=1280, height=720, background="#eee")
        self.start_button = tk.Button(text = 'Start Now', width = 25, command = self.new_window, padx = 20, pady = 20)
        self.end_button = tk.Button(text = 'Exit', width = 25, command = self.close_windows, padx = 20, pady = 20)
        self.start_button.place(in_=self.frame, anchor="c", relx=.5, rely=.4)
        self.end_button.place(in_=self.frame, anchor="c", relx=.5, rely=.55)
        self.frame.pack(fill="both", expand=True)
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
    def close_windows(self):
        self.master.destroy()

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()


# root=tk.Tk()

# entry_frame = tk.Frame(width=1280, height=720, background="#eee")
# entry_frame.pack(fill="both", expand=True)



# f2.place(in_=f1, anchor="c", relx=.5, rely=.5)
# f2 = tk.Frame(width=100, height=100, background="blue")

# root.mainloop()