import urllib.request
import json



url = "https://raw.githubusercontent.com/edk2010/DevSecOps/main/K8S/ingress-api/data_base.json"
json_file = urllib.request.urlopen(url)
data = json.load(json_file)



# Assuming you have the JSON data stored in a file named 'books_and_authors.json'
def get_book_by_name(book_name):
    try:


        for book in data["books"]:
            if book["title"] == book_name:
                author_id = book["author_id"]
                for author in data["authors"]:
                    if author["id"] == author_id:
                        book["author_name"] = author['name']
                        book['author_birth_year'] = author['birth_year']
                        book['author_nationality'] = author['nationality']
                        return book

        return None

    except FileNotFoundError:
        print("JSON data file not found.")
        return None



# Assuming you have the JSON data stored in a file named 'books_and_authors.json'
def get_books_by_author(author_name):
    try:
        #json_file = urllib.request.urlopen(url)

        #data = json.load(json_file)

        author_books = []
        for book in data["books"]:
            author_id = book["author_id"]
            for author in data["authors"]:
                if author["id"] == author_id and author["name"] == author_name:
                    author_books.append(book["title"])

        return author_books

    except FileNotFoundError:
        print("JSON data file not found.")
        return None





if __name__ == '__main__':

    # Example usage get_books_by_author:
    author_name = "Author1"
    books_by_author = get_books_by_author(author_name)
    print(books_by_author)
    if books_by_author:
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(book)
    else:
        print(f"No books found by {author_name}.")




    # Example usage get_book_by_name:
    book_name = "Book1"
    book_info = get_book_by_name(book_name)
    print(book_info)
    if book_info:
        print("Book Information:")
        print(f"Title: {book_info['title']}")
        print(f"Publication Year: {book_info['publication_year']}")
        print("Author Information:")
        print(f"Author Name: {book_info['author_name']}")
        print(f"Author Birth Year: {book_info['author_birth_year']}")
        print(f"Author Nationality: {book_info['author_nationality']}")
    else:
        print(f"No book found with the name {book_name}.")
