# region [IMPORTS]

from sqlite3 import Connection, Cursor, connect

# endregion

conn: Connection = connect('data.db')
cur: Cursor = conn.cursor()

# region [CREATE TABLES]

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS passwords(
        name TEXT NOT NULL,
        login TEXT NOT NULL,
        passwd TEXT NOT NULL
    )
    """
)

# endregion


def insert(name: str = '', login: str = '', passwd: str = '') -> None:
    try:
        cur.execute(
            f"""
        INSERT INTO passwords (name, login, passwd) VALUES ('{name}', '{login}', '{passwd}')
        """
        )

    except:
        print('An error ocurred while trying to register password')

    else:
        print('Your password was registered successfully')
        conn.commit()


def select_all() -> list:
    result: list = []

    try:
        result = cur.execute(
            f"""
            SELECT name FROM passwords ORDER BY 1 DESC
            """
        ).fetchall()
    except:
        print('An error ocurred trying to retrieve the passwords')

    if result != []:
        return result
    else:
        return ['None']


def select_especific(name: str) -> tuple:
    result: tuple = ()

    try:
        result = cur.execute(
            f"""
            SELECT login, passwd FROM passwords WHERE name = '{name}'
            """
        ).fetchone()

    except:
        print('An error ocurred trying to retrieve password')

    return result
