fruits = {"apple", "orange", "banana", "kiwi"}
print(fruits) #output: "{'banana', 'apple', 'orange', 'kiwi'}"
numbers = {"1", "2", "3", "7"}
print(numbers) #output: "{'1', '3', '2', '7'}"
fruits.add("strawberry")
print(fruits) #output: "{'banana', 'orange', 'strawberry', 'apple', 'kiwi'}"
fruits.remove("banana")
print(fruits)#output: "{'orange', 'strawberry', 'apple', 'kiwi'}"

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)  # output: "{1, 2, 3, 4, 5}" union
print(set_a & set_b)  # output: "{3}" intersection
print(set_a - set_b)  # output: "{1, 2}" difference
print(set_a ^ set_b)  # output: "{1, 2, 4, 5}" symmetric difference