def analyze_words(words):
    result = {}

    for word in words:
        letters = sorted(word)
        result[word] = letters  
    return result

words = ['hello', 'cat']
print(analyze_words(words))