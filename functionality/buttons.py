from decimal import Decimal


def number_button(text: str, display_section) -> None:

    if (display_section.history
            and display_section.history[-1] == '='):
        display_section.history = [text]
        display_section.display = ''

    if (display_section.display != '0'
            and display_section.display.isnumeric()):
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
        if len(display_section.history) == 1:
            display_section.history.append(text)
        elif len(display_section.history) == 2:
            display_section.history[-1] = text
        else:
            result = get_result(display_section.history[1],
                                display_section.history)
            display_section.history = [result, text]

        display_section.display = '0'

        # Give history property a list as an argument
        # To display its value
        display_section.history = display_section.history

        # ONLY FOR TESTING
        print('BASIC_OPERATION')
        print(display_section.history)
        print(display_section.display)


def equal_button(display_section):

    print(f'HISTORY LENGTH: {len(display_section.history)}')

    if len(display_section.history) == 3:
        result = get_result(display_section.history[1],
                            display_section.history)
        display_section.history.append('=')
        display_section.history = display_section.history
    else:
        if len(display_section.history) == 2:
            display_section.history.append(display_section.history[0])
            result = get_result(display_section.history[1],
                                display_section.history)
        else:
            result = '0'

        display_section.history = [result]

    print(display_section.history)
    display_section.display = result
    # display_section.history = [result]


def clear_button(text: str, display_section) -> None:

    if text == 'CE':
        display_section.display = '0'
        if len(display_section.history) in [1, 3]:
            display_section.history[-1] = '0'

    elif text == 'C':
        display_section.display = '0'
        display_section.history = []

    elif text == '<-':
        if len(display_section.display) != 1:
            display_section.display = display_section.display[:-1]
            if len(display_section.history) in [1, 3]:
                display_section.history[-1] = display_section.display
        else:
            display_section.display = '0'

    display_section.history = display_section.history


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
