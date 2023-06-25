def vowel_counter(string):
    vowel_count = 0
    for eachChar in string:
        if eachChar in 'aeiouAEIOU':
            vowel_count += 1
    return f"Number of vowels: {vowel_count}" 

