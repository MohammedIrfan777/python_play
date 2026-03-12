# Python code​​​​​​‌‌‌‌​‌​‌​​‌​‌‌​​​‌‌​​​‌‌‌ below

#convert the string into a list of tuples where each tuple contains a character and its count in the string. For example, the string 'aaabbcaaa' would be converted to [('a', 3), ('b', 2), ('c', 1), ('a', 3)]. Then, write a function that takes this list of tuples and converts it back into the original string.



def encodeString(stringVal):

    if not stringVal:
        return[]

    result = []
    prev = stringVal[0]
    count = 1

    for i in range(1, len(stringVal)):
        if stringVal[i] == prev:
            count +=1
        else:
            result.append((prev, count))
            prev = stringVal[i]
            count = 1

    result.append((prev, count))
    return result


def decodeString(encodedList):
    
    result = ""

    for char, count in encodedList:
        result += char * count

    print(result)


mylist = encodeString('aaabbcaaa')
print(mylist)
decodeString([('a', 3), ('b', 2), ('c', 1), ('a', 3)])


