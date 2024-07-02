# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:53:49 2024

@author: HARSHITHA
"""

import tkinter as tk
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        
        self.buttons = []
        self.numbers = list(range(1, 9)) * 2  # Pairs of numbers from 1 to 8
        random.shuffle(self.numbers)
        self.flipped = []
        self.start_time = time.time()
        self.best_time = None
        self.completed_pairs = 0
        
        self.timer_label = tk.Label(self.root, text="Time: 0.0s", font=("Helvetica", 16))
        self.timer_label.grid(row=0, column=0, columnspan=4)
        
        self.create_widgets()
        self.update_timer()
        
    def create_widgets(self):
        colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#c2f0c2", "#ff6666"]
        random.shuffle(colors)
        
        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.root, text="", width=6, height=3, 
                                   bg=random.choice(colors), 
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i + 1, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
    
    def on_button_click(self, i, j):
        if len(self.flipped) < 2 and self.buttons[i][j]["text"] == "":
            self.buttons[i][j]["text"] = str(self.numbers[i*4 + j])
            self.flipped.append((i, j))
            if len(self.flipped) == 2:
                self.root.after(1000, self.check_match)
    
    def check_match(self):
        (i1, j1), (i2, j2) = self.flipped
        if self.numbers[i1*4 + j1] == self.numbers[i2*4 + j2]:
            self.completed_pairs += 1
            if self.completed_pairs == 8:
                self.end_game()
        else:
            self.buttons[i1][j1]["text"] = ""
            self.buttons[i2][j2]["text"] = ""
        self.flipped = []
        
    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        self.timer_label.config(text=f"Time: {elapsed_time:.1f}s")
        self.root.after(100, self.update_timer)
    
    def end_game(self):
        elapsed_time = time.time() - self.start_time
        if self.best_time is None or elapsed_time < self.best_time:
            self.best_time = elapsed_time
            best_time_message = "New best time!"
        else:
            best_time_message = f"Best time: {self.best_time:.1f}s"
        
        tk.messagebox.showinfo("Congratulations!", f"You have completed the game in {elapsed_time:.1f} seconds!\n{best_time_message}")
        self.reset_game()
        
    def reset_game(self):
        self.flipped = []
        self.completed_pairs = 0
        self.numbers = list(range(1, 9)) * 2
        random.shuffle(self.numbers)
        for row in self.buttons:
            for button in row:
                button["text"] = ""
        self.start_time = time.time()
        
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
