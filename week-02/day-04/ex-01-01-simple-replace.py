
# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away

example = "In a dishwasher far far away";
example = example.replace("dishwasher", "galaxy")
print(example)

# or:

example = "In a dishwasher far far away";
example = example[:5] + "galaxy" + example[15:]
print(example)
