# lists
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
letters = ['a","b", "c']
zeros = [0] * 5

print(arr, matrix, letters, zeros, sep='\n')
# concat
conbined = arr + matrix
print(conbined)

numbers = list(range(7))
chars = list("string")
print(numbers, chars, sep="\n")

# acessing elements
print(arr[3])
print(arr[0:2])
print(matrix[1][2])

# unpacking and packing lists

other_list = list(range(10))

first, second, *others = other_list

print("first: ", first, "second: ", second, "others: ", others, sep='\n')

# loops with lists

others_letters = ['a', 'b', 'c', 'd', 'e']

for index, letter in enumerate(others_letters):
    print(index, letter)


# list methods

# add
letters = ['a', 'b', 'c', 'd', 'e']
letters.append("f")
print(letters)

# add in a specific position
letters.insert(2, "g")
print(letters)

# remove first occurence
letters.remove("g")
print(letters)

# remove last element
letters.pop()
print(letters)

# remove in a specific position
letters.pop(1)
print(letters)

# clear
letters.clear()
print(letters)

# sort
letters = ['a', 'b', 'd', 'e', 'c']
letters.sort()
print(letters)
print(letters.sort(reverse=True))

result = letters.index("d")
print(result)