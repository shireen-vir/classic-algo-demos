def fuzzy_union(A, B):
    result = {}
    for x in set(A) | set(B):
        result[x] = max(A.get(x, 0), B.get(x, 0))
    return result

def fuzzy_intersection(A, B):
    result = {}
    for x in set(A) | set(B):
        result[x] = min(A.get(x, 0), B.get(x, 0))
    return result

def fuzzy_complement(A):
    result = {}
    for x in A:
        result[x] = 1 - A[x]
    return result


def main():
    print("=== Fuzzy De Morgan's Law Demo ===")

    A = {}
    nA = int(input("Enter number of elements in Set A: "))
    for i in range(nA):
        elem = input(f"Enter element {i+1} of A: ")
        mu = float(input(f"Enter membership value of {elem} (0-1): "))
        A[elem] = mu

    B = {}
    nB = int(input("\nEnter number of elements in Set B: "))
    for i in range(nB):
        elem = input(f"Enter element {i+1} of B: ")
        mu = float(input(f"Enter membership value of {elem} (0-1): "))
        B[elem] = mu

    # Law 1: (A ∪ B)' = A' ∩ B'
    left1 = fuzzy_complement(fuzzy_union(A, B))
    right1 = fuzzy_intersection(fuzzy_complement(A), fuzzy_complement(B))

    # Law 2: (A ∩ B)' = A' ∪ B'
    left2 = fuzzy_complement(fuzzy_intersection(A, B))
    right2 = fuzzy_union(fuzzy_complement(A), fuzzy_complement(B))

    # --- Display Results ---
    print("\n--- Results ---")
    print("Set A:", A)
    print("Set B:", B)
    print("\nLaw 1: (A ∪ B)' = A' ∩ B'")
    print("Left Side :", left1)
    print("Right Side:", right1)
    print("\nLaw 2: (A ∩ B)' = A' ∪ B'")
    print("Left Side :", left2)
    print("Right Side:", right2)


if __name__ == "__main__":
    main()
