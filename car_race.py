import random
# Create the car class
class Car:
    # Create an initializer function
    def __init__(self, make, model, color, driver, max_speed, handling):
        self.make = make
        self.model = model
        self.color = color
        self.driver = driver
        self.max_speed = max_speed
        self.handling = handling
        self.miles_driven = 0
    def show_car_info(self):
        print(f"The {self.color} {self.make} {self.model} is driven by {self.driver}")
    
    def drive_car(self):
        self.miles_driven += random.randint(5,self.max_speed) + self.handling
    
    def show_stats(self, miles_to_win):
        print(f"{self.driver}'s car advanced to {self.miles_driven}")
        print()
        if self.miles_driven > miles_to_win:
            print(f"{self.driver} won the race!!!")

    def hit_maxwell(self, reduce_speed):
        hit = random.randint(1,3)
        if hit == 1:
            print(f"💥💥💥💥😿💥💥💥💥 Maxwell was hit by {self.driver}")
            reduce_speed = random.randint(10, 20)
            self.max_speed -= reduce_speed
            print(f"Max speed reduced by {reduce_speed}")
            print()
        else:
            print(f"Maxwell managed to save himself from {self.driver}")


def main():
    miles_to_win = 100
    # Create a car object
    muskCar = Car("Mazda", "Miata", "orange", "Elon Musk", 60, 11)

    # Create a second car
    bezosCar = Car("Nissan", "Sentra", "silver", "Jeff Bezos", 50, 12)

    print("The race is beginning.....")
    print("🏁🏁🏁🏁")

    # Call the instance function
    muskCar.show_car_info()
    print()
    bezosCar.show_car_info()
    
    while muskCar.miles_driven < 100 or bezosCar.miles_driven < 100:

        # Drive both cars at once
        muskCar.drive_car()
        bezosCar.drive_car()

        # Show the updated stats
        muskCar.show_stats(miles_to_win)
        bezosCar.show_stats(miles_to_win)

        # Call the hit_maxwell method on both Car objects
        muskCar.hit_maxwell()
        bezosCar.hit_maxwell()
    

if __name__ == "__main__":
    main()