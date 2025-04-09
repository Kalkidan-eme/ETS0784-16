for i in range(7):
    print(f"number={i}") # output:"number=0, number=1, number=2, number=3, number=4, number=5, number=6"
for i in range(2):
    for j in range(3):
        print(f"outer: {i}, inner:{j}") #output: "outer: 0, inner:0 outer: 0, inner:1 outer: 0, inner:2 outer: 1, inner:0 outer: 1, inner:1 outer: 1, inner:2"