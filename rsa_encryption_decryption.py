import rsa

def main():
    print("=== RSA Password Encryption Demo ===")
    
    # Step 1: Accept username and password
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Step 2: Generate RSA key pair (public and private keys)
    public_key, private_key = rsa.newkeys(512)  # 512-bit key size for demo

    # Step 3: Encrypt password using the public key
    encrypted_password = rsa.encrypt(password.encode(), public_key)

    # Step 4: Decrypt password using the private key
    decrypted_password = rsa.decrypt(encrypted_password, private_key).decode()

    # Step 5: Display results
    print("\n--- Output ---")
    print(f"Username            : {username}")
    print(f"Password            : {password}")
    print(f"Encrypted Password  : {encrypted_password}")
    print(f"Decrypted Password  : {decrypted_password}")


if __name__ == "__main__":
    main()
