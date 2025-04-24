def check_between_numbers(A, B, C):
    """
    Проверяет, находится ли число B строго между A и C.
    """
    return (A < B < C) or (C < B < A)

def check_odd_three(number):
    """
    Проверяет, является ли число нечетным трехзначным.
    """
    abs_num = abs(number)
    return 100 <= abs_num <= 999 and abs_num % 2 == 1

def check_unique_digits(number):
    """
    Проверяет, что все цифры в трехзначном числе уникальны.
    """
    abs_num = abs(number)
    num_str = str(abs_num)
    if len(num_str) != 3:
        return False
    return len(set(num_str)) == 3

def check_palindrome_number(number):
    """
    Проверяет, является ли число палиндромом, включая отрицательные числа.
    """
    num_str = str(abs(number))
    return num_str == num_str[::-1]

def check_ascending_digits(number):
    """
    Проверяет, образуют ли цифры числа строго возрастающую последовательность.
    """
    abs_num = abs(number)
    num_str = str(abs_num)
    if len(num_str) != 3:
        return False
    return num_str[0] < num_str[1] < num_str[2]