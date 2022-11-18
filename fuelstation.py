class FuelStation:

    def __init__(self, diesel, petrol, electric):
        self.available_fuel_station = {'diesel': diesel,
                                       'petrol': petrol,
                                       'electric': electric}
        self.max_available_fuel_station = {'diesel': diesel,
                                           'petrol': petrol,
                                           'electric': electric}

    def open_fuel_slot(self, fuel_type):
        if self.available_fuel_station.get(fuel_type) is not None and\
                self.available_fuel_station.get(fuel_type) < self.max_available_fuel_station.get(fuel_type):
            self.available_fuel_station[fuel_type] = self.available_fuel_station.get(fuel_type) + 1
            return True
        return False

    def fuel_vehicle(self, fuel_type):
        if self.available_fuel_station.get(fuel_type) is not None and\
                self.available_fuel_station.get(fuel_type) > 0:
            self.available_fuel_station[fuel_type] = self.available_fuel_station.get(fuel_type) - 1
            return True
        return False


fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.fuel_vehicle('petrol'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.fuel_vehicle('electric'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.open_fuel_slot('diesel'))
print(fuel_station.fuel_vehicle('diesel'))
print(fuel_station.open_fuel_slot('electric'))
print(fuel_station.open_fuel_slot('electric'))
