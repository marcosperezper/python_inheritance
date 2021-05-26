from deliverable import Deliverable


class Serie(Deliverable):
    # Properties
    __title = ""
    __seasons = 3
    __genre = ""
    __creator = ""

    # Constructor
    def __init__(self, title, seasons, genre, creator):
        self.__title = title
        self.__seasons = seasons
        self.__genre = genre
        self.__creator = creator

    # Getter/Setter
    @property
    def title(self):
        return self.__title

    @property
    def seasons(self):
        return self.__seasons

    @property
    def genre(self):
        return self.__genre

    @property
    def creator(self):
        return self.__creator

    @title.setter
    def title(self, title):
        self.__title = title

    @seasons.setter
    def seasons(self, seasons):
        self.__seasons = seasons

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @creator.setter
    def creator(self, creator):
        self.__creator = creator

    # Methods

    def __str__(self):
        return f"Title: {self.title}, Seasons: {self.seasons}, Genre: {self.genre}, Creator: {self.creator}"

    def comparable(self):
        return self.__seasons
