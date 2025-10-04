def diffie_hellman(p, g, private_key_alice, private_key_bob):
    """
    Implements the Diffie-Hellman Key Exchange
    Args:
        p (int): A large prime number
        g (int): A primitive root modulo p
        private_key_alice (int): Alice's private key
        private_key_bob (int): Bob's private key
    Returns:
        tuple: (shared_secret_alice, shared_secret_bob)
    """
    # Step 1: Alice computes her public key
    public_key_alice = pow(g, private_key_alice, p)

    # Step 2: Bob computes his public key
    public_key_bob = pow(g, private_key_bob, p)

    # Step 3: Alice computes the shared secret using Bob's public key
    shared_secret_alice = pow(public_key_bob, private_key_alice, p)

    # Step 4: Bob computes the shared secret using Alice's public key
    shared_secret_bob = pow(public_key_alice, private_key_bob, p)

    return public_key_alice, public_key_bob, shared_secret_alice, shared_secret_bob


def main():
    print("=== Diffie-Hellman Key Exchange Algorithm ===")

    # Input prime number and primitive root
    p = int(input("Enter a large prime number (p): "))
    g = int(input("Enter a primitive root modulo p (g): "))

    # Input private keys
    private_key_alice = int(input("Enter Alice's private key: "))
    private_key_bob = int(input("Enter Bob's private key: "))

    # Perform key exchange
    public_key_alice, public_key_bob, shared_secret_alice, shared_secret_bob = diffie_hellman(
        p, g, private_key_alice, private_key_bob
    )

    # Display results
    print("\n--- Results ---")
    print(f"Alice's Public Key: {public_key_alice}")
    print(f"Bob's Public Key: {public_key_bob}")
    print(f"Alice's Shared Secret: {shared_secret_alice}")
    print(f"Bob's Shared Secret: {shared_secret_bob}")

    # Verify both shared secrets are the same
    if shared_secret_alice == shared_secret_bob:
        print("\n✅ Key Exchange Successful! Shared Secret Established.")
    else:
        print("\n❌ Key Exchange Failed! Something went wrong.")


if __name__ == "__main__":
    main()
