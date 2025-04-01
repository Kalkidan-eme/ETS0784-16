text = [1, "hey", 3.14, [7,9,97]]
print(text) #output: "[1, 'hey', 3.14, [7, 9, 97]]"
print(text[1]) #output: "hey"
text[0] = 42
print(text) #output: "[42, 1, 'hey', 3.14, [7, 9, 97]]"
text = [1,3, 3, 7]
print(text) #output: "[1, 3, 3, 7]"
print(text[-1]) #output: "7"
text.append("nice")
print(text) #output: "[1, 3, 3, 7, 'nice']"