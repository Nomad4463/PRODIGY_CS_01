
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Loop through each character in the text
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Shift character and wrap around if necessary
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, don't change it
            result += char
    
    return result

def main():
    text = input("Enter the text: ")
    
    shift = int(input("Enter the shift value: "))
    
    # User input for mode (encrypt or decrypt)
    mode = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return
    
    # Perform Caesar Cipher
    result = caesar_cipher(text, shift, mode)
    
    # Print the result
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
