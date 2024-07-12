def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print("Example:")
print(factorial(4))

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000

print("The mission is done! Click 'Check Solution' to earn rewards!")
