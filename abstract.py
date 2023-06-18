from abc import ABC, abstractmethod

# Define an abstract base class
class Animal(ABC):

    # Declare an abstract method
    @abstractmethod
    def sound(self):
        pass

# Create a concrete subclass that inherits from the abstract base class
class Dog(Animal):

    # Implement the abstract method in the subclass
    def sound(self):
        print("Dog barks")

# Create another concrete subclass
class Cat(Animal):

    # Implement the abstract method differently in the subclass
    def sound(self):
        print("Cat meows")

# Create instances of the concrete subclasses
dog = Dog()
cat = Cat()

# Call the sound method on the instances
dog.sound()  # Output: Dog barks
cat.sound()  # Output: Cat meows
