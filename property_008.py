class Test:
    def __init__(self):
        self.__color = "red"

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, clr):
        self.__color = clr


class Celsius:
    def __init__(self):
        self._temperature = 0

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")

        print("Setting value")
        self._temperature = value


if __name__ == '__main__':
    c = Celsius()
    c.temperature = 12  # set temperature
    print('The temperature is {}c.'.format(c.temperature))  # get temperature
