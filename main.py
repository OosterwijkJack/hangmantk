import tkinter as tk
from tkinter import font
import logic as lg
from art import HANGMANPICS


class App:

    def __init__(self, parent):
        self.window = parent
        self.window.title("Hang Man")
        self.window.geometry("800x600")
        self.window.protocol("WM_DELETE_WINDOW", self.window.quit)
        self.logic = lg.Logic(4)

        self.TitleLabel = tk.Label(self.window, text="Hangman", font=("Courier", 25))
        self.ProgressLabel = tk.Label(self.window, text=' '.join(self.logic.progress_list), font=("Courier", 40))
        self.HangManLabel = tk.Label(self.window, text=HANGMANPICS[0], font=("Courier", 25))
        self.TextBox = tk.Text(self.window, font=("Courier", 12), height=1, width=10)
        self.TextBox.bind('<Return>', self.input_handler)
        self.TextBoxInfo = tk.Label(self.window, text="Enter Guess: ", font=("Courier", 12))

        self.LostText = tk.Label(self.window, text=f"You Lose! word was {self.logic.word}", font=("Courier", 30,), foreground='red')
        self.WinText = tk.Label(self.window, text=f"You Win!", font=("Courier", 50), foreground='green')

        self.draw_window()

    def draw_window(self):
        self.TitleLabel.pack()
        self.ProgressLabel.place(relx=0.5,rely=0.75, anchor=tk.CENTER)
        self.HangManLabel.place(relx=0.475, rely=0.4, anchor=tk.CENTER)
        self.TextBox.place(relx=0.55, rely=0.9, anchor=tk.CENTER)
        self.TextBoxInfo.place(relx=0.4, rely=0.9, anchor=tk.CENTER)

    def update_window(self):
        self.ProgressLabel['text'] = ' '.join(self.logic.progress_list)
        self.HangManLabel['text'] = HANGMANPICS[self.logic.tries]
        self.TextBox.delete('1.0', tk.END)

        if "_" not in self.logic.progress_list:
            self.WinText.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.TextBox.destroy()
            self.TextBoxInfo.destroy()

        if self.logic.tries >= 6:
            self.LostText.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.TextBox.destroy()
            self.TextBoxInfo.destroy()

    def input_handler(self, param: tk.Event):
        contents = self.TextBox.get(1.0, tk.END).lower().strip()

        if len(contents) > 1 or len(contents) <= 0:
            print("Invalid input!")
            self.update_window()
            return

        self.logic.letter_in_word(contents)
        self.update_window()



root = tk.Tk()

window1 = App(root)

root.mainloop()
