# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if not numbers:
        return (None, None)
    if len(numbers) == 1:
        return (numbers[0], None)

    max1 = numbers[0]
    max2 = None

    for n in numbers[1:]:
        if n > max1:
            max2 = max1
            max1 = n
        elif n < max1:
            if max2 is None or n > max2:
                max2 = n

    return (max1, max2)

# print(max_two_in_list([10, 10, 9, 8, 7]))


# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
   return sorted(set(numbers))

# print(remove_duplicates_and_sort([10, 5, 5, 10, 2]))

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num
        result.append(total)
    return result

# print(cumulative_sum([5, 10, 15]))

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

# print(transpose_matrix([[7, 8], [9, 10], [11, 12]]))

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[0::step]

# print(slice_every_nth([10, 20, 30, 40, 50], 3))


# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    total = 0
    for x, y in zip(list1, list2):
        total += x * y
    return total
# print(dot_product([2, 3, 4], [5, 6, 7]))


# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total += matrix1[i][k] * matrix2[k][j]
            result[i][j] = total

    return result
print(matrix_multiplication([[2, 4], [6, 8]], [[1, 3], [5, 7]]))
