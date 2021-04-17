# Various ways to justify text in a print statement
print('Right'.rjust(10))
print('Left'.ljust(10))
print('Center'.center(10))
print('Split'.center(30, '*'))

# Creating a function to print a list in a visually good way

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# Stripping text or removing whitespace from text

spam = '     Stripper time     '
print ('\n')
print(spam)
print(spam.strip())
print(spam,'\n', spam.strip())

print('this is a test')
