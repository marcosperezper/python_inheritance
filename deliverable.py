class Deliverable:
    # Properties
    __borrowed = False

    # Getter
    def is_delivered(self):
        return self.__borrowed

    # Methods
    def deliver(self):
        self.__borrowed = True

    def take_back(self):
        self.__borrowed = False

    def comparable(self):
        pass

    def compare_to(self, obj):
        if type(self) == type(obj):
            return self.comparable() > obj.comparable()
        else:
            raise Exception("You can't compare videogames with series")
