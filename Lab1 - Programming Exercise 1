def mean(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

def median(numbers):
    if len(numbers) == 0:
        return None
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[ n // 2]) / 2 
    else:
        return numbers[n // 2]

def mode(numbers):
    if len(numbers) == 0:
        return None
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    if len(modes) == 1:
        return modes[0]
    return None

if __name__ == "__main__":
    # Input a list of numbers
    print("Input a list of numbers (type 'x' to finish):")
    numbers = []
    while True:
        user_input = input("> ")
        if user_input.lower() == "x":
            break
        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Please enter a valid number or 'x' to finish.")

    print("\nResults:")
    print("Mean:", mean(numbers) if numbers else "N/A")
    print("Median:", median(numbers) if numbers else "N/A")
    mode_result = mode(numbers)
    if mode_result is not None:
        print("Mode:", mode_result)
    else:
        print("Mode: No mode was found.")
