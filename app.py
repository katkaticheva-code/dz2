def analyze_words(words):
    result = {}
    
    for word in words:
        letters = sorted(word)      # разбиваем и сортируем
        result[word] = tuple(letters) 
    
    return result


# пример
words = ['hello', 'cat']
print(analyze_words(words))