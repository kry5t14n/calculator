import interface
from database.create import create_database


def main():
    create_database()
    interface.App('Calculator', (280, 380))


if __name__ == '__main__':
    main()
