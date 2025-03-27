text = "           hello, welcome to github            "
result1 = text.strip()
print(result1) #output: "hello, welcome to  github"

text = "***cards***"
result2 = text.strip("***")
print(result2) #output: "cards"

text = "abcfoodabc"
result3 = text.strip("abc")
print(result3) #output: "food"
