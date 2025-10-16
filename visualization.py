import matplotlib.pyplot as plt
from database.database_manager import get_popular_queries_data

#график популярных запросов
def plot_popular_queries():
    queries, counts = get_popular_queries_data()

    if not queries:
        print("No data available for visualization.")
        return

    plt.figure(figsize=(10, 5))
    plt.barh(queries[::-1], counts[::-1], color="skyblue")  # oтображаем в обратном порядке, чтобы частые запросы были наверху
    plt.xlabel("Number of queries")
    plt.ylabel("Search query")
    plt.title("📊 Top 10 Most Popular Search Queries")
    plt.grid(axis="x", linestyle="--", alpha=0.7)

    plt.show()


if __name__ == "__main__":
    plot_popular_queries()