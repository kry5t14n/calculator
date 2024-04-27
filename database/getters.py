import sqlite3


def get_data(table_name: str) -> dir:

    # Open connection with database
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    data = f"Table '{table_name}' doesn't exist"

    # Get all the tables names
    tables = cur.execute('''
                SELECT name FROM sqlite_master WHERE type='table'
            ''').fetchall()

    for table in tables:
        if table_name.upper() in table:
            fetched_data = cur.execute(f'''
                        SELECT * FROM {table_name}
                    ''').fetchall()

            # Format fetched data
            if table_name.upper() == 'COLORS':
                data = {}
                for item in fetched_data:
                    data[item[1]] = item[2]

            if table_name.upper() == 'FONTS':
                data = {}
                for item in fetched_data:
                    data[item[0]] = item[1:]

    # Close connection with database
    conn.close()
    return data
