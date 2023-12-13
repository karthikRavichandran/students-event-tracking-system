from abc import ABC, abstractmethod

class Page(ABC):

    @abstractmethod
    def display(self):
        pass

