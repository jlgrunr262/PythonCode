# This is a beginner program to generate a story from words input by a user. 
loop = 1
while (loop < 2):
# These are the questions the user answers
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose another noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an descriptive word (adjective): ")
    noun3 = input("Choose a third noun: ")
# Here is the story template into which the words will be inserted  
    print ("----------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2, ",")
    print ("Be kind to your", p_noun, "in", place)
    print ("Where the weather is always", adjective,".")
    print ()
    print ("You may think that this is the", noun3, ",")
    print ("Well it is!")
    print ("----------------------------------")
# loop back to the start of the loop
    loop = loop +1



