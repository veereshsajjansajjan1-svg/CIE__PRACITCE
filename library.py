def book_details(book_id, title, author, year):
    details = (
        f"Book ID: {book_id}\n"
        f"Book Title: {title}\n"
        f"Author Name: {author}\n"
        f"Year of Publication: {year}"
    )
    return details


# Main program
if __name__ == "__main__":
    # Initializing values
    book_id = 101
    title = "Python Basics"
    author = "John Doe"
    year = 2023

    # Calling function
    result = book_details(book_id, title, author, year)
    print(result)
