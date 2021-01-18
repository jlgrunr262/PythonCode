# create a list
animals = ["lion", "tiger", "bear", "penguin"]
# create variable to hold number of characters
chars = 0
# for loop to look at each element in the list and count characters
for animal in animals:
    chars += len(animal)
# in the calculation use 'len' again but this time to count the length of the list
print("Total characters in the list: {}, Average length: {}".format(chars, chars/len(animals)))


# this is the enumerate function, which is a way of indexing

winners = ["Aleksei", "Anya", "Clarissa", "Belle"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# Use enumeration to provide a list of emails and names
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("jlg@jlgrunr.com", "Jerry Gentry"), ("cnumb@gmail.com", "David Gilmour")]))
# this is just to test GIT

