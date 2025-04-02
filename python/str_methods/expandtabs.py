text = "1\t2\t3"
print(text.expandtabs(4)) #output: "1   2   3"
print(text.expandtabs(5)) #output: "1    2    3"
print(text.expandtabs()) #output: "1       2       3"