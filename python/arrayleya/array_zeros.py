def move_zeros_in_the_array_to_the_back_in(my_array):

    non_zero = [] #create empty array to store non_zeros
    #zeros = []

    #loop through the original array
    for arrays in my_array:
        if arrays != 0: #if not zero, store it
            non_zero.append(arrays)

    zero_count = 0 #count how many zeros in our original array

    for numbers in my_array:
        if numbers == 0:
            zero_count = zero_count + 1

    for index in range(zero_count): #add zero to the end
        non_zero.append(0)

    return non_zero #return result

my_array = [5, 0, 3, 0, 2, 0]
result = move_zeros_in_the_array_to_the_back_in(my_array)

print("Original:",my_array)
print("After moving zeros:",result)
