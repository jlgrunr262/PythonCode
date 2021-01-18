# List comprehension is an easier way to itereate over a list
# Typical is like this
multiples = []
for x in range(1,11):
    multiples.append(x*7)

print(multiples)

# Using list comprehension the same function looks like this
multiples = [x*7 for x in range(1,11)]
print(multiples)

# THIS IS COOL!
# You can use list comprehension to do range evaluations. I
# If I want to list every number divisible by 3 from 0- 100...
thirds = [x for x in range(0,101) if x % 3 == 0]
print(thirds)
