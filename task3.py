class Book:

    def __init__(self, name, author, count=1):
        self.name = name
        self.author = author
        self.count = count

    def __str__(self):
        return f"{self.name} — {self.author} | Кількість: {self.count}"

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                book.count += 1
                return
        new_book = Book(name, author)
        self.books.append(new_book)

    def user_take_book(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                if book.count > 0:
                    book.count -= 1
                    print(f"Ви взяли книгу - {book.name} від {author}")
                else:
                    print(f"Книга {book.name} є, але немає в наявності")
                return

        print("Такої книги не існує!")


    def show_books(self):
        if not self.books:
            print("Нічого немає")
        else:
            print("Список книг")
            for book in self.books:
                print(book)



lib = Library()
lib.add_book("Лисяча нора", "Нора Сакавіч")
lib.add_book("Хімія смерті", "Саймон Бекетт")
lib.add_book("Хірург", "Тесс Геррітсен")
lib.add_book("Асистент", "Тесс Геррітсен")
lib.add_book("Асистент", "Тесс Геррітсен")

print()
print("=====================\n")
lib.user_take_book("Відлік до смерті", "Андреас Ґрубер")
lib.user_take_book("Лисяча нора", "Нора Сакавіч")
lib.user_take_book("Хірург", "Тесс Геррітсен")
print()
print("=====================\n")
lib.show_books()
