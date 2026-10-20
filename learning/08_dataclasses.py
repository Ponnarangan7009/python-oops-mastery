"""Dataclasses generate common methods for data-focused classes."""

from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    director: str
    year: int


movies = [
    Movie("Jailer 2", "Nelson", 2026),
    Movie("Dorothy", "Karthik", 2026),
]

# Dataclasses generate a useful __repr__ and value-based __eq__ by default.
for movie in movies:
    print(movie)

print(movies[0] == Movie("Jailer 2", "Nelson", 2026))

# A dataclass describes one record; the list stores multiple records.
