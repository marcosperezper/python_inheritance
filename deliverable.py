from abc import ABC


# Deliverable interface
class Deliverable(ABC):

    # Getter
    def is_delivered(self):
        pass

    # Methods
    def deliver(self):
        pass

    def take_back(self):
        pass

    def compare_to(self, obj):
        pass
