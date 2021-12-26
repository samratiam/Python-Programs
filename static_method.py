# Static method

class Vehicle:

    @staticmethod
    def is_good_mileage(mileage): #notice self is not used
        if mileage < 25:
            return "No"
        return "Yes"

print(Vehicle.is_good_mileage(26))
print(Vehicle.is_good_mileage(19))