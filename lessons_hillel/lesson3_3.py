lst = [1, 2, 3, 4, 5]

n = len(lst)

if n == 0:
    result = [[], []]
else:
    middle = (n + 1) // 2 
    result = [lst[:middle], lst[middle:]]

print(result)