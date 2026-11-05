count = 10
while count > 0:
    print(count)
    count -= 1

for number in [1, 2, 3, 4, 5]:
    print(number, "-", number * number)

try:
    number = int(input("Enter a whole number: "))
except ValueError:
    print("Please enter a whole number.")
else:
    if number > 10:
        print("The number is greater than 10.")
    else:
        print("The number is not greater than 10.")
