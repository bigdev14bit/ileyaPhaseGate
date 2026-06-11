def find_duplicates_in(my_array):

    seen = []        # stores seen numbers
    duplicates = []  # stores seen numbers more than once

# loop through each number in the array
    for numbers in my_array:
        already_exists = False
    
    # check if number already exists in seen array
        for item in seen:
            if item == numbers:
                already_exists = True
                break
    
        if already_exists:
            # check if not already in duplicates to prevent adding multiple times
            already_duplicate = False
        
            for duplicate_item in duplicates:
                if duplicate_item == numbers:
                    already_duplicate = True
                    break
        
            if not already_duplicate:
                duplicates.append(numbers)
        else:
            seen.append(numbers)

    return duplicates

#original array
my_array = [1, 1, 1, 1, 1, 1]
result = find_duplicates_in(my_array)
print("Original:", my_array)
print("Duplicates:",result)
