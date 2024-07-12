def replace_all(mainText: str, target: str, repl: str) -> str:
    return mainText.replace(target, repl)


print("Example:")
print(replace_all("hello world", "world", "TypeScript"))

assert replace_all("hello world", "world", "TypeScript") == "hello TypeScript"
assert replace_all("hello world world", "world", "TypeScript") == "hello TypeScript TypeScript"
assert replace_all("TypeScript is fun", "fun", "awesome") == "TypeScript is awesome"
assert replace_all("aaa", "a", "b") == "bbb"
assert replace_all("replace all the all", "all", "some") == "replace some the some"
assert replace_all("nothing to replace", "something", "nothing") == "nothing to replace"
assert replace_all("same same same", "same", "same") == "same same same"
assert replace_all("123 123", "123", "321") == "321 321"
assert replace_all("OpenAI", "AI", "Source") == "OpenSource"
assert replace_all("", "anything", "nothing") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
