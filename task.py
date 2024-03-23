books = []
members = []

def add_book(book_id,title,author,status):
  books.append({"book_id": book_id,"title": title, "author" : author,"status": status})

def add_members(member_id,name):
    members.append({"member_id": member_id,"name": name,"borrowed_books":[]})


    add_book(2024001,"Python Programming","Jacob Zama","Available")
    add_members(1,"Alisa Marka")

print("Books",books)
print("\nMembers",members)
