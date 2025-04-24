def square_odds(numbers):
    # Возвращает список квадратов нечётных чисел
    return [n ** 2 for n in numbers if n % 2 != 0]


def normalize_names(names):
    # Нормализует имена: первая буква заглавная, остальные строчные
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    # Оставляет только валидные email по условиям задания
    def is_valid(email):
        return (
            email.count("@") == 1
            and len(email) >= 5
            and not email.startswith("@")
            and not email.endswith("@")
        )
    return [email for email in emails if is_valid(email)]


def filter_palindromes(words):
    # Оставляет только палиндромы (регистр не важен)
    return [word for word in words if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    # Факториал числа (n >= 0)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def find_common_prefix(strings):
    # Если список пуст, вернуть ""
    if not strings:
        return ""
    # Берём первую строку как стартовый префикс
    prefix = strings[0]
    for s in strings[1:]:
        # Укорачиваем prefix, пока не станет префиксом s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix