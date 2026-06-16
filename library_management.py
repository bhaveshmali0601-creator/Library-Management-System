books = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append({"name": book, "issued": False})
        print("Book Added Successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            for book in books:
                status = "Issued" if book["issued"] else "Available"
                print(f"{book['name']} - {status}")

    elif choice == "3":
        search = input("Enter book name to search: ")
        found = False

        for book in books:
            if search.lower() == book["name"].lower():
                print("Book Found!")
                found = True

        if not found:
            print("Book not found.")

    elif choice == "4":
        book_name = input("Enter book name to issue: ")

        for book in books:
            if book["name"].lower() == book_name.lower():
                if not book["issued"]:
                    book["issued"] = True
                    print("Book Issued Successfully!")
                else:
                    print("Book already issued.")

    elif choice == "5":
        book_name = input("Enter book name to return: ")

        for book in books:
            if book["name"].lower() == book_name.lower():
                if book["issued"]:
                    book["issued"] = False
                    print("Book Returned Successfully!")
                else:
                    print("Book was not issued.")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
