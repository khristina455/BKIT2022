from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def square(self):
        """
        содержит виртуальный метод для вычисления площади фигуры.
        """
        pass