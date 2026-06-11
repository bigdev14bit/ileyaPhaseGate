array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

add_even = []
odd_numbers = []

for numbers in array:
    if numbers % 2 == 0:
        add_even.append(numbers)
    else:
        odd_numbers.append(numbers)

print("Even Numbers:",add_even)
print("Odd Numbers:",odd_numbers)
print("Both:",[add_even, odd_numbers])
