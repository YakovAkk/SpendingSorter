from AppDbContext.db_context import AppDbContext

class SpendingRepository:
    def __init__(self, db_context: AppDbContext):
        self.db_context = db_context

    def init_database_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS Spendings (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            CreatedAt TEXT NOT NULL,
            Amount REAL NOT NULL,
            Type INT NOT NULL,
            Comment TEXT NOT NULL
        )
        """
        with self.db_context.conn:
            cursor = self.db_context.conn.cursor()
            cursor.execute(query)
            self.db_context.conn.commit()
            print("Table 'spendings' initialized.")

    def create_spending(self, created_at, amount, type_of_spending, comment):
        query = """
            INSERT INTO Spendings (CreatedAt, Amount, Type, Comment)
            VALUES (?, ?, ?, ?)
        """
        params = (created_at, amount, type_of_spending.value, comment)
        with self.db_context.conn:
            cursor = self.db_context.conn.cursor()
            cursor.execute(query, params)
            self.db_context.conn.commit()

    def get_all_spendings(self):
        query = "SELECT * FROM Spendings"
        with self.db_context.conn:
            cursor = self.db_context.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            return rows

    def update_spending(self, spending_id, amount=None, type_of_spending=None, comment=None):
        query = f"""
        UPDATE Spendings
        SET Amount = COALESCE({amount}, Amount),
            Type = COALESCE({type_of_spending}, Type),
            Comment = COALESCE({comment}, Comment)
        WHERE id = {spending_id}
        """
        with self.db_context.conn:
            cursor = self.db_context.conn.cursor()
            cursor.execute(query,)
            self.db_context.conn.commit()
            print(f"Spending record with ID {spending_id} updated.")

    def delete_spending(self, spending_id):
        query = f"DELETE FROM spendings WHERE id = {spending_id}"
        with self.db_context.conn:
            cursor = self.db_context.conn.cursor()
            cursor.execute(query)
            self.db_context.conn.commit()
            print(f"Spending record with ID {spending_id} deleted.")