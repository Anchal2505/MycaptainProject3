'''Pyhon code to create a function called most_frequent that takjes a string and print the letters in decreasing order of frequency.Use Dictionaries'''
W= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print (most_frequent(W))
