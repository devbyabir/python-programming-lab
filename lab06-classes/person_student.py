class Person:
    def __init__(self, name, age):
        """Constructor to initialize person attributes"""
        self.name = name
        self.age = age
        print(f"Person created: {self.name} (Age: {self.age})")

    def greet(self):
        """Method to greet others"""
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

    def __del__(self):
        """Show when this object is finalized."""
        print(f"Person object {self.name} is being destroyed\n")


class Student(Person):
    def __init__(self, name, age, student_id, university="Demo University"):
        """Student constructor - inherits from Person"""
        super().__init__(name, age)  # Initialize parent class attributes
        self.student_id = student_id
        self.university = university
        print(f"Student record created - ID: {self.student_id}, University: {self.university}")

    def greet(self):
        """Override the greet method from Person"""
        print(
            f"Student introduction: {self.name}, ID: {self.student_id}, Age: {self.age}, Studying at {self.university}")

    def study(self, subject):
        """New method specific to Student class"""
        print(f"{self.name} is studying {subject} at {self.university}")


def main():
    print("=== PERSON CLASS DEMONSTRATION ===")
    person1 = Person("Mina", 25)
    person2 = Person("Sam", 30)

    # Call methods
    person1.greet()
    person2.greet()

    print("\n=== STUDENT CLASS DEMONSTRATION (INHERITANCE) ===")
    student1 = Student("Rahim", 22, "DEMO-001", "Zhengzhou University")

    # Call inherited and overridden methods
    student1.greet()
    student1.study("Computer Science & Engineering")


    print("\n=== OBJECT DESTRUCTION DEMONSTRATION ===")
    print("Deleting Mina's record explicitly...")
    del person1

    print("\n=== END OF DEMONSTRATION ===")


if __name__ == "__main__":
    main()
