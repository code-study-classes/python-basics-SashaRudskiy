def calculate_distance(x1, x2):
    return abs(x2 - x1)


def calculate_segments(length_a, length_b):
    return length_a // length_b


def calculate_digit_sum(number):
    return sum(int(digit) for digit in str(abs(number)))


def calculate_rect_area(x1, y1, x2, y2):
    return abs(x2 - x1) * abs(y2 - y1)


def round_to_multiple(number, multiple):
    return int(multiple * round(float(number) / multiple))