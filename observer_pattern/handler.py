from observer_pattern.weather_station import WeatherStation
from observer_pattern.phone_display import PhoneDisplay
from observer_pattern.lcd_display import LcdDisplay

# observable
weather_station = WeatherStation()

# observer 1
lcd = LcdDisplay()

# observer 2
phone = PhoneDisplay()

# register observers
weather_station.register_observer(lcd)
weather_station.register_observer(phone)

# set measurements
# when measurements are set then -> all the observers
# will also be notified
weather_station.set_measurements(10.0, 12.5, 15.7)