def goes_after(word: str, first: str, second: str) -> bool:
    if first not in word or second not in word or first == second:
        return False

    first_index = word.find(first)
    return first_index < len(word) - 1 and word[first_index + 1] == second


print("Example:")
print(goes_after("world", "w", "o"))

assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("All test cases passed!")
