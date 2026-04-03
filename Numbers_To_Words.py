def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 0:
        return "zero"

    elif n < 20:
        return ones[n]

    elif n < 100:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")

    elif n < 1000:
        return ones[n // 100] + " hundred" + (
            " " + number_to_words(n % 100) if n % 100 != 0 else "")

    else:
        return "Number out of range"


# Input
n = int(input("Enter a number: "))

# Print from 1 to n
for i in range(1, n + 1):
    print(number_to_words(i))
