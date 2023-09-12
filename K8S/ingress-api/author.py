from fastapi import FastAPI
import my_data
app = FastAPI()


@app.get("/")
def read_root():
    return {"about API": "u can find book written by author... Usage: /author/{author_name} "}


@app.get("/author/{author_name}")
def read_item(author_name):
    #print(author_name)
    #print(my_data.get_books_by_author(author_name))
    return my_data.get_books_by_author(author_name)


