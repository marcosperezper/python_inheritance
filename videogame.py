from deliverable import Deliverable


class Videogame(Deliverable):
    # Properties
    __title = ""
    __estimated_hours = 10
    __genre = ""
    __company = ""
    __borrowed = False

    # Constructor
    def __init__(self, title, estimated_hours, genre, company):
        self.__title = title
        self.__estimated_hours = estimated_hours
        self.__genre = genre
        self.__company = company

    # Getter/Setter
    @property
    def title(self):
        return self.__title

    @property
    def estimated_hours(self):
        return self.__estimated_hours

    @property
    def genre(self):
        return self.__genre

    @property
    def company(self):
        return self.__company

    @title.setter
    def title(self, title):
        self.__title = title

    @estimated_hours.setter
    def estimated_hours(self, estimated_hours):
        self.__estimated_hours = estimated_hours

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @company.setter
    def company(self, company):
        self.__company = company

    # Methods
    def __str__(self):
        return f"Title: {self.title}, Hours: {self.estimated_hours}, Genre: {self.genre}, Company: {self.company}"

    def is_delivered(self):
        return self.__borrowed

    def deliver(self):
        self.__borrowed = True

    def take_back(self):
        self.__borrowed = False

    def compare_to(self, obj):
        return self.__estimated_hours > obj.__estimated_hours
