class Animal:
    def __init__(self, species):
        self.species = species
        print(f"{self.species} animal created")

    def make_sound(self):
        print("The animal makes a sound")

    def __del__(self):
        print(f"{self.species} animal destroyed")


class Dog(Animal):
    def __init__(self, breed="Unknown"):
        super().__init__("Dog")
        self.breed = breed
        print(f"Dog of breed {self.breed} created")

    def make_sound(self):
        print(f"The {self.breed} dog barks: Woof woof!")

    def wag_tail(self):
        print(f"The {self.breed} dog is wagging its tail")


def main():
    print("=== ANIMAL CLASS DEMONSTRATION ===")
    animal1 = Animal("Generic")
    animal1.make_sound()

    print("\n=== DOG CLASS DEMONSTRATION (INHERITANCE) ===")
    dog1 = Dog()
    dog1.make_sound()

    dog2 = Dog("Golden Retriever")
    dog2.make_sound()
    dog2.wag_tail()

    print("\n=== OBJECT DESTRUCTION ===")
    del animal1
    del dog1
    del dog2


if __name__ == "__main__":
    main()
