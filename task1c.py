books = []
members = []



books.append({"book_id": int(input("Enter the book_id")),
                "title": input("Enter the title"), 
                "author": input("Enter the author"),
                "status": input("Enter the status")})

members.append({"member_id": int(input("Enter member ID: ")),
                    "name": input("Enter the name"),
                    "borrowed_books":[]})


    
    

print("Books",books)
print("\nMembers",members)