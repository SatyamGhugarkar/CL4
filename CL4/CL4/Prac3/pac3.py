# Matrix Multiplication using MapReduce

from collections import defaultdict

# Mapper
def mapper(name, row, col, value, n):
    result = []

    if name == "A":
        for k in range(n):
            result.append(((row, k), ("A", col, value)))

    else:
        for i in range(n):
            result.append(((i, col), ("B", row, value)))

    return result

# Reducer
def reducer(values):
    A = {}
    B = {}

    for name, index, value in values:

        if name == "A":
            A[index] = value
        else:
            B[index] = value

    total = 0

    for j in A:
        if j in B:
            total += A[j] * B[j]

    return total


# Main
n = 2

A = [
    (0, 0, 1),
    (0, 1, 2),
    (1, 0, 3),
    (1, 1, 4)
]

B = [
    (0, 0, 5),
    (0, 1, 6),
    (1, 0, 7),
    (1, 1, 8)
]

mapped = []

# Map phase
for r, c, v in A:
    mapped.extend(mapper("A", r, c, v, n))

for r, c, v in B:
    mapped.extend(mapper("B", r, c, v, n))

# Shuffle phase
grouped = defaultdict(list)

for key, value in mapped:
    grouped[key].append(value)

# Reduce phase
print("Result Matrix:\n")

for key in sorted(grouped):
    print(f"C{key} =", reducer(grouped[key]))