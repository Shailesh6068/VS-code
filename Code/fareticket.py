class vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity

    def get_fare(self):
        return self.seating_capacity*100

class Bus(vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def get_fare(self):
        vehicle_fare =super().get_fare()
        maintain_fare = 0.1*vehicle_fare
        total_fare = vehicle_fare + maintain_fare
        return total_fare

vehicle1 =vehicle(50)
print("Vehicle fare : ",vehicle1.get_fare())

Bus1 = Bus(50)
print("bus fare :",Bus1.get_fare())



      