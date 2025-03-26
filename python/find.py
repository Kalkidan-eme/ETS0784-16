text = "hello, welcome to github"
result1 = text.find("welcome")
result2 = text.find("github")
result3 = text.find("python") #not present in the text
result4 = text.find("to")
print(result1) #output: "7"
print(result2) #output: "18"
print(result3) #output: "-1"
print(result4) #output: "15"