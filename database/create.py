import sqlite3
from database import setters


def create_database() -> None:

    # Open connection with database
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    # Get all tables names
    get_tables = cur.execute('''
            SELECT name FROM sqlite_master WHERE type='table'
        ''').fetchall()

    # Format fetched data
    tables = [table[0] for table in get_tables]

    # Create FONTS table if it doesn't exist
    if 'FONTS' not in tables:
        cur.execute('''
                CREATE TABLE FONTS (
                    ID INTEGER,
                    NAME STRING,
                    SIZE INTEGER
                )
            ''')

        # Add data to the table
        setters.insert_fonts_data(conn)
        conn.commit()

    # Create COLORS table if it doesn't exist
    if 'COLORS' not in tables:
        cur.execute('''
                CREATE TABLE COLORS (
                    ID INTEGER,
                    NAME STRING,
                    CODE STRING
                )
            ''')
        # Add data to the table
        setters.insert_colors_data(conn)
        conn.commit()

    # Close connection with database
    conn.close()
