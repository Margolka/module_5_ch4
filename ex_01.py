import random
from datetime import date


class Film:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        # Variables
        self._views = 0

    @property
    def views(self):
        return self._views

    def play(self, step=1):
        self._views += step

    def __str__(self):
        return f"{self.title} ({self.year})"


class Serial(Film):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} (S{self.season:02d}E{self.episode:02d})"


def filtration(how=None):
    if how == None:
        return list
    return [item for item in list if item.__class__ == how]


def get_movies():
    return sorted(filtration(Film), key=lambda film: film.title)


def get_series():
    return sorted(filtration(Serial), key=lambda serial: serial.title)


def search(wanted):
    return [item for item in list if item.title == wanted].pop()


def generate_views():
    drawn = random.choice(list)
    drawn.play(random.randint(1, 100))
    print(drawn, drawn.views)


def generate_views_for_10():
    for _ in range(10):
        generate_views()


def top_titles(how_many, content_type=None):
    by_views = sorted(
        filtration(content_type), key=lambda item: item.views, reverse=True
    )
    return by_views[:how_many]


if __name__ == "__main__":
    print("Biblioteka filmów")
    # Movies and Serials sample
    film_01 = Film(title="Zielona mila", year=1999, genre="Dramat")
    film_02 = Film(title="Skazani na Shawshank", year=1994, genre="Dramat")
    film_03 = Film(title="Forrest Gump", year=1994, genre="Dramat/Komedia")
    film_04 = Film(title="Leon zawodowiec", year=1994, genre="Dramat/Kryminał")
    film_05 = Film(title="Requiem dla snu", year=2000, genre="Dramat")
    film_06 = Film(title="Matrix", year=1999, genre="Akcja/Sci-fi")
    film_07 = Film(title="Milczenie owiec", year=1991, genre="Thriller")
    film_08 = Film(title="Gladiator", year=2000, genre="Dramat historyczny")
    serial_01 = Serial(
        title="Gra o tron",
        year=2011,
        genre="Dramat/Fantasy/Przygodowy",
        season=1,
        episode=10,
    )
    serial_02 = Serial(
        title="Dr House", year=2005, genre="Dramat/Komedia", season=1, episode=22
    )
    serial_03 = Serial(
        title="Breaking Bad", year=2008, genre="Drama/Kryminał", season=1, episode=7
    )
    serial_04 = Serial(
        title="Stranger Things",
        year=2016,
        genre="Dramat/Horror/Sci-Fi",
        season=1,
        episode=8,
    )
    serial_05 = Serial(
        title="Przyjaciele", year=1994, genre="Komedia", season=1, episode=24
    )
    serial_06 = Serial(
        title="Sherlock", year=2010, genre="Dramat/Kryminał", season=1, episode=3
    )

    list = [
        film_01,
        film_02,
        film_03,
        film_04,
        film_05,
        film_06,
        film_07,
        film_08,
        serial_01,
        serial_02,
        serial_03,
        serial_04,
        serial_05,
        serial_06,
    ]

    generate_views_for_10()
    print(f"Najpopularniejsze filmy i seriale dnia {date.today().strftime('%d.%m.%Y')}")
    popular = top_titles(3)
    for item in popular:
        print(item, item.views)
