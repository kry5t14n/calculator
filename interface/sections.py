import tkinter as tk
from database import getters
import interface


class Top(tk.Frame):
    def __init__(self, parent) -> None:

        # Get colors and fonts from the database
        self.colors = getters.get_data('COLORS')
        self.fonts = getters.get_data('FONTS')

        # Create and place the Top section
        super().__init__(parent)
        self['bg'] = self.colors['Dark3']
        self.grid(row=0, column=0, sticky='e')

        # Section properties
        self._display = '0'
        self._history = []

        # Create and place the section labels with grid()
        self.lbl_display = interface.Label(self, (1, 0),
                                           '0', self.fonts[2])
        self.lbl_history = interface.Label(self, (0, 0),
                                           ' '.join(self.history),
                                           self.fonts[3])

    @property
    def display(self) -> str:
        return self._display

    @property
    def history(self) -> list:
        return self._history

    @display.setter
    def display(self, new_value: str) -> None:
        self.lbl_display['text'] = new_value
        self._display = new_value

    @history.setter
    def history(self, new_value) -> None:
        self.lbl_history['text'] = ' '.join(new_value)
        self._history = new_value


class Bottom(tk.Frame):
    def __init__(self, parent, display_section) -> None:

        # Define section of the display
        self.display_section = display_section

        # Get colors from the database
        self.colors = getters.get_data('COLORS')

        # Create and place the Bottom section
        super().__init__(parent)
        self['bg'] = self.colors['Dark3']
        self.grid(row=1, column=0, sticky='nsew')

        # Configure Bottom section
        self.rowconfigure(
            [i for i in range(6)],
            minsize=50,
            weight=1
        )
        self.columnconfigure(
            [i for i in range(4)],
            minsize=70,
            weight=1
        )

        # Create top section layout and place it with grid()
        self.create_layout()

    def create_layout(self) -> None:

        # Number Buttons
        button_text = 9

        for i in range(3):
            for j in range(3):
                interface.Button(self, (i+2, 2-j), str(button_text),
                                 self.display_section, 'number')
                button_text -= 1

        interface.Button(self, (5, 1), str(button_text),
                         self.display_section, 'number')

        # Basic operations Buttons
        interface.Button(self, (1, 3), '/',
                         self.display_section, 'basic_operation')
        interface.Button(self, (2, 3), '*',
                         self.display_section, 'basic_operation')
        interface.Button(self, (3, 3), '-',
                         self.display_section, 'basic_operation')
        interface.Button(self, (4, 3), '+',
                         self.display_section, 'basic_operation')

        # Advanced operations Buttons
        interface.Button(self, (0, 0), '%',
                         self.display_section, 'advanced_operation')
        interface.Button(self, (1, 0), '¹⁄ₓ',
                         self.display_section, 'advanced_operation')
        interface.Button(self, (1, 1), 'x²',
                         self.display_section, 'advanced_operation')
        interface.Button(self, (1, 2), '√x',
                         self.display_section, 'advanced_operation')

        # Equal sign Button
        interface.Button(self, (5, 3), '=',
                         self.display_section, 'equal_sign')

        # Clear and delete Buttons
        interface.Button(self, (0, 1), 'CE',
                         self.display_section, 'clear')
        interface.Button(self, (0, 2), 'C',
                         self.display_section, 'clear')
        interface.Button(self, (0, 3), '←',
                         self.display_section, 'clear')

        # Other Buttons
        interface.Button(self, (5, 0), '+/-',
                         self.display_section, 'other')
        interface.Button(self, (5, 2), '.',
                         self.display_section, 'other')

        # # This is only a demo layout
        # # It should be changed soon
        # interface.Button(self, (0, 0), '%')
        # interface.Button(self, (0, 1), 'CE')
        # interface.Button(self, (0, 2), 'C')
        # interface.Button(self, (0, 3), '<-')
        # interface.Button(self, (1, 0), '1/x')
        # interface.Button(self, (1, 1), 'x^2')
        # interface.Button(self, (1, 2), 'sqrt(x)')
        # interface.Button(self, (1, 3), '/')
        # interface.Button(self, (2, 0), '7')
        # interface.Button(self, (2, 1), '8')
        # interface.Button(self, (2, 2), '9')
        # interface.Button(self, (2, 3), '*')
        # interface.Button(self, (3, 0), '4')
        # interface.Button(self, (3, 1), '5')
        # interface.Button(self, (3, 2), '6')
        # interface.Button(self, (3, 3), '-')
        # interface.Button(self, (4, 0), '1')
        # interface.Button(self, (4, 1), '2')
        # interface.Button(self, (4, 2), '3')
        # interface.Button(self, (4, 3), '+')
        # interface.Button(self, (5, 0), '+/-')
        # interface.Button(self, (5, 1), '0')
        # interface.Button(self, (5, 2), '.')
        # interface.Button(self, (5, 3), '=')
