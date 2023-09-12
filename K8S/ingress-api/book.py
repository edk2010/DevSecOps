from fastapi import FastAPI
import my_data
app = FastAPI()

@app.get("/")
def read_root():
    return {"about API": "u can find information about books...Usage: /book/{book_name}"}


@app.get("/book/{book_name}")
def read_item(book_name):
    print(book_name)
    print(my_data.get_book_by_name(book_name))
    return my_data.get_book_by_name(book_name)
