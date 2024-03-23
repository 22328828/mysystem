books = []
members = []

def add_book():

  books.append({"book_id": int(input("Enter the book_id")),
                "title": input("Enter the title"), 
                "author": input("Enter the author"),
                "status": input("Enter the status")})

def add_members():
    members.append({"member_id": int(input("Enter member ID: ")),
                    "name": input("Enter the name"),
                    "borrowed_books":[]})


    add_book()
    add_members()

print("Books",books)
print("\nMembers",members)