from decimal import Decimal
import math


def number_button(text: str, display_section) -> None:

    if display_section.history and display_section.history[-1] == '=':
        display_section.history = [text]
        display_section.display = ''

    if (display_section.display != '0'
            and (display_section.display.isnumeric()
                 or display_section.display[-1] == '.')):
        display_section.display += text
    else:
        display_section.display = text

    if (display_section.history
            and len(display_section.history) != 2):
        display_section.history[-1] = display_section.display
    else:
        display_section.history.append(display_section.display)

    # Give history property a list as an argument
    # To display its value
    display_section.history = display_section.history

    # ONLY FOR TESTING
    print('NUMBER')
    print(display_section.history)
    print(display_section.display)


def basic_operation_button(text: str, display_section) -> None:

    if display_section.history:
        if display_section.history[-1][-1] == '.':
            display_section.history[-1] = str(int(
                float(display_section.history[-1])))
        if len(display_section.history) == 1:
            display_section.history.append(text)
        elif len(display_section.history) == 2:
            display_section.history[-1] = text
        else:
            result = get_result(display_section.history[1],
                                display_section.history)
            if float(result).is_integer():
                result = str(int(float(result)))
            display_section.history = [result, text]

        display_section.display = '0'

        # Give history property a list as an argument
        # To display its value
        display_section.history = display_section.history

        # ONLY FOR TESTING
        print('BASIC_OPERATION')
        print(display_section.history)
        print(display_section.display)


def advanced_operation_button(text: str, display_section) -> None:

    check_decimals = False

    if display_section.history and display_section.history[-1] == '=':
        display_section.history = [display_section.display]

    if (display_section.history
            and display_section.history[-1][-1] == '.'):
        display_section.history[-1] = str(int(
            float(display_section.history[-1])))

    if len(display_section.history) in [1, 3]:
        if text == '%':
            if len(display_section.history) == 1:
                display_section.history = ['0']
            else:
                display_section.history[-1] = str(
                    Decimal(display_section.history[0])
                    * Decimal(display_section.history[-1])
                    * Decimal('0.01'))
                check_decimals = True
        elif text == '¹⁄ₓ':
            if display_section.history[-1] == '0':
                display_section.history = ['0']
            else:
                display_section.history[-1] = str(
                    1 / Decimal(display_section.history[-1]))
                check_decimals = True
        elif text == 'x²':
            display_section.history[-1] = str(
                Decimal(display_section.history[-1]) ** 2)
            check_decimals = True
        elif text == '√x':
            if float(display_section.history[-1]) >= 0:
                display_section.history[-1] = str(
                    math.sqrt(Decimal(display_section.history[-1])))
                check_decimals = True
            else:
                display_section.history = ['0']

    elif len(display_section.history) == 2:
        if text == '%':
            display_section.history.append(str(
                Decimal(display_section.history[0])
                ** 2 * Decimal('0.01')))
            check_decimals = True
        elif text == '¹⁄ₓ':
            if display_section.history[0] == '0':
                display_section.history = ['0']
            else:
                display_section.history.append(str(
                    1 / Decimal(display_section.history[0])))
                check_decimals = True
        elif text == 'x²':
            display_section.history.append(str(
                Decimal(display_section.history[0]) ** 2))
            check_decimals = True
        elif text == '√x':
            if float(display_section.history[0]) >= 0:
                display_section.history.append(str(
                    math.sqrt(Decimal(display_section.history[0]))))
                check_decimals = True
            else:
                display_section.history = ['0']

    if check_decimals:
        if float(display_section.history[-1]).is_integer():
            display_section.history[-1] = str(
                int(float(display_section.history[-1])))

    if display_section.history:
        display_section.history = display_section.history
        display_section.display = display_section.history[-1]


def equal_button(display_section) -> None:

    if (display_section.history
            and display_section.history[-1][-1] == '.'):
        display_section.history[-1] = str(int(
            float(display_section.history[-1])))

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
        print(display_section.history)
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

    print('OTHER')

    if display_section.history and display_section.history[-1] == '=':
        display_section.history = [display_section.display]

    number = True if (display_section.history and
                      (display_section.history[-1][-1].isnumeric()
                       or display_section.history[-1][-1] == '.')) \
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


def get_result(mode: str, elements: list) -> str:

    if mode == '/':
        result = Decimal(elements[0]) / Decimal(elements[2])
    elif mode == '*':
        result = Decimal(elements[0]) * Decimal(elements[2])
    elif mode == '-':
        result = Decimal(elements[0]) - Decimal(elements[2])
    elif mode == '+':
        result = Decimal(elements[0]) + Decimal(elements[2])
    else:
        return 'Wrong Character'

    return str(result)
