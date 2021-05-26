
def spiral_array_printer(array, number_of_columns, number_of_rows):
    top, left = 0, 0
    bottom = number_of_rows - 1
    right = number_of_columns - 1
    direction = 0
    x_index = 0
    y_index = 0
    elements_printed = 0 
    while elements_printed <= (number_of_columns*number_of_rows - 1):
        print(array[x_index][y_index], end=' ')
        elements_printed += 1

        if direction == 0:
            if y_index >= right:
                direction = 1
                top += 1
                x_index += 1
            else:
                y_index += 1

        elif direction == 1:
            if x_index >= bottom:
                direction = 2
                bottom -= 1
                y_index -= 1
            else:    
                x_index += 1

        elif direction <= 2:
            if y_index <= left:
                direction = 3
                right -= 1
                x_index -= 1
            else:
                y_index -= 1

        elif direction == 3:
            if x_index <= top:
                direction = 0
                left += 1
                y_index += 1 
            else:
                x_index -= 1


matrix_1 = [
    [3],
    [6],
    [9],
]

number_of_rows = len(matrix_1)
number_of_columns = len(matrix_1[0])

spiral_array_printer(matrix_1, number_of_columns, number_of_rows)
print("")
    