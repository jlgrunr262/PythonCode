sentence = ["This", "is", "to", "test", "if", "I", "am", "replicating", "to", "git"]
altsent = ["This is to test if I am replicating to git"]

for index, word in enumerate(sentence):
    print("{}".format(word))
# Exerything above here works (altsent isn't used)
    if index % 2 == 0:
        print(sentence[index])
# 
# newword = (int(sentence[index])