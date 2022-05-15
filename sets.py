# Create an empty set
s = set()

# Add elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

# no element ever appears more than onece in a set (similar to maths)

s.remove(2)
print(s)

print(f"the set has {len(s)} elements")
# the above will calculate the length of "S" and print out how many elements the set has
