from observer_pattern.IObserver import IObserver

class PhoneDisplay(IObserver):
    def __init__(self):
        pass
    
    def update(self, temperature: float, humidity: float, pressure: float):
        print(" Hello I am Phone Display ")
        print(f" Current updated measurements are, temp: {temperature}, humidity: {humidity}, pressure: {pressure} ")