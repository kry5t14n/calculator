def insert_fonts_data(conn) -> None:
    conn.execute('''INSERT INTO FONTS (ID, NAME, SIZE) \
                VALUES (1, 'Arial', 64)''')

    conn.execute('''INSERT INTO FONTS (ID, NAME, SIZE) \
                VALUES (2, 'Arial', 32)''')

    conn.execute('''INSERT INTO FONTS (ID, NAME, SIZE) \
                VALUES (3, 'Arial', 16)''')

    conn.execute('''INSERT INTO FONTS (ID, NAME, SIZE) \
                VALUES (4, 'Arial', 8)''')


def insert_colors_data(conn) -> None:
    conn.execute('''INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (1, 'Dark3', '#212529')''')

    conn.execute('''INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (2, 'Dark2', '#343A40')''')

    conn.execute('''INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (3, 'Dark1', '#6C757D')''')

    conn.execute('''INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (4, 'Light1', '#DEE2E6')''')

    conn.execute('''INSERT INTO COLORS (ID, NAME, CODE) \
            VALUES (5, 'Light2', '#F8F9FA')''')
