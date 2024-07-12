def to_title_case(sentence: str) -> str:
    words = sentence.split()
    title_case_words = [word.capitalize() for word in words]
    return ' '.join(title_case_words)


print("Example:")
print(to_title_case("hello world"))

assert to_title_case("hello world") == "Hello World"
assert to_title_case("openai gpt-4") == "Openai Gpt-4"
assert to_title_case("this is a title") == "This Is A Title"
assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"
assert to_title_case("JUMPs ovER a LAZy dog") == "Jumps Over A Lazy Dog"
assert to_title_case("typescript is great") == "Typescript Is Great"
assert to_title_case("the answer is 42") == "The Answer Is 42"
assert to_title_case("to be or not to be") == "To Be Or Not To Be"
assert to_title_case("that is the question") == "That Is The Question"
assert to_title_case("") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
