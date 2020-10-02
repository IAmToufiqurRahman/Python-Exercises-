from collections import deque

# list
numbers = list(range(21))
print(numbers)
print(numbers[::-1])

# list unpacking
first, second, third, *others, second_last, last = numbers
print(first, second, third, last, second_last)
print(others)

# looping over list
vowels = ['a', 'e', 'i', 'o', 'u']

for index, letters in enumerate(vowels):
    print(index+1, letters)

# adding or removing items in list: append, insert, pop, remove, del, clear
vowels.insert(0, '*')
vowels.remove('*')
print(vowels)

# finding items in list: index, count
print(vowels.count('a'))

# sorting list: sort, sorted
numbers = [3, 25, 1, 5, 7, 2]
print(sorted(numbers, reverse=True))

# lambda function or anonymous function: lambda parameters: expression
items = [
    ("product1", 10),
    ("product1", 13),
    ("product1", 7)
]
items.sort(key=lambda item: item[1])
print(items)

# map function: mapping something to another thing
# we want to extract the prices of products from the items list into a new list called prices

prices = list(map(lambda item: item[1], items))
print("this is prices:", prices)

# filter fucntion: filters on given condition

filtered_list_of_items = list(filter(lambda item: item[1] >= 10, items))
print(filtered_list_of_items)

# list comprehensions: [expression for x in y], list comprehension can be used in stead of map and filter

price = [item[1] for item in items]
print("this is prices:", price)
filtered_list_of_item = [item for item in items if item[1] >= 10]
print(filtered_list_of_item)

example_list_comprehension = [(letter, number)
                              for letter in 'abcd' for number in range(4)]
print(example_list_comprehension)

# zip function: combines two or more iterables

print(list(zip(numbers, vowels)))

# stacks & queue: linear data structure
# stack stands for LIFO (last in first out), like a pile of books or pushing the back-button in browser
# queue stands for FIFO (first in first out), like a line of people in front of a resturant
# stack & queue will be implemented using deque object in stead of

# stack implementation

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
print(stack)

# queue implementation

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
