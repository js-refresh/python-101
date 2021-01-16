print("Word counter!")
user_input = input("Pick a word, I'll tell you how many of each word: ")

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    
    return counts

print(word_count(user_input))