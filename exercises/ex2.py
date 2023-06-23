def array_to_string(arrayOfInts):
    arrayOfStrings = []
    for eachElement in arrayOfInts:
        arrayOfStrings.append(str(eachElement))
    print(arrayOfStrings)
    
array = [1, 2, 3]
result = array_to_string(array)
print(result)