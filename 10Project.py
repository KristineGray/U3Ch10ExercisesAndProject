# 10.12. Project: Functions

line_start = '\n<--------'
line_end = '-------->'

part = '10.12.2. Part A: Reverse Characters'
print(line_start, part, line_end)
'''
def reverse_characters(string):
    char_list = list(string)
    char_list.reverse()
    reversed_string = ''.join(char_list)
    return reversed_string

# string_input = input('Enter a string to reverse: ')
string_input = 'Reverse Me!'
print(f'Your string: {string_input} \nReversed string: {reverse_characters(string_input)}')
'''

part = '10.12.3. Part B: Reverse Digits'
print(line_start, part, line_end)

# reverse_characters(1234)

def reverse_characters(value):
    if type(value) == str:
        char_list = list(value)
        char_list.reverse()
        reversed_string = ''.join(char_list)
        return reversed_string
    if type(value) == int or type(value) == float:
        num_as_str = str(value)
        digit_list = list(num_as_str)
        digit_list.reverse()
        if type(value) == int:
            reversed_num = int(''.join(digit_list))
        else:
            reversed_num = float(''.join(digit_list))
        return reversed_num

print(f'\nReversing 56791 returns: {reverse_characters(56791)}')
print(f'\nReversing 24.65 returns: {reverse_characters(24.65)}')


part = '0.12.4. Part C: Complete Reversal'
print(line_start, part, line_end)

def reverse_list(old_list):
    new_list = []
    for element in old_list:
        new_element = reverse_characters(element)
        new_list.append(new_element)
    return new_list

list_str = ['apple', 'potato', 'Capitalized Words']
list_num = [123, 8897, 4.2, 1138, 8675309]	
list_mix = ['hello', 'world', 12.3, 'orange', 987]	

print(f'\nReversing {list_str} returns:\n\t{reverse_list(list_str)}')
print(f'\nReversing {list_num} returns:\n\t{reverse_list(list_num)}')
print(f'\nReversing {list_mix} returns:\n\t{reverse_list(list_mix)}')


part = '10.12.5. Bonus Missions'
print(line_start, part, line_end)

def fun_phrase(phrase):
    if len(phrase) <= 3:
        sub_phrase = phrase[-1]
    else:
        sub_phrase = phrase[:3]
    message = f"We put the '{sub_phrase}' in '{phrase}'."
    return message

print(fun_phrase('Functions rock!'))

def rectangle_area(length, width):
    return length * width

area_one = rectangle_area(5, 10)
area_two = rectangle_area(7, 6)

print(f"The area is {area_one} cm^2.")
print(f"The area is {area_two} cm^2.")