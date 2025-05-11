# hw4

## Part A

### 1. removeRowAndCol (non-destructive and destructive) [10 pts; 5 pts each]

> Here we will write removeRowAndCol twice -- once non-destructively, and then again destructively. Note that neither of these versions may call nor essentially duplicate the other version. So in particular, your nondestructive version may not do this:

```text
    L = copy.deepcopy(L)
    doDestructiveVersion(L)
    return L
```

> Instead, do not use copy.deepcopy and directly construct the modified 2d list.

> Both functions take a rectangular list L and two ints, row and col. In both cases, the goal is to obtain a version of the list that has the given row and given column removed. You may assume that row and col are both legal values (that is, they are non-negative integers that are smaller than the largest row and column, respectively). For example, the list shown to the left would lead to the result shown on the right when called with the row 1 and the column 2.

> nondestructiveRemoveRowAndCol(L, row, col): the non-destructive version should return a new list, and should not modify the provided list at all.

> destructiveRemoveRowAndCol(L, row, col): the destructive version should modify the original list, and should return None.

```python
def nondestructiveRemoveRowAndCol(L, row, col):
    return [
        [L[r][c] for c in range(len(L[0])) if c != col]
        for r in range(len(L)) if r != row
    ]

def destructiveRemoveRowAndCol(L, row, col):
    del L[row]
    for r in range(len(L)):
        del L[r][col]
    return None
```

### 2. matrixMultiply(m1, m2) [7.5 pts]

> Write the function matrixMultiply(m1, m2) that takes two 2d lists (that we will consider to be matrices) and returns a new 2d list that is the result of multiplying the two matrices. Return None if the two matrices cannot be multiplied for any reason (such as if their dimensions do not match). 


```python
def matrixMultiply(m1, m2):
    if len(m1[0]) != len(m2):
        return None

    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result
```

### 3. isKingsTour(board) [7.5 pts]

> Background: in Chess, a King can move from any square to any adjacent square in any of the 8 possible directions. A King's Tour is a series of legal King moves so that every square is visited exactly once. We can represent a Kings Tour in a 2d list where the numbers represent the order the squares are visited, going from 1 to N2.


```python
def isKingsTour(board):
    n = len(board)

    positions = {}
    for row in range(n):
        for col in range(n):
            value = board[row][col]
            if 1 <= value <= n**2:
                positions[value] = (row, col)
            else:
                return False

    if len(positions) != n**2:
        return False

    for i in range(1, n**2):
        r1, c1 = positions[i]
        r2, c2 = positions[i + 1]
        if abs(r1 - r2) > 1 or abs(c1 - c2) > 1:
            return False

    return True
```

## Part B

### 6. isMagicSquare(L) [15 pts]

> Write the function isMagicSquare(L) that takes an arbitrary list (that is, a possibly-empty, possibly-ragged, possibly-2d list of arbitrary values) and returns True if it is a magic square and False otherwise, where a magic square has these properties:

```
    The list is 2d, non-empty, square, and contains only integers, where no integer occurs more than once in the square.
    Each row, each column, and each of the 2 diagonals each sum to the same total. Note that we are not requiring that the integers are strictly in the range from 1 to n for some n. We are just requiring that the integers are unique and that the sums are all the same.
```


```python
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
```