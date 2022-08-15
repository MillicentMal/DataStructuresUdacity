def lowercase_sort(string):
    lowercase = {}
    sorted_string = []
    for i in range(len(string)):
        if string[i].islower():
            lowercase[i] = string[i]
        else:
            sorted_string.insert(i, string[i])
    indexes = sorted(lowercase)
    new = sorted(lowercase.items(),  key=lambda x: x[1])
 
    for i in range(len(indexes)):
        sorted_string.insert(indexes[i], new[i][1])
    return "".join(sorted_string)


string = "My NaMe is Millicent"

print(string)
print(lowercase_sort(string))
