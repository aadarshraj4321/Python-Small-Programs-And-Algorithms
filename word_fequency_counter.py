## Word Frequency

def word_f(words):
    count_word = {}
    wordlist = words.split()
    for word in wordlist:
        if word in count_word:
            count_word[word] += 1
        else:
            count_word[word] = 1
    return count_word

words = input(" : ")
print(word_f(words))
