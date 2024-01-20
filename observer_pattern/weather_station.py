from observer_pattern.IObservable import IObservable
from observer_pattern.IObserver import IObserver

class WeatherStation(IObservable):

    def __init__(self):
        # list of observers
        self.observers: List[IObserver] = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer: IObserver):
        self.observers.append(observer)
    
    def remove_observer(self, observer: IObserver):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observ in self.observers:
            observ.update(self.temperature, self.humidity, self.pressure)


    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        # after measurements are reset
        # state of observable has changed -> notify all observers
        self.notify_observers()
