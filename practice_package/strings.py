import os

def extract_file_name(path):
    filename = os.path.basename(path)
    if '.' in filename:
        return filename.split('.')[0]
    return filename

def encrypt_sentence(s):
    vowels = 'aeiouAEIOU'
    lo_vowels = [c for c in s if c in 'aeiou']
    consonants = [c for c in s if c.isalpha() and c not in vowels]
    up_vowels = [c for c in s if c in 'AEIOU']
    others = [(i, c) for i, c in enumerate(s) if not c.isalpha()]
    result = lo_vowels + consonants + up_vowels
    for i, c in others:
        result.insert(i, c)
    return ''.join(result)

def check_brackets(s):
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if not stack:
```

> ChatGPT + Midjourney:
```

                return i
            stack.pop()
    if stack:
        return stack[0]
    return 0

def reverse_domain(domain):
    return '.'.join(domain.split('.')[::-1])

def count_vowel_groups(word):
    vowels = 'aeiouAEIOU'
    has_vowel = any(c in vowels for c in word)
    groups = 0
    prev_vowel = False
    if has_vowel:
        for c in word:
            if c in vowels:
                if not prev_vowel:
                    groups += 1
                    prev_vowel = True
            else:
                prev_vowel = False
    elif 'y' in word.lower():
        for c in word:
            if c.lower() == 'y':
                if not prev_vowel:
                    groups += 1
                    prev_vowel = True
            else:
                prev_vowel = False
    else:
        groups = 0
    return groups
