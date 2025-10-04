def rail_fence_encrypt(text, key):
    # Create the matrix to encrypt the message
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]
     
    # To determine the direction
    dir_down = False
    row, col = 0, 0
     
    for ch in text:
        # check the direction of flow
        if row == 0 or row == key - 1:
            dir_down = not dir_down
         
        # place the character
        rail[row][col] = ch
        col += 1
         
        # find the next row
        row += 1 if dir_down else -1
     
    # construct the cipher
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)


def columnar_encrypt(text, key):
    # Remove spaces
    text = text.replace(" ", "")
    
    # Number of columns
    key_len = len(key)
    
    # Padding to fill the matrix evenly
    extra = len(text) % key_len
    if extra != 0:
        text += "_" * (key_len - extra)  # Using '_' as padding
    
    # Create the matrix
    matrix = [list(text[i:i+key_len]) for i in range(0, len(text), key_len)]
    
    # Order of columns (based on alphabetical order of key)
    order = sorted(list(enumerate(key)), key=lambda x: x[1])
    order_index = [idx for idx, char in order]
    
    # Read column by column in order
    cipher = ""
    for idx in order_index:
        for row in matrix:
            cipher += row[idx]
    
    return cipher


def main():
    print("Choose Transposition Cipher Technique:")
    print("1. Rail Fence Cipher")
    print("2. Columnar Cipher")

    choice = input("Enter your choice (1/2): ").strip()
    text = input("Enter the text to encrypt: ")

    if choice == "1":
        key = int(input("Enter Rail Fence Key (number of rails): "))
        encrypted = rail_fence_encrypt(text, key)
        print("Encrypted Text (Rail Fence):", encrypted)

    elif choice == "2":
        key = input("Enter Columnar Key (word for column order): ")
        encrypted = columnar_encrypt(text, key)
        print("Encrypted Text (Columnar):", encrypted)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
