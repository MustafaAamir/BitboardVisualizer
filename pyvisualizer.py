#!/usr/bin/python

import tkinter as tk
from tkinter import font

TEXTCOLOR = "#FBF1C7"
BGCOLOR = "#32302F"
alpha_coords = ["A", "B", "C", "D", "E", "F", "G", "H"]

class BitboardViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bitboard Visualizer")
        self.geometry("700x750")
        self.resizable(False, False)
        self.configure(bg=BGCOLOR)
        self.custom_font = font.Font(family="Monospace", size=12, weight="bold")
        self.label_font = font.Font(family="Monospace", size=12)
        self.bitboard = 0
        self.buttons = []

        self.create_buttons()

        self.dec_label = tk.Label(self, text="0", font = self.custom_font, bg="#32302f", fg="#fbf1c7")
        self.dec_label.pack(pady=5)
        self.hex_label = tk.Label(self, text="0x0", font= self.custom_font, bg="#32302f", fg="#FBF1C7")
        self.hex_label.pack(pady=5)

        self.create_operation_buttons()

    def create_buttons(self):
        frame = tk.Frame(self, bg=BGCOLOR)
        frame.pack()
        for i in range(8):
            row = []
            for j in range(8):
                text = alpha_coords[j] + str(i + 1)
                button = tk.Button(frame, text=text, width=4, height=2, command=lambda r=i, c=j: self.toggle_bit(r, c),
                                   bg=BGCOLOR, fg=TEXTCOLOR, activebackground=TEXTCOLOR, font=self.custom_font, activeforeground=BGCOLOR)
                button.grid(row=i, column=j, padx=2, pady=2)
                row.append(button)
            self.buttons.append(row)

    def toggle_bit(self, row, col):
        index = row * 8 + col
        self.bitboard ^= 1 << index  # Toggle the bit at the given index
        self.update_display()

    def update_display(self):
        for i in range(8):
            for j in range(8):
                index = i * 8 + j
                if self.bitboard & (1 << index):
                    self.buttons[i][j].config(bg=TEXTCOLOR, fg=BGCOLOR)
                else:
                    self.buttons[i][j].config(bg=BGCOLOR, fg=TEXTCOLOR)
        self.dec_label.config(text=str(self.bitboard))
        self.hex_label.config(text=hex(self.bitboard))

    def fill(self):
        self.bitboard = (1 << 64) - 1
        self.update_display()

    def clear(self):
        self.bitboard = 0
        self.update_display()

    def shl(self):
        self.bitboard = (self.bitboard << 1) & ((1 << 64) - 1)
        self.update_display()

    def shr(self):
        self.bitboard = self.bitboard >> 1
        self.update_display()

    def bitwise_not(self):
        self.bitboard = ~self.bitboard & ((1 << 64) - 1)
        self.update_display()

    def create_operation_buttons(self):
        frame = tk.Frame(self)
        frame.pack()

        button_style = {"font": self.custom_font, "bg": BGCOLOR, "activebackground": TEXTCOLOR, "activeforeground": BGCOLOR}
        fill_button = tk.Button(frame, text="Fill", command=self.fill, **button_style, fg="#cc241d")
        fill_button.pack(side=tk.LEFT)

        clear_button = tk.Button(frame, text="Clear", command=self.clear, **button_style, fg="#98971a")
        clear_button.pack(side=tk.LEFT)

        shl_button = tk.Button(frame, text="Lsh", command=self.shl, **button_style, fg="#d79921")
        shl_button.pack(side=tk.LEFT)

        shr_button = tk.Button(frame, text="Rsh", command=self.shr, **button_style, fg="#458588")
        shr_button.pack(side=tk.LEFT)

        not_button = tk.Button(frame, text="Not", command=self.bitwise_not, **button_style, fg="#b12686")
        not_button.pack(side=tk.LEFT)


if __name__ == "__main__":
    app = BitboardViewer()
    app.mainloop()

