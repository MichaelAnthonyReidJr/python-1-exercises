def count_words(sentence):
    
    return len(sentence.split(" "))    
    
sentence = input("Enter sentence: ")
num_words = count_words(sentence)
print(num_words)