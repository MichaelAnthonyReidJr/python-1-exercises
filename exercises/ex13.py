def frame_it(stringArray):
    largestLength = 0
    for eachWord in stringArray:
        if len(eachWord) > largestLength:
            largestLength = len(eachWord)
        lengthOfStars = largestLength + 4
    print('*' * lengthOfStars)
    
    for eachWord in stringArray:
        print('* ' + eachWord + " " * (lengthOfStars - len(eachWord) - 3) + '*')
    
    print('*' * lengthOfStars)


  

