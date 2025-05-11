# hw3

## Part A

### 1. rotateString(s, k) [5 pts]

> Write the function rotateString(s, k) that takes a string s and a possibly-negative integer k. If k is non-negative, the function returns the string s rotated k places to the left. If k is negative, the function returns the string s rotated |k| places to the right.

```python
def rotateString(s, k):
    if k > 0:
        return s[k:] + s[:k]
    else:
        return s[(len(s)-k-2):] + s[:(len(s)-k-2)]
```

### 2. applyCaesarCipher(message, shift) [5 pts]

> A Caesar Cipher is a simple cipher that works by shifting each letter in the given message by a certain number. For example, if we shift the message "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo".

> Write the function applyCaesarCipher(message, shift) which shifts the given message by shift letters. You are guaranteed that message is a string, and that shift is an integer between -25 and 25. Capital letters should stay capital and lowercase letters should stay lowercase, and non-letter characters should not be changed. Note that "Z" wraps around to "A".

```python
def applyCaesarCipher(message, shift):
    cipherText = ""
    for ch in message:
        finalLetter = ch
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            if stayInAlphabet < ord('a'):
                stayInAlphabet += 26
            finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    return cipherText
```

### 3. largestNumber(text) [5 pts]

> largestNumber: Write the function largestNumber(text) that takes a string of text and returns the largest int value that occurs within that text, or None if no such value occurs. You may assume that the only numbers in the text are non-negative integers and that numbers are always composed of consecutive digits (without commas, for example).

```python
def largestNumber(s):
    temp = 0
    f = False
    ans = 0
    for ch in s:
        if ch.isnumeric():
            f = True
            temp = temp * 10 + int(ch)
        else:
            if ans < temp:
                ans = temp
            temp = 0
    return None if f == False else ans
```

### 4. topScorer(data) [5 pts]

> Write the function topScorer(data) that takes a multi-line string encoding scores as csv data for some kind of competition with players receiving scores, so each line has comma-separated values. The first value on each line is the name of the player (which you can assume has no integers in it), and each value after that is an individual score (which you can assume is a non-negative integer). You should add all the scores for that player, and then return the player with the highest total score. If there is a tie, return all the tied players in a comma-separated string with the names in the same order they appeared in the original data. If nobody wins (there is no data), return None (not the string "None").

```python
def topScorer(data):
    if not data.strip():  # Handle empty input
        return None
    
    lines = data.splitlines()
    max_score = 0
    top_players = []
    
    for line in lines:
        parts = line.split(',')
        name = parts[0]
        scores = map(int, parts[1:])
        total_score = sum(scores)
        
        if total_score > max_score:
            max_score = total_score
            top_players = [name]  # New top scorer
        elif total_score == max_score:
            top_players.append(name)  # Tie, add to the list
    
    return ','.join(top_players) if top_players else None
```

## Part B

### 6. collapseWhitespace(s) [10 pts]
Without using the s.replace() method, write the function collapseWhitespace(s), that takes a string s and returns an equivalent string except that each occurrence of whitespace in the string is replaced by a single space. So, for example, `collapseWhitespace("a\t\t\tb\n\nc")` replaces the three tabs with a single space, and the two newlines with another single space , returning "a b c".

```python
def collapseWhitespace(s):
    ans = ""
    lastPos = False
    for i in range(0, len(s)):
        if s[i].isalpha() and s[i] != '\\':
            ans += (s[i] + ' ')
            lastPos = False
        elif s[i] == ' ':
            lastPos = True
    return ans[:len(ans)-1] if lastPos == False else ans
```

### 7. patternedMessage(message, pattern) [15 pts]

> Write the function patternedMessage(message, pattern) that takes two strings, a message and a pattern, and returns a string produced by replacing the non-whitespace characters in the pattern with the non-whitespace characters in the message.


```python
def patternedMessage(msg, pattern):
    pattern = pattern.strip()
    filtered_message = ''.join(c for c in msg if not c.isspace())
    result = []
    message_index = 0
    for char in pattern:
        if char.isspace():
            result.append(char)
        else:
            result.append(filtered_message[message_index])
            message_index = (message_index + 1) % len(filtered_message)
    return ''.join(result)
```

!!! warning

    This function can't process some outlier input.


8. encodeRightLeftRouteCipher(message,rows) [15 pts]

> Background: A right-left route cipher is a fairly simple way to encrypt a message. It takes two values, some plaintext and a number of rows, and it first constructs a grid with that number of rows and the minimum number of columns required, writing the message in successive columns. For example, if the message is WEATTACKATDAWN, with 4 rows, the grid would be:

```text
    W T A W
    E A T N
    A C D
    T K A
```
> We will assume the message only contains uppercase letters. We'll fill in the missing grid entries with lowercase letters starting from z and going in reverse (wrapping around if necessary), so we have:

```text
    W T A W
    E A T N
    A C D z
    T K A y
```

> Next, we encrypt the text by reading alternating rows first to the right ("WTAW"), then to the left ("NTAE"), then back to the right ("ACDz"), and back to the left ("yAKT"), until we finish all rows. We precede these values with the number of rows itself in the string. So the encrypted value for the message WEATTACKATDAWN with 4 rows is `4WTAWNTAEACDzyAKT`.


```python
def encodeRightLeftRouteCipher(text, rows):
    import math

    cols = math.ceil(len(text) / rows)
    grid = [[''] * cols for _ in range(rows)]
    index = 0
    for col in range(cols):
        for row in range(rows):
            if index < len(text):
                grid[row][col] = text[index]
                index += 1

    filler = iter(chr(x) for x in range(ord('z'), ord('a') - 1, -1))
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '':
                grid[row][col] = next(filler)

    encoded_message = []
    for i, row in enumerate(grid):
        encoded_message.extend(row) if i % 2 == 0 else encoded_message.extend(row[::-1])

    return f"{rows}{''.join(encoded_message)}"
```

### 8. decodeRightLeftRouteCipher(message) [5 pts]

> Write the function decodeRightLeftRouteCipher, which takes an encoding from the previous problem and runs it in reverse, returning the plaintext that generated the encoding. For example, `decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT")` returns `WEATTACKATDAWN`.

```python
# Literally the same as Q8.
```