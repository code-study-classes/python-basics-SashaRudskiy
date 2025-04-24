# dicts.py

def count_char_occurrences(text):
    # Подсчет буквенных символов (регистр не важен)
    text = text.lower()
    result = {}
    for ch in text:
        if ch.isalpha():
            result[ch] = result.get(ch, 0) + 1
    return result

def merge_dicts(dict1, dict2, conflict_resolver):
    # Объединение с учётом конфликтов
    result = dict(dict1)
    for key, val2 in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], val2)
        else:
            result[key] = val2
    return result

def invert_dictionary(original_dict):
    # Ключи становятся значениями, значения -- ключами. Несколько ключей в списке.
    result = {}
    for k, v in original_dict.items():
        if v in result:
            result[v].append(k)
        else:
            result[v] = [k]
    return result

def dict_to_table(data_dict, columns):
    # columns -- порядок вывода, значения -- str, отсутствующие -- "N/A", выравнивание
    columns_upper = [col.upper() for col in columns]
    rows = []

    # Строим строки данных
    for id in data_dict:
        row = []
        for col in columns:
            value = data_dict[id].get(col, "N/A")
            row.append(str(value))
        rows.append(row)

    # Собираем все строки
    table = [columns_upper] + rows

    # Вычисляем ширину по каждому столбцу
    col_widths = []
    for col_ix in range(len(columns)):
        max_len = max(len(table[r][col_ix]) for r in range(len(table)))
        col_widths.append(max_len)
    
    # Форматируем таблицу строками
    lines = []
    # Шапка
    header = "| " + " | ".join(table[0][col_ix].ljust(col_widths[col_ix]) for col_ix in range(len(columns))) + " |"
    lines.append(header)
    # Разделитель
    sep = "|-" + "-|-".join("-" * col_widths[col_ix] for col_ix in range(len(columns))) + "-|"
    lines.append(sep)
    # Данные
    for row in table[1:]:
        line = "| " + " | ".join(row[col_ix].ljust(col_widths[col_ix]) for col_ix in range(len(columns))) + " |"
        lines.append(line)
    return "\n".join(lines)

def deep_update(base_dict, update_dict):
    # Копируем базовый словарь
    import copy
    res = copy.deepcopy(base_dict)
    for k, v in update_dict.items():
        if k in res and isinstance(res[k], dict) and isinstance(v, dict):
            res[k] = deep_update(res[k], v)
        else:
            res[k] = v
    return res