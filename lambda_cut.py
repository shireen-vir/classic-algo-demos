def lambda_cut(fuzzy_set, lam):
    """Perform lambda cut on a fuzzy set."""
    result = []
    for elem, mu in fuzzy_set.items():
        if mu >= lam:
            result.append(elem)
    return result


def main():
    print("=== Fuzzy Lambda-Cut Demo ===")

    fuzzy_set = {}
    n = int(input("Enter number of elements in the fuzzy set: "))
    for i in range(n):
        elem = input(f"Enter element {i+1}: ")
        mu = float(input(f"Enter membership value of {elem} (0-1): "))
        fuzzy_set[elem] = mu

    lam = float(input("\nEnter λ (lambda) value (0-1): "))

    cut_result = lambda_cut(fuzzy_set, lam)

    print("\n--- Results ---")
    print("Fuzzy Set :", fuzzy_set)
    print(f"Lambda (λ): {lam}")
    print("λ-cut Set :", cut_result)


if __name__ == "__main__":
    main()
