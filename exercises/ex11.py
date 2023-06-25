def diagonal_printer(sentence):
    
    wordsArray = sentence.split()
    row = 0
    for eachWord in wordsArray:
        i = 0 
        for eachChar in eachWord:
             print(' ' * i + eachChar)
             i += 1
            
                             
