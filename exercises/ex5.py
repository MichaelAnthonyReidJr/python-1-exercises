def replace_period(sentence, punctuation):
    newSentence = sentence.replace(".", punctuation )
    return newSentence
    
sentence = "Test.  This is a test.  Testing."
sentence2 = replace_period(sentence, "!")
print(sentence2)  
        