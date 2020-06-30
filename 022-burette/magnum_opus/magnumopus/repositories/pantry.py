from abc import ABC, abstractmethod

class Pantry(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_substance(self, substance):
        pass

    @abstractmethod
    def find_substances_by_nature(self, nature):
        pass

    @abstractmethod
    def count_all_substances(self):
        pass

    @abstractmethod
    def commit(self):
        pass
