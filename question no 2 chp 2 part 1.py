def separate_string(s):
    num_str = ""
    letter_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
        elif char.isalpha():
            letter_str += char
    return num_str, letter_str


def ascii_conversion(num_str, letter_str):
    even_numbers = [int(num) for num in num_str if int(num) % 2 == 0]
    uppercase_letters = [ord(letter) for letter in letter_str if letter.isupper()]
    return even_numbers, uppercase_letters


def decrypt_ciphered_quote(ciphered_quote, s):
    decrypted_quote = ""
    for char in ciphered_quote:
        if char.isalpha():
            decrypted_quote += chr((ord(char) - 65 + s) % 26 + 65)
        else:
            decrypted_quote += char
    return decrypted_quote


input_string = "56aAww1984sktr235270aYmn145ss785fsq31D0"
num_str, letter_str = separate_string(input_string)
even_numbers, uppercase_letters = ascii_conversion(num_str, letter_str)

# Try shift key values from 1 to 25
for s in range(1, 26):
    decrypted_quote = decrypt_ciphered_quote("VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR", s)
    if "FAMOUS QUOTE FROM A CELEBRITY" in decrypted_quote:
        print(f"Original quote: {decrypted_quote}\nShift key value (s): {s}")
        break