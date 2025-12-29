def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    text = text.lower()
    r = {}

    for char in text:
        if char not in r:
            r[char] = 1
        else:
            r[char] += 1
    
    return r

def sort_on(items):
    return items["num"]

def get_report_stats(chars):
    r = []

    for char in chars:
        if not char.isalpha():
            continue

        r.append({
            "char": char,
            "num": chars[char],
        })

    r.sort(reverse=True, key=sort_on)

    return r