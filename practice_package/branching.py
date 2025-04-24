def is_weekend(day):
    return day == 6 or day == 7


def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.10, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    else:
        return 0


def describe_number(n):
    even_str = "четное" if n % 2 == 0 else "нечетное"
    if 0 <= n <= 9:
        rank_str = "однозначное"
    elif 10 <= n <= 99:
        rank_str = "двузначное"
    elif 100 <= n <= 999:
        rank_str = "трехзначное"
    else:
        rank_str = ""
    return f"{even_str} {rank_str} число"


def convert_to_meters(unitNumber, lengthInUnits):
    if unitNumber == 1:
        return lengthInUnits * 0.1
    elif unitNumber == 2:
        return lengthInUnits * 1000
    elif unitNumber == 3:
        return lengthInUnits
    elif unitNumber == 4:
        return lengthInUnits * 0.001
    elif unitNumber == 5:
        return lengthInUnits * 0.01
    else:
        return 0


def describe_age(age):
    units = [
        '', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять'
    ]
    teens = [
        'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
        'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'
    ]
    tens = [
        '', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'
    ]
    hundreds = [
        '', 'сто'
    ]

    def number_words(n):
        if n == 100:
            return "сто"
        if 10 <= n <= 19:
            return teens[n - 10]
        ten = n // 10
        unit = n % 10
        result = []
        if ten > 0:
            result.append(tens[ten])
        if unit > 0:
            result.append(units[unit])
        return " ".join(result).strip()

    def word_years(n):
        if 11 <= n % 100 <= 14:
            return "лет"
        last = n % 10
        if last == 1:
            return "год"
        elif 2 <= last <= 4:
            return "года"
        else:
            return "лет"

    return f"{number_words(age)} {word_years(age)}"