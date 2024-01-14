
def decrypt(cryptogram, shift):
    """
    Decrypts a cryptogram using a specified Caesar cipher shift.

    Parameters:
    cryptogram (str): The encrypted text.
    shift (int): The shift key for decryption.

    Returns:
    str: The decrypted text.
    """
    decrypted_text = ''
    for char in cryptogram:
        if char.isalpha():
            # Shift the character by the specified amount
            decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A') if char.isupper() else
                                  (ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

def find_shift_key(cryptogram):
    """
    Finds the Caesar cipher shift key by checking for common words in the decrypted text.

    Parameters:
    cryptogram (str): The encrypted text.

    Returns:
    int or None: The found shift key or None if not found.
    """
    for shift in range(26):
        decrypted_text = decrypt(cryptogram, shift)
        # Check if the decrypted text contains common words or patterns
        if ' the ' in decrypted_text.lower() or ' and ' in decrypted_text.lower() or ' is ' in decrypted_text.lower():
            return shift
    return None

# Provided cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAONG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Find the shift key
shift_key = find_shift_key(cryptogram)

if shift_key is not None:
    # Decrypt the cryptogram using the found shift key
    original_quote = decrypt(cryptogram, shift_key)
    print("Shift Key:", shift_key)
    print("Original Quote:", original_quote)
else:
    print("Shift key not found.")
