import pyodbc

class DBSave:

    def __init__(self, db_name='newsfeed.db'):
        self.db_name = db_name

    def __enter__(self):
        self.conn = pyodbc.connect(f"DRIVER={{SQLite3 ODBC Driver}};Direct=True;Database={self.db_name};String Types=Unicode")
        self.cursor = self.conn.cursor()
        self.create_tables()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            text TEXT,
            city TEXT,
            date DATE
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS ads (
            text TEXT,
            exp_date DATE
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS forecasts (
            text TEXT,
            rating INTEGER,
            city TEXT,
            date DATE
        )
        ''')
        self.conn.commit()

    def insert_record(self, table_name, **kwargs):
        #Duplicate check
        conditions = [f"{key} = ?" for key in kwargs.keys()]
        condition_str = " AND ".join(conditions)
        values = tuple(kwargs.values())
        select_sql = f"SELECT * FROM {table_name} WHERE {condition_str}"
        self.cursor.execute(select_sql, values)
        if self.cursor.fetchone():
            print("Record already exists")
        else:
            columns = ', '.join(kwargs.keys())
            placeholders = ', '.join('?' for _ in kwargs)
            insert_sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(insert_sql, values)
            self.conn.commit()
