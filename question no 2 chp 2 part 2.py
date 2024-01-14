# This program will decrypts the given cryptogram using different shift key and finds the correct shift key that gives the original quote.

# Decrypting the quote
def decrypt_ciphered_quote(ciphered_quote, s):
    decrypted_quote = ""
    for char in ciphered_quote:
        if char.isalpha():
            decrypted_quote += chr((ord(char) - 65 + s) % 26 + 65)
        else:
            decrypted_quote += char
    return decrypted_quote


input_string = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
s = 13
decrypted_quote = decrypt_ciphered_quote(input_string, s)
print(f"Original quote: {decrypted_quote}\nShift key value (s): {s}")







# we got the key by just counting by ourselves

# Try shift key values from 1 to 25
#for s in range(1, 26):
#    decrypted_quote = decrypt_ciphered_quote(input_string, s)
#    if "A" in decrypted_quote:
#        print(f"Original quote: {decrypted_quote}\nShift key value (s): {s}")
#        break