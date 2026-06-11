my_array = [0, 0, 0]

reverse = []

for numbers in range(len(my_array) - 1, -1, -1):
    reverse.append(my_array[numbers])

print("Original:",my_array)
print("Reversed:",reverse)

if reverse == my_array:
   print()
   print("True")
   #print("Original",my_array,"and reverse",reverse,"Is a palindrome")
else:
    print()
    print("False")
    #print("Original",my_array,"and reverse",reverse,"Is not a palindrome")
