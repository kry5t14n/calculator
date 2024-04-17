from functionality.helpers import *
import math


def number_button(text: str, display_section) -> None:

    # Display button text if it's a result of operation
    if display_section.history and display_section.history[-1] == '=':
        display_section.history = [text]
        display_section.display = '0'

    # Update display
    if (display_section.display != '0'
            and is_number(display_section.display[-1])):
        display_section.display += text
    else:
        display_section.display = text

    # Update history
    if (display_section.history
            and len(display_section.history) != 2):
        display_section.history[-1] = display_section.display
    else:
        display_section.history.append(display_section.display)

    display_section.history = display_section.history


def basic_operation_button(text: str, display_section) -> None:

    if display_section.history:

        # Format the last number
        display_section.history[-1] \
            = clear_number(display_section.history[-1])

        # Add or change the operation sign
        if len(display_section.history) == 1:
            display_section.history.append(text)
        elif len(display_section.history) == 2:
            display_section.history[-1] = text
        # Get the result and add the operation sign
        else:
            result = get_result(display_section.history[1],
                                display_section.history)
            if float(result).is_integer():
                result = str(int(float(result)))
            display_section.history = [result, text]

        # Update history and display
        display_section.display = '0'
        display_section.history = display_section.history


def advanced_operation_button(text: str, display_section) -> None:

    if display_section.history:

        # Get the result
        if display_section.history[-1] == '=':
            display_section.history = [display_section.display]

        # Format the last number
        display_section.history[-1] \
            = clear_number(display_section.history[-1])

    if len(display_section.history) in [1, 3]:

        if text == '%':
            if len(display_section.history) == 1:
                display_section.history = ['0']
            else:
                display_section.history[-1] = str(
                    Decimal(display_section.history[0])
                    * Decimal(display_section.history[-1])
                    * Decimal('0.01'))

        elif text == '¹⁄ₓ':
            # Prevent dividing by 0
            if display_section.history[-1] == '0':
                display_section.history = ['0']
            else:
                display_section.history[-1] = str(
                    1 / Decimal(display_section.history[-1]))

        elif text == 'x²':
            display_section.history[-1] = str(
                Decimal(display_section.history[-1]) ** 2)

        elif text == '√x':
            # Get result only if given value >= 0
            if float(display_section.history[-1]) >= 0:
                display_section.history[-1] = str(
                    math.sqrt(Decimal(display_section.history[-1])))
            else:
                display_section.history = ['0']

    elif len(display_section.history) == 2:

        if text == '%':
            display_section.history.append(str(
                Decimal(display_section.history[0])
                ** 2 * Decimal('0.01')))

        elif text == '¹⁄ₓ':
            # Prevent dividing by 0
            if display_section.history[0] == '0':
                display_section.history = ['0']
            else:
                display_section.history.append(str(
                    1 / Decimal(display_section.history[0])))

        elif text == 'x²':
            display_section.history.append(str(
                Decimal(display_section.history[0]) ** 2))

        elif text == '√x':
            # Get result only if given value >= 0
            if float(display_section.history[0]) >= 0:
                display_section.history.append(str(
                    math.sqrt(Decimal(display_section.history[0]))))
            else:
                display_section.history = ['0']

    if display_section.history:

        display_section.history[-1] \
            = clear_number(display_section.history[-1])

        display_section.history = display_section.history
        display_section.display = display_section.history[-1]


def equal_button(display_section) -> None:

    # Format the last number
    if display_section.history:
        display_section.history[-1] \
            = clear_number(display_section.history[-1])

    if '=' not in display_section.history:

        result = '0'

        if len(display_section.history) == 3:
            result = get_result(display_section.history[1],
                                display_section.history)
        elif len(display_section.history) == 2:
            display_section.history.append(display_section.history[0])
            result = get_result(display_section.history[1],
                                display_section.history)
        elif display_section.history:
            result = display_section.history[0]

        if float(result).is_integer():
            result = str(int(float(result)))

        display_section.history.append('=')
        display_section.history = display_section.history
        display_section.display = result


def clear_button(text: str, display_section) -> None:

    if text == 'CE':
        display_section.display = '0'
        if len(display_section.history) in [1, 3]:
            display_section.history[-1] = '0'

    elif text == 'C':
        display_section.display = '0'
        display_section.history = []

    elif text == '←':
        if len(display_section.display) != 1:
            display_section.display = display_section.display[:-1]
            if len(display_section.history) in [1, 3]:
                display_section.history[-1] = display_section.display
        else:
            display_section.display = '0'

    display_section.history = display_section.history


def other_button(text: str, display_section) -> None:

    if display_section.history and display_section.history[-1] == '=':
        display_section.history = [display_section.display]

    number = True if (display_section.history and
                      is_number(display_section.history[-1][-1])) \
        else False

    if number:
        if text == '+/-':
            display_section.history[-1] = str(
                Decimal(display_section.history[-1]) * -1)
        elif text == '.':
            if '.' not in display_section.history[-1]:
                display_section.history[-1] += '.'

        display_section.history = display_section.history
        display_section.display = display_section.history[-1]
