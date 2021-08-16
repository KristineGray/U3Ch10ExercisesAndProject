# 10.11. Exercises: Functions

line_start = '\n<--------'
line_end = '-------->'


part = '10.11.2. Part B: Return Values'
print(line_start, part, line_end)

def shift_case(phrase):
    new_phrase = ''
    for character in phrase:
        if character.isupper():
            new_phrase += character.lower()
        elif character.islower():
            new_phrase += character.upper()
        else:
            new_phrase += character
    return new_phrase

phrase = 'Hello, World!'
print(f'\nOriginal phrase: {phrase}\nNew phrase: {shift_case(phrase)}')


def calculate_average(num_list):
    list_sum = 0
    for num in num_list:
        list_sum += num
    ave_num = round(list_sum / len(num_list), 1)
    return ave_num

num_list_one = [2, 7, 6]
num_list_two = [20, 17, 46, 8]
num_list_three = [0, 3.33, 44, 50, 63, 70.9, 75.2, 83.2]

print(f'\nThe average of {num_list_one} is {calculate_average(num_list_one)}')
print(f'The average of {num_list_two} is {calculate_average(num_list_two)}')
print(f'The average of {num_list_three} is {calculate_average(num_list_three)}')


def make_line(num_chars, symbol='#'):
    line = ''
    for num in range(num_chars):
        line += symbol
    return line

first_line = make_line(5, 'T')
second_line = make_line(8)

print(f'\nThe output for "make_line(5, \'T\')" is:\n{first_line}')
print(f'\nThe output for "make_line(8)" is:\n{second_line}')

def make_rectangle(width, height, symbol='#'):
    rectangle_string = ''
    for row in range(height):
        if row == 0:
            rectangle_string = make_line(width, symbol)
        else:
            rectangle_string += '\n' + make_line(width, symbol)
    return rectangle_string

first_rectangle = make_rectangle(5, 3)
second_rectangle = make_rectangle(6, 2, '*')

print(f'\nThe output for "make_rectangle(5, 3)" is:\n{first_rectangle}')
print(f'\nThe output for "make_rectangle(2, 6, \'*\')" is:\n{second_rectangle}')

def make_square(side, symbol='#'):
    return make_rectangle(side, side, symbol)

first_square = make_square(5)
second_square = make_square(3, 'Racecar')

print(f'\nThe output for "make_square(5)" is:\n{first_square}')
print(f'\nThe output for "make_square(3, \'Racecar\')" is:\n{second_square}')



part = '10.11.3. Bonus Exercises'
print(line_start, part, line_end)

def make_right_triangle(height, symbol='^'):
    triangle_str = ''
    for row in range(height):
        if row == 0:
            triangle_str = make_line(row + 1, symbol)
        else:
            triangle_str += '\n' + make_line(row + 1, symbol)
    return triangle_str

print(f'\nRight Triangles:\n{make_right_triangle(3)}')

def make_iso_triangle(height, symbol='!'):
    # triangle_str = ''
    for row in range(height):
        spaces = make_line(height - row - 1, ' ')
        if row == 0:
            triangle_str = spaces + make_line((row + 1) * 2, symbol) + spaces
        else:
            triangle_str += '\n' + spaces + make_line((row + 1) * 2, symbol) + spaces

    return triangle_str

print(f'\nIsoceles Triangles:\n{make_iso_triangle(5)}')

def make_right_diamond_half(height, symbol='$'):
    diamond_str = make_right_triangle(height // 2, symbol)
    for row in range(height // 2, 0, -1):
        diamond_str += '\n' + make_line(row, symbol)

    return diamond_str

print(f'\nHalf Diamond:\n{make_right_diamond_half(8)}')