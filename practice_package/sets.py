def find_common_elements(set1, set2):
    # Пересечение без оператора &
    return set1.intersection(set2)

def is_superset(set_a, set_b):
    # Является ли set_b подмножеством set_a без >=
    for el in set_b:
        if el not in set_a:
            return False
    return True

def remove_duplicates(items):
    # Удаляет дубликаты, сохраняя порядок
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def count_unique_words(text):
    # Считает уникальные слова (регистр не имеет значения)
    words = text.lower().split()
    return len(set(words))

def find_shared_items(*sets):
    # Пересечение произвольного количества множеств
    if not sets:
        return set()
    result = sets[0].copy()
    for s in sets[1:]:
        result = result.intersection(s)
        if not result:
            break
    return result