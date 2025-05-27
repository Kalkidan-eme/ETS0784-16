text = "123456"
result1 = text.isdigit()
print(result1) #output: "True"
text = "123r56"
result2 = text.isdigit()
print(result2) #output: "False"
text = "1 2 3 4 5 6"
print(text.isdigit()) #output: "False"