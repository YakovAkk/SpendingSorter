import sqlite3
import os

class AppDbContext:
    def __init__(self, folder_name="SpendingSorterData", db_name="SpendingSorter.db"):
        base_dir = os.getcwd()
        self.folder_path = os.path.join(base_dir, folder_name)

        os.makedirs(self.folder_path, exist_ok=True)

        self.db_path = os.path.join(self.folder_path, db_name)
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        print(f"Database connected at {self.db_path}.")

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Database connection closed.")

    def execute_query(self, query, params=()):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()

