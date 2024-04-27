import sqlite3


def test_if_table_is_created():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    get_tables = cur.execute('''
                SELECT name FROM sqlite_master WHERE type='table'
            ''').fetchall()
    conn.close()

    tables = [table[0] for table in get_tables]

    assert 'COLORS' in tables
