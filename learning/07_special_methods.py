"""Special methods let objects work with built-in operations."""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        # Human-friendly text used by print(book).
        return f"{self.title} by {self.author}"

    def __repr__(self):
        # Unambiguous developer-oriented representation.
        return f"Book(title={self.title!r}, author={self.author!r})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author) == (other.title, other.author)


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        # Called by len(playlist); must return an integer.
        return len(self.songs)


class Score:
    def __init__(self, points):
        self.points = points

    def __add__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        # This example chooses to return a number.
        return self.points + other.points


book = Book("The Alchemist", "Paulo Coelho")
print(book)            # __str__
print(repr(book))      # __repr__
print(book == Book("The Alchemist", "Paulo Coelho"))  # __eq__

playlist = Playlist(["Imagine", "Hey Jude"])
print(len(playlist))   # __len__

print(Score(10) + Score(5))  # __add__
