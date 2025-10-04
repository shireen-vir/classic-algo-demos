def max_min_composition(A, R, Y):
    """Max-Min Composition"""
    result = {}
    for y in Y:
        values = []
        for x in A:
            muA = A[x]
            muR = R.get((x, y), 0)
            values.append(min(muA, muR))
        result[y] = max(values)
    return result

def max_product_composition(A, R, Y):
    """Max-Product Composition"""
    result = {}
    for y in Y:
        values = []
        for x in A:
            muA = A[x]
            muR = R.get((x, y), 0)
            values.append(muA * muR)
        result[y] = max(values)
    return result


def main():
    print("=== Fuzzy Composition Operations ===")

    A = {}
    nA = int(input("Enter number of elements in fuzzy set A (on X): "))
    for i in range(nA):
        elem = input(f"Enter element {i+1} of X: ")
        mu = float(input(f"Enter membership value of {elem} (0-1): "))
        A[elem] = mu

    R = {}
    nR = int(input("\nEnter number of relation pairs in R (X × Y): "))
    Y_elements = set()
    for i in range(nR):
        x = input(f"Enter X element for pair {i+1}: ")
        y = input(f"Enter Y element for pair {i+1}: ")
        mu = float(input(f"Enter membership value for R({x},{y}) (0-1): "))
        R[(x, y)] = mu
        Y_elements.add(y)

    Y = list(Y_elements)

    print("\n--- Results ---")
    print("Fuzzy Set A:", A)
    print("Fuzzy Relation R:", R)
    print("Set Y:", Y)

    max_min = max_min_composition(A, R, Y)
    max_prod = max_product_composition(A, R, Y)

    print("\nMax-Min Composition Result (B):", max_min)
    print("Max-Product Composition Result (B):", max_prod)


if __name__ == "__main__":
    main()
