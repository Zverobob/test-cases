import numpy as np

# Т.К задача не уточнена, ищем парные сивмолы, а не количество их включений в слово.
def find_pairs(word):
    word = word.lower()
    pairs = []
    for i in range(0, len(word) - 1):
        if (word[i] == word[i + 1]) and (word[i] not in pairs):
            pairs.append(word[i])
    return pairs


if __name__ == "__main__":
    word_h = "Hello"
    print("One word example:")
    print("Umushed:", "".join(find_pairs(word_h)))
    print("Mushed: ", "".join(find_pairs(word_h)))

    word = "Hello! Does our continuum space-time expanding accelerates? We have to make some trekking then!"
    print("Many words example:")
    print("Umushed:", find_pairs(word))
    print("Mushed:", "".join(find_pairs(word)))
