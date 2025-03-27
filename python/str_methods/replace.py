text = "hello, welcome to github"
result1 = text.replace("hello", "hey")
print(result1) #output: "hey,welcome to github"
result2 = text.replace("github","GitHub")
print(result2) #output: "hello, welcome to GitHub"

text = "strawberry, strawberry, strawberry"
result3 = text.replace("strawberry", "mint", 2)
print(result3) #output: "mint, mint, strawberry"
