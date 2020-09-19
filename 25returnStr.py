# middleSubstring("A") --> A
# middleSubstring("AB") --> A
# middleSubstring("ABC") --> B
# middleSubstring("ABCD") --> BC
# middleSubstring("ABCDE") --> BC
# middleSubstring("ABCDEF") --> CDE
# middleSubstring("ABCDEFG") --> CDE
# middleSubstring("ABCDEFGH") --> CDEF
# middleSubstring("ABCDEFGHI") --> CDEF
# middleSubstring("ABCDEFGHIJ") --> DEFGH
# middleSubstring("ABCDEFGHIJK") --> DEFGH
# middleSubstring("ABCDEFGHIJKL") --> DEFGHI
# middleSubstring("fundamental") --> damen

import math

def middleSubstring(string):
    #ここから書きましょう
    halfLength = math.floor(len(string) / 2)
    start = math.ceil(halfLength/2)
    end = start + halfLength

    if len(string) <= 2:
        return string[0]
    else:
        return string[start: end]

print(middleSubstring("A"))
print(middleSubstring("AB"))
print(middleSubstring("ABC"))
print(middleSubstring("ABCD"))
print(middleSubstring("ABCDE"))
print(middleSubstring("ABCDEF"))
print(middleSubstring("ABCDEFG"))
print(middleSubstring("ABCDEFGH"))
print(middleSubstring("ABCDEFGHI"))
print(middleSubstring("ABCDEFGHIJ"))
print(middleSubstring("ABCDEFGHIJK"))
print(middleSubstring("ABCDEFGHIJKL"))
# print(middleSubstring("fundamental"))
# test