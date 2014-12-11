__author__ = 'robinwyss'
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature import Temperature


class Temp:
    HOST = "192.168.1.60"
    PORT = 4223
    UID = "ngP"

    def __init__(self):
        ipcon = IPConnection()
        ipcon.connect(self.HOST, self.PORT)
        self.t = Temperature(self.UID, ipcon)

    def temperature(self):
        temperature = self.t.get_temperature()/100.0
        print('Temperature: ' + str(temperature) + ' C')



if __name__ == "__main__":
    temp = Temp()
    temp.temperature()
