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


def make_line(num_chars, symbol):
    

part = '10.11.3. Bonus Exercises'
print(line_start, part, line_end)