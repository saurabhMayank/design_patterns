from observer_pattern.IObserver import IObserver


class LcdDisplay(IObserver):
    def __init__(self):
        pass
    
    def update(self, temperature: float, humidity: float, pressure: float):
        print(" Hello I am LCD Display ")
        print(f" Current updated measurements are -> temp: {temperature}, humidity: {humidity}, pressure: {pressure} ")
        print("\n")