# This program will decrypt the encrypted code by revealing the key and storing the decrypted code in text file

# Decryption function

def decrypt(encrypted_code, key):
    original_code = ""
    for char in encrypted_code:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            original_code += chr(shifted)
        else:
            original_code += char
    return original_code


# Calculating the key

total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2
print("Key:", total)

# Decrypting the encrypted code

with open('encrypted code.txt', 'r') as encrypted_text: # reading the encrypted code
   encrypted_code = encrypted_text.read()

original_code = decrypt(encrypted_code, total)  # decrypting the code

with open("decrypted code.txt", "w") as file:  # writing the decrypted code in text file
    file.write(original_code)