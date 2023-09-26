
numbers = [28, 25, 42, 2, 27, 6565]

def getSmaller(numbers):
    """Get the smallest number."""

    if len(numbers) == 0:
        return None

    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

print(getSmaller(numbers))