import random

books = [
      {"title": "Clean Code", "author": "Robert C. Martins", "genre": "Programming", "page": "462"},
      {"title": "Java How To Programmer", "author": "Paul Dietel", "genre": "Programming", "page": 1286},
      {"title": "A Woman Of Substance", "author": "Barbara Taylor Bradford", "genre": "Novel", "page": "2000"},
      {"title": "The Psychology of Persuasion", "author": "Robert B. Cialdini", "genre": "Socials", "page": "10000"},
      {"title": "Dune", "author": "Frank Herbert", "genre": "Sci-fi", "page": "8500"},
      {"title": "The alchemist", "author": "??", "genre": "Fiction", "page": "8000"},
      {"title": "The name of the wind", "author": "Patrick Rothfuss", "genre": "Fantasy", "page": "10000"}
        ]

menu = """
==============================================================================
WELCOME   TO   BOOK   RECOMMENDING   SYSTEM
==============================================================================

1. GET RECOMMENDATION.
2. ADD BOOK.
3. REMOVE BOOK.
4. UPDATE BOOK.
5. EXIT
==============================================================================
"""

print(menu)
while True:

    userInput = input("Enter Option: ")
    if userInput == "5":
        print()
        print("Exit Successfully.")
        break

    elif userInput == "1":
        recommended_book = random.choice(books)
        print()
        print("=" * 50)
        print("----RECOMMENDING----")
        print()
        print(f"TITLE------>   {recommended_book["title"]}")
        print(f"AUTHOR----->   {recommended_book["author"]}")
        print(f"GENRE------>   {recommended_book["genre"]}")
        print(f"PAGE------->   {recommended_book["page"]}")
        print("=" * 50)
        print()

    elif userInput == "2":
        print()
        print("----ADD   BOOK----")

        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        page = input("Page: ")

        add_book = {
            "title": title,
            "author": author,
            "genre": genre,
            "page": page
                }

        books.append(add_book)

        print()
        print("----BOOK   ADDED   SUCCESSFULLY----")
        print()
        print("=" * 50)
        print(f"TITLE------>   {title}")
        print(f"AUTHOR----->   {author}")
        print(f"GENRE------>   {genre}")
        print(f"PAGE------->   {page}")
        print("=" * 50)
        print()

    elif userInput == "3":
        print()
        print("----REMOVE   BOOK----")
        print()

        if len(books) == 0:
            print()
            print("No Books To Remove In The System")
            break
        else:
            counter = 1

            remove_book = input("Did You Want To Remove Any Book: ")
            clean_remove = remove_book.strip().lower()

            if clean_remove != "no":
                for book in books:
                    print(f"{counter}: TITLE----->   {book["title"]}")
                    counter = counter + 1

                print()
                number_of_book_to_remove = int(input("Enter Number Of Book To Remove: "))
                if number_of_book_to_remove <= 1 and number_of_book_to_remove >= len(books):
                    print("Errror, book not found!.")
                else:
                    book_to_remove = number_of_book_to_remove - 1
                    deleted = books.pop(book_to_remove)

                    print()
                    print("=" * 50)
                    print("Book Deleted Successfully")
                    print(f"REMOVED:----->   {deleted["title"]}")
                    print("----Remaining",len(books),"Books.----")
                    print("=" * 50)
                    print()

    elif userInput == "4":
        print()
        print("----UPDATE   BOOK----")
        print()

        if len(books) == 0:
            print()
            print("No Books To Update In The System")
            break
        else:
            counter = 1

            for things in books:
                print(f"{counter}: TITLE----->   {things["title"]}")
                counter = counter + 1

            print()
            update_book = int(input("Enter Number Of Book To Update: "))
            if update_book <= 1 and update_book >= len(books):
                print()
                print("Errror, book not found!.")
            else:
                book_to_update = update_book - 1
                selected_book = books[book_to_update]

                menu = f"""
            YOU SELECETED:

TITLE:    "{selected_book["title"]}"
What Did You Want To Update??

1: Title.
2: Author's Name.
3: Genre Title.
4: Page Count.
                """
                print(menu)
                update_input = int(input("Enter Option: "))
                if update_input == 1:
                    title = input(f"Change: {selected_book["title"]} title: ")
                    selected_book["title"] = title
                    print()
                    print(f"Book Updated Successfully.")
                    print(f"New Title:  {selected_book["title"]}")

                elif update_input == 2:
                    author = input(f"Change: {selected_book["author"]} author's name: ")
                    selected_book["author"] = author
                    print()
                    print(f"Book Updated Successfully.")
                    print(f"New Author's Name:  {selected_book["author"]}")

                elif update_input == 3:
                    genre = input(f"Change: {selected_book["genre"]} genre title: ")
                    selected_book["genre"] = genre
                    print()
                    print(f"Book Updated Successfully.")
                    print(f"New Genre Title:  {selected_book["genre"]}")

                elif update_input == 4:
                    page_count = int(input(f"Change: {selected_book["page"]} page count: "))
                    selected_book["page"] = page_count
                    print()
                    print(f"Book Updated Successfully.")
                    print(f"New Page Count:  {selected_book["page"]}")

                else:
                    print("Invalid Stuffs.")

    else:
        print("Invalid Inputs!")
