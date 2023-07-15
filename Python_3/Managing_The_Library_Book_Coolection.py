# ------------------------------------------------------------------
# Implementation
# ------------------------------------------------------------------
# Checking if a book is contained in the Library collection
def is_string_present(array, target_string):
    return target_string in array

library = {}
library_total = 0
books_added = 0
books_removed = 0

def add_book(title, author, library_import = None, books_added_import = None, library_total_import = None,index = None):
    global library, books_added, library_total
    if(isinstance(title, str) == False):
        title = title[index]
    if(isinstance(author, str) == False):
        author = author[index]
    if(library_import != None):
        library = library_import[index]
    if(books_added_import != None):
        books_added = books_added_import[index]
    if(library_total_import != None):
        library_total = library_total_import[index]
    # Add the book to the library dictionary and increase both the 'books_added' and 'library_total' variables by 1.
        # Adding the book to the library dictionary
    library[title] = { "author": author }
        # Increasing both the "books_added" and "library_total" variables by one
    books_added += 1
    library_total += 1
    # Write the sentence confirming that the book has been added in the 'string_3a' variable.
    string_3a = "Book" + title + " by " + author + "has been added to the library."

    return is_string_present(library, title), books_added, library_total, string_3a


def search_book(title, library_import = None, index = None):
    global library
    if(isinstance(title, str) == False):
        title = title[index]
    if(library_import != None):
        library = library_import
    # Search for the book in the library. Also write two sentences that need to be returned as feedback by the code based on the outcome of the value of the boolean variable.
    # Store the relevant sentence in the 'string_3c' variable.
    # Note: If the boolean value is true, the code underneath the "if" statement will execute. If the boolean value is false, the code underneath the "else" statement will execute. 

    # Search for the book in the library using the "title" and "index"
    search_bool = (title in library)
    string_3b = ""

    if search_bool:
        string_3b = "Book found! " + title + " by " + library[title]["author"] + "."
    else:
        string_3b = "Book " + title + " not found in the library."

    return search_bool, string_3b


def remove_book(title, library_import = None, books_removed_import = None, library_total_import = None,index = None):
    global library, books_removed, library_total
    if(isinstance(title, str) == False):
        title = title[index]
    if(library_import != None):
        library = library_import[index]
    if(books_removed_import != None):
        books_removed = books_removed_import[index]
    if(library_total_import != None):
        library_total = library_total_import[index]
    # Check if the book is still in the library. 
    # If it is still in the library, set the boolean variable 'remove_book' to true to allow the code to remove the book from the library.
    # If the 'remove_book' variable is true, increase the 'books_removed' variable by 1 and decrease the 'library_total' variable by 1.
    # Also write the two sentences that need to returned as feedback by the code based on the outcome of the value of the boolean variable. 
    # Store these sentences in the 'string_3c' variable.
    # Note: If the boolean value is true, the code underneath the "if" statement will execute. If the boolean value is false, the code underneath the "else" statement will execute. 

    # Checking if the book  is  still  available  in  the  library.
    remove_book = search_book(title, library, index)[0]

    string_3c = ""

    if remove_book:
        author = library.pop(title) # This line of code removes the book 'title' from the library.
        books_removed += 1
        library_total -= 1
        string_3c = "Book " + title + " by " + author["author"] + " has been removed from the library."
    else:
        string_3c = "Book " + title + "not found in the library"

    return remove_book, books_removed, library_total, string_3c

def library_feedback(library_total_import = None, books_addded_import = None, books_removed_import = None, index = None):
    global books_added, books_removed, library_total
    if(library_total_import != None):
        library_total = library_total_import[index]
    if(books_addded_import != None):
        books_addded = books_addded_import[index]
    if(books_removed_import != None):
        books_removed = books_removed_import[index]
    # Generate the feedback of the library's book collection operation

    string_3d = "There are currently " + str(library_total) + " books in the book collection. The following operations were performed: " + str(books_added) + " books were added to the collection and " + str(books_removed) + " books were removed"
    return library_total, books_added, books_removed, string_3d

# ------------------------------------------------------------------
# Testing and Debugging Purposes
# ------------------------------------------------------------------

# Imports
import os, sys
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
with HiddenPrints():
    print("This Implementation is Just for Python 3 Programming Language Practices")

# Testing Code
print(" Question 3: Library's Book Collection".center(80, "-"), "\n")
books = ["The Joy of Programming", "The Laughing Algorithm", "Pythonic Puns","The Silly Science"]
authors = ["John Python","Alice Jester","Monty Coder"]

books_added = 0
books_removed = 0
library_total = 0

print(" Add a Book ".center(40, "-"))
response1d = add_book(books[0], authors[0])
print("\nIndex 0:\n", response1d)
print(library_feedback())
response2d = add_book(books[1], authors[1])
print("\nIndex 1:\n", response2d)
print(library_feedback())
response3d = add_book(books[2], authors[2])
print("\nIndex 0:\n", response3d)
print(library_feedback())
print()

print("\nLibrary:", library, "\n")


print(" Search for a Book ".center(40, "-"), "\n")
response1e = search_book(books[0])
response2e = search_book(books[2])
response3e = search_book(books[3])
print("Index 0:\n", response1e)
print("Index 2:\n", response2e)
print("Index 3:\n", response3e)
print()


print(" Remove a Book ".center(40, "-"))
response1f = remove_book(books[1])
print("\nRemove index 1:\n", response1f)
print(library_feedback())
response1g = remove_book(books[1])
print("\nRemove index 1:\n", response1g)
print(library_feedback())
response1h = remove_book(books[2])
print("\nRemove index 2:\n", response1h)
print(library_feedback())
response1i = remove_book(books[3])
print("\nRemove index 3:\n", response1i)
print(library_feedback())
response1j = remove_book(books[0])
print("\nRemove index 0:\n", response1j)
print(library_feedback())


print("\nLibrary:", library, "\n")

print()

print(" Search for a Book ".center(40, "-"))
response1k = search_book(books[1])#,library)
print(response1k)
print("--------- DONE --------")
