def add_numbers(arrayOfNumericTypes):
    floatSum = 0.00
    for eachElement in arrayOfNumericTypes:
        floatSum += float(eachElement)
    return floatSum;
        
array = [1.0, 1.1, "1"]
result = add_numbers(array)
print(result)   