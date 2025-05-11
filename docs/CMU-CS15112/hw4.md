# hw4

## Part A

### 1. alternatingSum(a) [6 pts]

> Write the function alternatingSum(a) that takes a list of numbers and returns the alternating sum (where the sign alternates from positive to negative or vice versa). For example, `alternatingSum([5,3,8,4])` returns 6 (that is, 5-3+8-4). If the list is empty, return 0.

```python
def alternatingSum(a):
    if not a:
        return 0
    result = 0
    for i in range(len(a)):
        if i % 2 == 0:
            result += a[i]
        else:
            result -= a[i]
    return result
```

### 2. median(a) [6 pts]

> Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, which is the value of the middle element, or the average of the two middle elements if there is no single middle element. If the list is empty, return None. Do not use `statistics.median()` here.


```python
def median(a):
    if not a:
        return None
    sorted_a = sorted(a)
    n = len(sorted_a)
    mid = n // 2 
    return sorted_a[mid] if n % 2 == 1 else ((sorted_a[mid - 1] + sorted_a[mid]) / 2)
```

### 3. smallestDifference(a) [6 pts]

>  Write the function smallestDifference(a) that takes a list of integers and returns the smallest absolute difference between any two integers in the list. If the list is empty, return -1.

```python
def smallestDifference(a):
    if not a:
        return -1
    
    sorted_a = sorted(a)
    res = 2 ** 63 - 1
    for i in range(len(sorted_a) - 1):
        if sorted_a[i + 1] - sorted_a[i] < res:
            res = sorted_a[i + 1] - sorted_a[i]
    return res
```

### 4. nondestructiveRemoveRepeats(L) [6 pts]

> Write the function nondestructiveRemoveRepeats(L), which takes a list L and nondestructively returns a new list in which any repeating elements in L are removed.

```python
def nondestructiveRemoveRepeats(L):
    seen = set()
    result = []
    for item in L:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

### 5. destructiveRemoveRepeats(L) [6 pts]

> Write the function destructiveRemoveRepeats(L), which implements the same function destructively. Thus, this function should directly modify the provided list to not have any repeating elements. Since this is a destructive function, it should not return any value at all (so, implicitly, it should return None).


```python
def destructiveRemoveRepeats(L):
    seen = set()
    i = 0
    while i < len(L):
        if L[i] in seen:
            L.pop(i)
        else:
            seen.add(L[i])
            i += 1
```

## Part B

### 7. isSorted(a) [10 pts]

> Write the function isSorted(a) that takes a list of numbers and returns True if the list is sorted (either smallest-first or largest-first) and False otherwise. Your function must only consider each value in the list once (so, in terms of big-oh, which we will learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort the list.


```python
def isSorted(a):
    if len(a) <= 1:
        return True

    increasing = True
    decreasing = True
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            decreasing = False
        if a[i] > a[i + 1]:
            increasing = False

    return increasing or decreasing
```

### 8. lookAndSay(a) [10 pts]

> First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say method, using tuples for each (count, value) pair.


```python
def lookAndSay(a):
    if not a:
        return []

    cnt = 1
    ans = []
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            cnt += 1
        else:
            ans.append((cnt, a[i]))
            cnt = 1
    ans.append((cnt, a[-1]))
    return ans
```

### 9. inverseLookAndSay(a) [10 pts]

> Write the function inverseLookAndSay(a) that does the inverse of the previous problem.


```python
def lookAndSay(a):
    if not a:
        return []

    cnt = 1
    ans = []
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            cnt += 1
        else:
            ans.append((cnt, a[i]))
            cnt = 1
    ans.append((cnt, a[-1]))
    return ans

def inverseLookAndSay(a):
    ans = []
    for cnt, num in a:
        for _ in range(cnt):
            ans.append(num)
    return ans
```

9. decodeRightLeftRouteCipher(message) [5 pts]

> Write the function decodeRightLeftRouteCipher, which takes an encoding from the previous problem and runs it in reverse, returning the plaintext that generated the encoding. For example, `decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT")` returns `WEATTACKATDAWN`.

```python
# Literally the same as Q8.
```