import abc
class SmartDevice:
    def __init__(self,name,status):
        self._name = name
        self._status = 'off'
    @abc.abstractmethod
    def turn_on(self):
        pass
    @abc.abstractmethod
    def turn_off(self):
        pass
    def device_info(self):
        print(f"Device info:\n Name:{self._name}\n Status:{self._status}")
class Smart_light(SmartDevice):
    def __init__(self,name,status):
        super().__init__(name,status)
    def turn_on(self):
        self._status = 'on'
        print("Light is now on")
    def turn_off(self):
        self._status = 'off'
        print("Light is now off")

    def Set_brightness(self,brightness):
        self.brightness = brightness
        if brightness>0 and brightness<=100:
            print(f"The brightness is set to {brightness}%")
        else:
            print("Enter the valid brightness")

class Smart_Thermostat(SmartDevice):
    def __init__(self,name,status):
        super().__init__(name,status)

    def turn_on(self):
        self._status = 'on'
        print("Thermostat is on")

    def turn_off(self):
        self._status = 'off'
        print("Thermostat is off")

    def set_temperature(self,temp):
        self.temp = temp
        print(f"The temperature of thermostat is set to {temp}")

if __name__ == "__main__":
    sl1 = Smart_light("tube","on")
    sl1.turn_on()
    sl1.turn_off()
    sl1.Set_brightness(45)
    sl1.device_info()
    t1 = Smart_Thermostat("t1","on")
    t1.turn_on()
    t1.turn_off()
    t1.set_temperature(56)
    t1.device_info()