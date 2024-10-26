from AppDbContext.db_context import AppDbContext
from Models.type_of_spending import TypeOfSpending
from Repositories.spending_repository import SpendingRepository

def main():
    db_context = AppDbContext()
    db_context.connect()
    spending_repo = SpendingRepository(db_context)
    spending_repo.init_database_tables()
    # spending_repo.create_spending("2024-10-26 10:00:00", 150.0, TypeOfSpending.Food, "Lunch with friends")
    spending_repo.get_all_spendings()

if __name__ == '__main__':
    main()