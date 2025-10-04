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

def fuzzy_algebraic_sum(A, B):
    result = {}
    for x in set(A) | set(B):
        muA = A.get(x, 0)
        muB = B.get(x, 0)
        result[x] = muA + muB - (muA * muB)
    return result

def fuzzy_algebraic_product(A, B):
    result = {}
    for x in set(A) | set(B):
        muA = A.get(x, 0)
        muB = B.get(x, 0)
        result[x] = muA * muB
    return result

def fuzzy_cartesian_product(A, B):
    result = {}
    for x in A:
        for y in B:
            result[(x, y)] = min(A[x], B[y])
    return result


def main():
    print("=== Fuzzy Set Operations ===")

    A = {}
    nA = int(input("Enter number of elements in Set A: "))
    for i in range(nA):
        elem = input(f"Enter element {i+1} of A: ")
        mu = float(input(f"Enter membership value of {elem} (0 to 1): "))
        A[elem] = mu

    B = {}
    nB = int(input("\nEnter number of elements in Set B: "))
    for i in range(nB):
        elem = input(f"Enter element {i+1} of B: ")
        mu = float(input(f"Enter membership value of {elem} (0 to 1): "))
        B[elem] = mu

    print("\n--- Results ---")
    print("Set A:", A)
    print("Set B:", B)
    print("Union:", fuzzy_union(A, B))
    print("Intersection:", fuzzy_intersection(A, B))
    print("Complement of A:", fuzzy_complement(A))
    print("Algebraic Sum:", fuzzy_algebraic_sum(A, B))
    print("Algebraic Product:", fuzzy_algebraic_product(A, B))
    print("Cartesian Product:", fuzzy_cartesian_product(A, B))


if __name__ == "__main__":
    main()
