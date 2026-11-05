def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


def calculate_sum(first, second):
    return first + second


def is_positive(number):
    return number > 0


def create_list(numbers):
    return [number * 2 for number in numbers]


def create_tuple(numbers):
    return tuple(number * 2 for number in numbers)


if __name__ == "__main__":
    greet("Mina")
    greet("Sam", "Good morning")
    print("Sum:", calculate_sum(2, 6))
    for number in (-2, 0, 3):
        print(number, "is positive:", is_positive(number))
    print(create_list([1, 2, 3]))
    print(create_tuple([1, 2, 3]))
