import tkinter as tk
import interface
from database import getters
# from decimal import *


class App(tk.Tk):
    def __init__(self, title: str, size: tuple) -> None:

        # Get colors from the database
        colors = getters.get_data('COLORS')

        # Main setup and styling
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        self.rowconfigure([0, 1], weight=1)
        self.columnconfigure(0, weight=1)
        self['bg'] = colors['Dark3']

        # Top section
        display_section = interface.Top(self)
        interface.Bottom(self, display_section)

        # Run App loop
        self.mainloop()


if __name__ == '__main__':
    App('Calculator', (280, 380))
