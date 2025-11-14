def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 1 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        return tens[n // 10] + (ones[n % 10] if n % 10 != 0 else "")
    elif n == 100:
        return "onehundred"
    return ""


def f(x):
    return len(number_to_words(x))

x = int(input())

for _ in range(1000):
    x = f(x)

print(x)