def filter_clean(words, banned):
    filtered = []
    banned__set = set(banned)
    for word in words:
        if word not in banned__set:
            filtered.append(word)
    return filtered


def first_duplicate(items):
    unique_items = set()
    for item in items:
        old_len = len(unique_items)
        unique_items.add(item)
        if len(unique_items) == old_len:
            return item
    return None

print(filter_clean(["a", "spam", "b"], ("spam")) == ["a", "b"])
