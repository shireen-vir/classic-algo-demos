def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result


def modified_caesar_cipher(text, shift):
    return caesar_cipher(text, shift)


def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char not in used and char.isalpha():
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J is merged with I
        if char not in used:
            used.add(char)
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    if char == "J":
        char = "I"
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def playfair_cipher(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])

    # Break text into digraphs
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            digraphs.append(a + "X")
            i += 1
        else:
            digraphs.append(a + b)
            i += 2

    encrypted = ""
    for pair in digraphs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        if row1 == row2:  # same row
            encrypted += matrix[row1][(col1 + 1) % 5]
            encrypted += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # same column
            encrypted += matrix[(row1 + 1) % 5][col1]
            encrypted += matrix[(row2 + 1) % 5][col2]
        else:  # rectangle rule
            encrypted += matrix[row1][col2]
            encrypted += matrix[row2][col1]

    return encrypted


def main():
    print("Choose Cipher Technique:")
    print("1. Caesar Cipher (Shift = 3)")
    print("2. Modified Caesar Cipher (User-defined shift)")
    print("3. Playfair Cipher")

    choice = input("Enter your choice (1/2/3): ").strip()
    text = input("Enter the text to encrypt: ")

    if choice == "1":
        encrypted = caesar_cipher(text)
        print("Encrypted Text (Caesar Cipher):", encrypted)

    elif choice == "2":
        shift = int(input("Enter shift value: "))
        encrypted = modified_caesar_cipher(text, shift)
        print("Encrypted Text (Modified Caesar Cipher):", encrypted)

    elif choice == "3":
        key = input("Enter Playfair cipher key: ")
        encrypted = playfair_cipher(text, key)
        print("Encrypted Text (Playfair Cipher):", encrypted)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
