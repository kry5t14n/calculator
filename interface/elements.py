import tkinter as tk
from database import getters
from functionality.buttons import *
from functools import partial


class Label(tk.Label):
    def __init__(self, parent, position: tuple,
                 text: str, font: tuple) -> None:

        # Get colors and fonts from the database
        self.colors = getters.get_data('COLORS')
        self.fonts = getters.get_data('FONTS')

        # Create and place a Label
        super().__init__(parent)
        self.grid(
            row=position[0],
            column=position[1],
            sticky="e",
            padx=10
        )

        # Label Styles
        self['text'] = text
        self['font'] = font
        self['fg'] = self.colors['Light2']
        self['bg'] = self.colors['Dark3']


class Button(tk.Button):
    def __init__(self, parent, position: tuple,
                 text: str, display_section,
                 btn_type: str) -> None:

        self.display_section = display_section
        self.btn_type = btn_type

        # Get colors and fonts from the database
        self.colors = getters.get_data('COLORS')
        self.fonts = getters.get_data('FONTS')

        # Create and place a Button
        super().__init__(parent)
        self.grid(
            row=position[0],
            column=position[1],
            sticky='nsew'
        )

        # Button styles
        self['text'] = text
        self['font'] = self.fonts[3]
        self['fg'] = self.colors['Light2']
        self['bg'] = self.colors['Dark2']

        # Button command
        if btn_type == 'number':
            self['command'] = partial(number_button,
                                      text, display_section)
        elif btn_type == 'basic_operation':
            self['command'] = partial(basic_operation_button,
                                      text, display_section)
        elif btn_type == 'advanced_operation':
            self['command'] = partial(advanced_operation_button,
                                      text, display_section)
        elif btn_type == 'equal_sign':
            self['command'] = partial(equal_button,
                                      display_section)
        elif btn_type == 'clear':
            self['command'] = partial(clear_button,
                                      text, display_section)
        elif btn_type == 'other':
            self['command'] = partial(other_button,
                                      text, display_section)
