def reverse_string(text):
    letters = []
    for index in range(len(text) - 1, -1, -1):
        letters.append(text[index])
    return "".join(letters)


def fibonacci(position):
    if position < 0:
        raise ValueError("Position must be zero or greater.")
    current, following = 0, 1
    for _ in range(position):
        current, following = following, current + following
    return current


def bubble_sort(numbers):
    result = list(numbers)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(bubble_sort([5, 1, 4, 2, 1]))
    try:
        position = int(input("Fibonacci position (0-1000): "))
        if not 0 <= position <= 1000:
            raise ValueError("Enter a position from 0 to 1000.")
        print(fibonacci(position))
    except ValueError as error:
        print(error)
