class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        # Initialize the total and available spots for each fuel type
        self.total_spots = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }
        self.available_spots = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }

    def fuel_vehicle(self, fuel_type: str) -> bool:
        # Check if there are available spots for the given fuel type
        if self.available_spots.get(fuel_type, 0) > 0:
            self.available_spots[fuel_type] -= 1
            return True
        return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        # Check if we can release a spot for the given fuel type
        if self.available_spots.get(fuel_type, 0) < self.total_spots.get(fuel_type, 0):
            self.available_spots[fuel_type] += 1
            return True
        return False


# Example Usage:
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

print(fuel_station.fuel_vehicle("diesel"))  # true (1 slot now open)
print(fuel_station.fuel_vehicle("petrol"))  # true (1 slot now open)
print(fuel_station.fuel_vehicle("diesel"))  # true (0 slots now open)
print(fuel_station.fuel_vehicle("electric"))  # true (0 slots now open)
print(fuel_station.fuel_vehicle("diesel"))  # false (0 slots open)
print(fuel_station.open_fuel_slot("diesel"))  # true (1 slot now open)
print(fuel_station.fuel_vehicle("diesel"))  # true (0 slots now open)
print(fuel_station.open_fuel_slot("electric"))  # true (1 slot now open)
print(fuel_station.open_fuel_slot("electric"))  # false (only 1 slot available at the fuel station)
