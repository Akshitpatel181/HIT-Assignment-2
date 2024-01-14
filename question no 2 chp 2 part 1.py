def separate_and_convert(s):
    """
    Separates numbers and letters from the input string and converts even numbers to ASCII values,
    and upper-case letters to their ASCII values.

    Parameters:
    s (str): Input string containing both numbers and letters.

    Returns:
    str: String of even numbers.
    str: String of upper-case letters.
    list: ASCII values of even numbers.
    list: ASCII values of upper-case letters.
    """

    # Separate numbers and letters
    number_string = ''.join([char for char in s if char.isdigit()])
    letter_string = ''.join([char for char in s if char.isalpha()])

    # Convert even numbers to ASCII Code Decimal Values
    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    ascii_values_numbers = [ord(str(num)) for num in even_numbers]

    # Convert upper-case letters to ASCII Code Decimal Values
    upper_case_letters = [char for char in letter_string if char.isupper()]
    ascii_values_letters = [ord(char) for char in upper_case_letters]

    return ''.join(map(str, even_numbers)), ''.join(map(str, upper_case_letters)), ascii_values_numbers, ascii_values_letters

# Example usage
input_string = 'AKSHITpatel1213'
result_numbers, result_letters, ascii_numbers, ascii_letters = separate_and_convert(input_string)

print("Number String:", result_numbers)
print("Letter String:", result_letters)
print("ASCII Values of Even Numbers:", ascii_numbers)
print("ASCII Values of Upper-case Letters:", ascii_letters)
