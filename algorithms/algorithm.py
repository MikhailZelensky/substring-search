from abc import ABC, abstractmethod


class Algorithm(ABC):

    @staticmethod
    @abstractmethod
    def search(substring, text):
        pass

    @classmethod
    def findall(cls, substring, text):
        return list(cls.search(substring, text))

    @classmethod
    def name(cls):
        return cls.__name__
