my_array = [4, 7, 9, 10, 16, 18]
perfect_squares = []

def perfect_square():

    for numbers in my_array:

        number = 0

        while number * number <= numbers:
            if number * number == numbers:
                perfect_squares.append(numbers)
                break

            number = number + 1

        else:
            perfect_squares.append(-1)

print(perfect_square())
print("Original:",my_array)
print("Perfect square:",perfect_squares)

