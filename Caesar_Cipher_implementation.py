def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

# --- User interaction ---
text = input("Enter text: ")
choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
shift = int(input("Enter shift (1-25): "))

if choice == 'e':
    result = encrypt(text, shift)
    print("Encrypted:", result)
elif choice == 'd':
    result = decrypt(text, shift)
    print("Decrypted:", result)
else:
    print("Invalid choice! Enter 'e' for encrypt or 'd' for decrypt.")
