from abc import ABC, abstractmethod
from observer_pattern.IObserver import IObserver

class IObservable(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def register_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass