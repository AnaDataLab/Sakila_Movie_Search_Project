from database.database_manager import (
    search_movies_by_title,
    search_movies_by_genre_and_year,
    search_movies_by_actor,
    get_top_10_popular_movies,
    save_search_query,
    create_tables
)
from visualization import plot_popular_queries

def print_separator():
    print("=" * 77)

def print_movies(movies):
    if not movies:
        print("\n❌ No movies found.")
        return

    print("\n🎬 Found movies:")
    print_separator()

    #проверка - есть ли в данных имена актёров
    if 'first_name' in movies[0] and 'last_name' in movies[0]:
        print(f"{'№':<3} | {'Actor':<20} | {'Title':<30} | {'Year':<5} | {'Rating':<6}")
        print_separator()
        for idx, movie in enumerate(movies, start=1):
            actor_name = f"{movie['first_name']} {movie['last_name']}"
            print(f"{idx:<3} | {actor_name:<20} | {movie['title'][:30]:<30} | {movie['release_year']:<5} | {movie['rating']:<6}")
    else:
        print(f"{'№':<3} | {'Title':<30} | {'Year':<5} | {'Rating':<6}")
        print_separator()
        for idx, movie in enumerate(movies, start=1):
            print(f"{idx:<3} | {movie['title'][:30]:<30} | {movie['release_year']:<5} | {movie['rating']:<6}")

    print_separator()

    while True:
        choice = input("\n🔎 Would you like to see the movie description? Enter the movie number or '0' to return to the main menu: ").strip()

        if choice == "0":
            return

        if not choice.isdigit() or not (1 <= int(choice) <= len(movies)):
            print("\n❌ Error: Please enter a valid movie number or '0' to return to the main menu.")
            continue

        selected_movie = movies[int(choice) - 1]
        print("\n📖  Movie description:")
        print_separator()
        print(f"🎬 {selected_movie['title']} ({selected_movie['release_year']})")
        print(f"⭐️ Rating: {selected_movie['rating']}")
        print(f"📝 {selected_movie['description']}")
        print_separator()

def main_menu():
    while True:
        print("\n🎬 Welcome to the Movie Search System!")
        print_separator()
        print("1️⃣ 🔍 Search movie by title")
        print("2️⃣ 🎭 Search movie by genre and year")
        print("3️⃣ 🎬 Search movie by actor")
        print("4️⃣ 📊 View Top 10 Most Popular Movies")
        print("5️⃣ 📈 View Popular Search Queries Chart")
        print("6️⃣ ❌ Exit")
        print_separator()

        choice = input("\nChoose an action (1-6): ").strip()

        if choice == "1":
            title = input("\n🔎 Enter a keyword from the movie title: ").strip()
            movies = search_movies_by_title(title)
            print_movies(movies)
            save_search_query("title", title)

        elif choice == "2":
            genre = input("\n🎭 Enter the movie genre: ").strip()
            year = input("📅 Enter the movie release year: ").strip()

            if not year.isdigit():
                print("\n❌ Error: The year must be a number. Try again.")
                continue

            movies = search_movies_by_genre_and_year(genre, int(year))
            print_movies(movies)
            save_search_query("genre_year", f"{genre}, {year}")

        elif choice == "3":
            actor_name = input("\n🎭 Enter an actor's first or last name: ").strip()
            movies = search_movies_by_actor(actor_name)
            print_movies(movies)
            save_search_query("actor", actor_name)

        elif choice == "4":
            queries = get_top_10_popular_movies()
            print("\n📊 Top 10 Most Popular Movies:")
            print_separator()
            print(f"{'№':<3} | {'Title':<30} | {'Year':<5} | {'Rating':<6} | {'Views'}")
            print_separator()

            for idx, query in enumerate(queries, start=1):
                print(
                    f"{idx:<3} | {query['title'][:30]:<30} | {query['release_year']:<5} | {query['rating']:<6} | {query['views']}")
            print_separator()

            while True:
                choice = input(
                    "\n🔎 Would you like to see the movie description? Enter the movie number or '0' to return to the main menu: ").strip()

                if choice == "0":
                    break

                if not choice.isdigit() or not (1 <= int(choice) <= len(queries)):
                    print("\n❌ Error: Please enter a valid movie number or '0' to return to the main menu.")
                    continue

                selected_movie = queries[int(choice) - 1]

                print("\n📖 Movie description:")
                print_separator()
                print(f"🎬 {selected_movie['title']} ({selected_movie['release_year']})")
                print(f"⭐️ Rating: {selected_movie['rating']}")
                print(f"📝 {selected_movie['description']}")
                print_separator()

            main_menu()


        elif choice == "5":
            print("\n📈 Generating Popular Search Queries Chart...")
            plot_popular_queries()

        elif choice == "6":
            print("\n👋 Goodbye!")
            break

        else:
            print("\n❌ Error: Invalid input. Please try again.")

if __name__ == "__main__":
    create_tables()  # Проверяем/создаём таблицу перед запуском
    main_menu()