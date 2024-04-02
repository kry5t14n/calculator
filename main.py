import interface
from database import create


def main():
    create.create_database()
    interface.App('Calculator', (280, 380))


if __name__ == '__main__':
    main()
