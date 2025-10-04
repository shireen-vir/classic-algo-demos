import cryptocode
import hashlib
import base64


def main():
    print("=== Security Operations Demo ===")

    text = input("Enter the text: ")
    secret_key = "my_secret_key"   # You can also take this from user if needed

    encrypted_text = cryptocode.encrypt(text, secret_key)
    decrypted_text = cryptocode.decrypt(encrypted_text, secret_key)

    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()

    encoded_b64 = base64.b64encode(text.encode()).decode()
    decoded_b64 = base64.b64decode(encoded_b64).decode()

    print("\n--- Results ---")
    print(f"Original Text       : {text}")
    print(f"Encrypted Text      : {encrypted_text}")
    print(f"Decrypted Text      : {decrypted_text}")
    print(f"MD5 Digest          : {md5_hash}")
    print(f"SHA256 Digest       : {sha256_hash}")
    print(f"Base64 Encoded      : {encoded_b64}")
    print(f"Base64 Decoded      : {decoded_b64}")


if __name__ == "__main__":
    main()
