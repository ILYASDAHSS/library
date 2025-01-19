from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, title, identifier):
        self.title = title
        self.identifier = identifier
        self.borrowed_by = None

    @abstractmethod
    def display_info(self):
        pass

    def borrow(self, user):
        if self.is_available():
            self.borrowed_by = user
            user.add_borrowed_item(self)

    def return_item(self):
        if not self.is_available():
            user = self.borrowed_by
            self.borrowed_by = None
            user.remove_borrowed_item(self)

    def is_available(self):
        return self.borrowed_by is None


class Book(Document):
    def display_info(self):
        print(f"Book: {self.title}, ID: {self.identifier}")


class DVD(Document):
    def __init__(self, title, identifier, director):
        super().__init__(title, identifier)
        self.director = director

    def display_info(self):
        print(f"DVD: {self.title}, ID: {self.identifier}, Director: {self.director}")
        print(f"Hello, can you help me escape this world??")


class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

    def add_borrowed_item(self, document):
        self.borrowed_items.append(document)

    def remove_borrowed_item(self, document):
        self.borrowed_items.remove(document)

    def display_borrowed_items(self):
        titles = [doc.title for doc in self.borrowed_items]
        print(f"Borrowed items by {self.name}: {', '.join(titles)}" if titles else "No borrowed items.")


class Library:
    def __init__(self):
        self.documents = []

    def add_document(self, document):
        self.documents.append(document)

    def display_documents(self):
        print("\nAvailable documents:")
        for doc in self.documents:
            doc.display_info()

    def search_document(self, identifier):
        for doc in self.documents:
            if doc.identifier == identifier:
                return doc
        return None


def main():
    library = Library()
    reader = Reader("ILYAS")

    while True:
        print("\nMenu:")
        print("1. Add a document")
        print("2. Display documents")
        print("3. Borrow a document")
        print("4. Return a document")
        print("5. Display borrowed items")
        print("6. Quit")

        choice = input("Your choice: ")

        if choice == "1":
            print("1. Add a Book")
            print("2. Add a DVD")
            doc_type = input("Choose the document type: ")
            title = input("Title: ")
            identifier = int(input("Identifier: "))

            if doc_type == "1":
                library.add_document(Book(title, identifier))
            elif doc_type == "2":
                director = input("Director: ")
                library.add_document(DVD(title, identifier, director))
            else:
                print("Invalid choice.")

        elif choice == "2":
            library.display_documents()

        elif choice == "3":
            identifier = int(input("Identifier of the document to borrow: "))
            document = library.search_document(identifier)
            if document and document.is_available():
                document.borrow(reader)
                print(f"Document '{document.title}' borrowed successfully.")
            else:
                print("Document not available or not found.")

        elif choice == "4":
            identifier = int(input("Identifier of the document to return: "))
            document = library.search_document(identifier)
            if document and not document.is_available():
                document.return_item()
                print(f"Document '{document.title}' returned successfully.")
            else:
                print("Document not borrowed or not found.")

        elif choice == "5":
            reader.display_borrowed_items()

        elif choice == "6":
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()