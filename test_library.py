from library import book_details

def test_book_details():
    output = book_details(101, "Python Basics", "John Doe", 2023)
    expected = (
        "Book ID: 101\n"
        "Book Title: Python Basics\n"
        "Author Name: John Doe\n"
        "Year of Publication: 2023"
    )
    assert output == expected
