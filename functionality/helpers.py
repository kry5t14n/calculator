from decimal import Decimal


def get_result(mode: str, elements: list) -> str:

    if mode == '/':
        if elements[2] != '0':
            result = Decimal(elements[0]) / Decimal(elements[2])
        else:
            result = 'Error'
    elif mode == '*':
        result = Decimal(elements[0]) * Decimal(elements[2])
    elif mode == '-':
        result = Decimal(elements[0]) - Decimal(elements[2])
    elif mode == '+':
        result = Decimal(elements[0]) + Decimal(elements[2])
    else:
        return 'Wrong Character'

    result = clear_number(str(result))

    return result


def is_number(text: str) -> bool:

    chars = [str(i) for i in range(10)]
    chars.append('.')
    if len(text) == 1 and text in chars:
        return True

    return False


def clear_number(number: str) -> str:

    try:
        if number[-1] == '.' or float(number).is_integer():
            return str(int(float(number)))
    except ValueError:
        return number

    return number
