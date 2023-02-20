# Define a class named Car
class Car:
    def __init__(self, name):
        self.name = name

    # Method to make the car go
    def go(self):
        print("The " +self.name + " is moving.")

    # Method to make the car stop
    def stop(self):
        print("The " + self.name + " is stopping.")

# Define a main function to create and use Car objects
def main():
    # Create a Car object named car1 with name "Chevy"
    car1 = Car("Chevy")
    # Make car1 go and stop
    car1.go()
    car1.stop()

    # Create a Car object named car2 with name "Kia"
    car2 = Car("Kia")
    # Make car2 go and stop
    car2.go()
    car2.stop()

# Call the main function if this script is being run directly
if __name__ == "__main__":
  main()
