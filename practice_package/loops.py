def sum_even_digits(number):
    total = 0
    for digit in str(abs(number)):
        n = int(digit)
        if n % 2 == 0:
            total += n
    return total

def count_vowel_triplets(text):
    vowels = set("aeiouy")
    text_lower = text.lower()
    count = 0
    i = 0
    while i <= len(text_lower) - 3:
        window = text_lower[i:i+3]
        if all(c in vowels for c in window):
            count += 1
            i += 3  # skip to next non-overlapping window
        else:
            i += 1
    return count



def find_fibonacci_index(number):
    if number < 1:
        return -1
    a, b = 1, 1
    index = 1
    if number == 1:
        return 1
    while a < number:
        a, b = b, a + b
        index += 1
    if a == number:
        return index
    return -1

def remove_duplicates(string):
    if not string:
        return ""
    result = [string[0]]
    for ch in string[1:]:
        if ch != result[-1]:
            result.append(ch)
    return ''.join(result)