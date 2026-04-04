def analyze_words(words):
    return {word: tuple(sorted(set(word))) for word in words}

words = ['hello', 'cat']
print(analyze_words(words))