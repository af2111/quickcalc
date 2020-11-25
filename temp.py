class UnitError(Exception):
    pass


def celsius(num, fromUnit):
    if fromUnit == "c": 
        return num
    if fromUnit == "k": 
        return num - 273.15
    if fromUnit == "f":
        return (num - 32) * 5/9
def kelvin(num, fromUnit):
    if fromUnit == "c": 
        return num + 273.15
    if fromUnit == "k":
        return num
    if fromUnit == "f": 
        return (num - 32) * 5/9 + 273.15
def fahrenheit(num, fromUnit):
    if fromUnit == "c": 
        return (num * 9/5) + 32
    if fromUnit == "k":
        return (num - 273.15) * 9/5 + 32
    if fromUnit == "f": 
        return num
class Convert:
    temperatureUnits = {
        "c": celsius,
        "f": fahrenheit,
        "k": kelvin
    }
    @staticmethod
    def Temperature(num, fromUnit, toUnit):
        if toUnit in Convert.temperatureUnits and fromUnit in Convert.temperatureUnits:
            return Convert.temperatureUnits[toUnit](num, fromUnit)
        else:
            raise UnitError
if __name__ == "__main__":
    print(Convert.Temperature(42, "k", "c"))
    print(Convert.Temperature(42, "c", "k"))
    print(Convert.Temperature(42, "c", "f"))
