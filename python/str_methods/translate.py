text = "banana"
table = str.maketrans({'a':'x', 'b':'y'})
print(text.translate(table)) #output: "yxnxnx"