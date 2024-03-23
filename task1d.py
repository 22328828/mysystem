import pandas as pd



booker = {'book_id': [123,345,56],
           'title': ['book','me time','my book'], 
            'author': ['jacob','Nkazimulo','zama'],
            'status': ['available']}

nk = pd.DataFrame(booker)

print("DataFrame for book " , nk)

member = {'member_id': [23,12,45],
                    'name': ['Nkazimulo','Prince','Kabyle'],
                    'borrowed_books':[]}

nka = pd.DataFrame(member)

print("DataFrame for member ",nk)
 