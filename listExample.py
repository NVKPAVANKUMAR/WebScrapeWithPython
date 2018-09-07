import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(map(lambda x, y: x + y, list1, list2))
print([x + y for x, y in zip(list1, list2)])
print(np.add(list1, list2))
