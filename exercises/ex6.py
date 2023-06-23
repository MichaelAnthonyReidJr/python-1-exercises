def slice_it(stringArray):
    sentence = ""
    for eachElement in stringArray:
        sentence += stringArray.slice(2)

array = ["this", "is", "another", "test"]
r = slice_it(array)
print(r)
