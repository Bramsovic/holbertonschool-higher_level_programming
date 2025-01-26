#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    roman_numbers = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previous_value = 0

    for char in roman_string:
        current_value = roman_numbers[char]
        if current_value > previous_value:
            total += current_value - 2 * previous_value
        else:
            total += current_value
        previous_value = current_value

    return total
