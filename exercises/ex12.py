def word_histogram(stringOfWords):
    words = stringOfWords.split()
    numbersDictionary = {}
    for eachWord in words:
        wordCount = 0
        for everyOtherWord in words: 
            if eachWord == everyOtherWord:
                wordCount += 1
        numbersDictionary.update({eachWord: wordCount})
    print(numbersDictionary)    


