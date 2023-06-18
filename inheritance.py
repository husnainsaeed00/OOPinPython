class Animal:
    def speak(self):
        print('Animal speeks')

class Dog(Animal):
    def speak(self):
        print("dogs bark")

animal= Animal()
dog = Dog()

animal.speak()
dog.speak()