fruits = ["cherry", "banana", "apple", "litchi", "mango", "guava", "dragonfruit"]
sorted_fruits = sorted(fruits, key=lambda x: (len(x), x ))
print(sorted_fruits)


