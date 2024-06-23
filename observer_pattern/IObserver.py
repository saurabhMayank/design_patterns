from abc import ABC, abstractmethod


# Observer interface
class IObserver(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass