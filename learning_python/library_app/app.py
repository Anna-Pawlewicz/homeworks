import json
import os
# [x] Zaimplementować dodawanie książek
# [x] Zaimplementować wyświetlanie książek
# [x] Zaimplementować usuwanie książek
# [x] Zaimplementować wyszukiwanie książek
# [X] Zaimplementować ocenianie książki po wciśnięciu klawisza 'O' (jak ocena)
#   Ocenić można w skali od 1 do 5 i musi być wybrana konkretna książka
#   Ocena ma się wyświetlać wraz z resztą informacji o książce
#   Nie powinno się podawać oceny w momencie dodawania książki do biblioteki
#   Jeśli wybierze się książkę, która już ma ocenę, to ocena ma zostać zaktualizowana
#   Zadbać o wyświetlanie stosownych komunikatów (np. jeśli podana ocena będzie spoza zakresu)
# [x] Zaimplementować wyświetlanie rankingu książek po wciśnięciu klawisz 'R' (jak ranking)
#   Ranking ma być inną formą wyświetlania, w której książki posortowane są od tej z najwyższą oceny
#   do tej z najniższą oceną (książki bez oceny nie mają być wyświetlane)
#   W przypadku braku ocenionych książek wyświetlić stosowny komunikat
from typing import List, Any

books = []
book_id = 1
library_json = "library.json"

welcome_message = """
Wciśnij D, aby dodać książkę
Wciśnij W, aby wyświetlić bibliotekę
Wciśnij U, aby usunąć książkę
Wciśnij S, aby wyszukać książkę
Wciśnij O, aby ocenić książkę
Wciśnij R, aby wyświetlić ranking
Wciśnij Z, aby zakończyć
Wybór: """


def main():
    print("Witaj w mojej bibliotece!")
    load_library()
    choice = input(welcome_message)

    while choice not in ('z', 'Z'):
        if choice in ('d', 'D'):
            add_book()
        elif choice in ('w', 'W'):
            display_library()
        elif choice in ('u', 'U'):
            delete_book()
        elif choice in ('s', 'S'):
            found_books = search_book()
            for book in found_books:
                display_book(book)
        elif choice in ('o', 'O'):
            rate_book()
        elif choice in ('r', 'R'):
            display_ranking()
        else:
            print("Wybrano nieznaną opcję, spróbuj jeszcze raz")

        choice = input(welcome_message)
    save_library()
    print("Biblioteka jest zamknięta")


def save_library():
    print("Zapisywanie biblioteki...")
    with open(library_json, "w") as library_file:
        json.dump(books, library_file)
    print("Biblioteka została zapisana pomyślnie")


def load_library():
    global books
    print("Wczytywanie biblioteki...")
    if os.path.exists(library_json):
        with open(library_json, "r") as library_file:
            books = json.load(library_file)
        print("Wczytano pomyślnie bibliotekę")
        unique_book_id()
        return
    print("Nie ma pliku biblioteki na dysku")


def unique_book_id():
    global book_id
    max_id = 0
    for book in books:
        if book["id"] > max_id:
            max_id = book["id"]
    book_id = max_id + 1


def add_book():
    global book_id
    title = input("Podaj tytuł: ")
    author = input("Podaj autora: ")
    year = input("Podaj rok wydania: ")
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year,
        "rate": None
    }
    book_id += 1
    books.append(new_book)
    print("Dodano książkę\n")
    display_book(new_book)


def display_book(book, show_id=False):
    if show_id:
        print(f"Id: {book['id']}")
    print(f"Tytuł: {book['title']}")
    print(f"Autor: {book['author']}")
    print(f"Rok wydania: {book['year']}")
    if book['rate'] is not None:
        print(f"Ocena książki: {book['rate']}")
    print("")


def display_library():
    for book in books:
        display_book(book)


def delete_book():
    books_to_delete = search_book()
    if len(books_to_delete) > 1:
        for book in books_to_delete:
            display_book(book, True)
        chosen_id = input("Podaj ID książki do usunięcia: ")
        decision = input(f"Czy chcesz usunąć książkę o id = {chosen_id} (T/n)?")
        if decision in ('T', 't'):
            for book in books:
                if book['id'] == int(chosen_id):
                    books.remove(book)
                    print("Książka usunięta")
                    break
    elif len(books_to_delete) == 1:
        display_book(books_to_delete[0])
        decision = input(f"Czy chcesz usunąć książkę (T/n)?")
        if decision in ('T', 't'):
            books.remove(books_to_delete[0])
            print("Książka usunięta")


def search_book():
    search_by = input("Podaj kryterium wyszukiwania (title, author, year): ")

    while search_by not in ("title", "author", "year"):
        search_by = input("Niepoprawne kryterium, spróbuj jeszcze raz: ")

    search_value = input(f"Podaj wartość kryterium {search_by}: ")

    found_books = []
    for found_book in books:
        if found_book[search_by] == search_value:
            found_books.append(found_book)

    if len(found_books) == 0:
        print("Nie znaleziono książki")

    return found_books


def rate_book():
    book_to_rate = search_book()
    if len(book_to_rate) > 1:
        for book in book_to_rate:
            display_book(book, True)
        chosen_id = int(input("Podaj ID książki do oceny: "))
        for book in books:
            if book['id'] == chosen_id:
                rate_value = int(input("Podaj ocenę od 1 do 5: "))
                while rate_value < 1 or rate_value > 5:
                    rate_value = int(input("Podaj ocenę od 1 do 5: "))
                book['rate'] = rate_value
                display_book(book, True)
                break
    elif len(book_to_rate) == 1:
        display_book(book_to_rate[0])
        rate_value = int(input("Podaj ocenę od 1 do 5: "))
        while rate_value < 1 or rate_value > 5:
            rate_value = int(input("Podaj ocenę od 1 do 5: "))
        book_to_rate[0]["rate"] = rate_value
        display_book(book_to_rate[0], True)
    else:
        return


def display_ranking():
    sorted_books = sorted(books, key=lambda k: (k["rate"]))
    sorted_books.reverse()
    for book in sorted_books:
        if book['rate'] is not None:
            display_book(book)


main()

# def word_translator(word):
#     if word == "tytul":
#         word = "title"
#     elif word == "autor":
#         word = "author"
#     elif word == "rok":
#         word = "year"
#     return word
