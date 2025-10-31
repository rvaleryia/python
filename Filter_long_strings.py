def filter_long_strings(strings):
    return [e for e in strings if len(e) > 5]

words = ["cat", "banana", "Moskva", "strawberry", "table", "dog"]
long_words = filter_long_strings(words)
print(long_words)

