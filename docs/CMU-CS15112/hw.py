def isMagicSquare(L):
    if not L or not all(isinstance(row, list) for row in L):
        return False
    n = len(L)
    if any(len(row) != n for row in L):
        return False

    all_elements = [element for row in L for element in row]
    if not all(isinstance(x, int) for x in all_elements):
        return False
    if len(all_elements) != len(set(all_elements)):
        return False

    target_sum = sum(L[0])

    for row in L:
        if sum(row) != target_sum:
            return False

    for col in range(n):
        if sum(L[row][col] for row in range(n)) != target_sum:
            return False

    if sum(L[i][i] for i in range(n)) != target_sum:
        return False
    if sum(L[i][n - 1 - i] for i in range(n)) != target_sum:
        return False

    return True