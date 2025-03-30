text = "hello, welcome to github"
result1 = text.isalnum()
print(result1) #output: "False"
text = "1 coffee"
result2 = text.isalnum()
print(result2) #output: "False"
text = "1coffee" 
result3 = text.isalnum()
print(result3) #output: "True"