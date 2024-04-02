def insert_fonts_data(conn) -> None:
    conn.execute('''
                INSERT INTO FONTS (ID, NAME, SIZE) \
                VALUES (1, 'Arial', 64)
            ''')

    conn.execute('''
                INSERT INTO FONTS (ID, NAME, SIZE) \
                VALUES (2, 'Arial', 32)
            ''')

    conn.execute('''
                INSERT INTO FONTS (ID, NAME, SIZE) \
                VALUES (3, 'Arial', 16)
            ''')

    conn.execute('''
                INSERT INTO FONTS (ID, NAME, SIZE) \
                VALUES (4, 'Arial', 8)
            ''')


def insert_colors_data(conn) -> None:
    conn.execute('''
            INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (1, 'Dark3', '#0D1B2A')
        ''')

    conn.execute('''
            INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (2, 'Dark2', '#1B263B')
        ''')

    conn.execute('''
            INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (3, 'Dark1', '#415A77')
        ''')

    conn.execute('''
            INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (4, 'Light1', '#778DA9')
        ''')

    conn.execute('''
            INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (5, 'Light2', '#E0E1DD')
        ''')