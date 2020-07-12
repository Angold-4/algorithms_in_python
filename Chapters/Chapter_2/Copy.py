# Angold4 20200515
import Colors
import copy

"""list is Can-Change-Obj"""
A = [1, 2, 3, 4, 5]
B = A
B.append(6)
print(B, A)  # [1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5, 6]

"""Tuple is Can't-Change-Obj"""
A = 1, 2, 3, 4, 5
B = A
B = 1, 2, 3, 4, 5, 6
print(B, A)  # (1, 2, 3, 4, 5, 6) (1, 2, 3, 4, 5)


"""Shallow Copy"""
A = [1, 2, 3, 4, 5]
B = list(A)  # Create a new list -- A and B are different lists
B.append(6)
print(B, A)  # [1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5]
"""Special Case"""
A = []
A.append(Colors.Blue('darkblue', 'DBlue'))
A.append(Colors.Red('orangered', 'ORed'))
A.append(Colors.Yellow('lightyellow', 'LYellow'))
B = list(A)  # Make a Shallow Copy or B = copy.copy(A)
B.append(Colors.Blue('skyblue', 'SBlue'))
print(B)  # [<Colors.Blue object at 0x7fa06c660b50>, <Colors.Red object at 0x7fa06c6608b0>, <Colors.Yellow object at 0x7fa06d1d29d0>, <Colors.Blue object at 0x7fa06d336490>]
print(A)  # [<Colors.Blue object at 0x7fa06c660b50>, <Colors.Red object at 0x7fa06c6608b0>, <Colors.Yellow object at 0x7fa06d1d29d0>]


"""Deep Copy"""
A = []
A.append(Colors.Blue('darkblue', 'DBlue'))
A.append(Colors.Red('orangered', 'ORed'))
A.append(Colors.Yellow('lightyellow', 'LYellow'))
B = copy.deepcopy(A)  # Make a Deepcopy
B.append(Colors.Blue('skyblue', 'SBlue'))
print(B)  # [<Colors.Blue object at 0x7fa06d3571f0>, <Colors.Red object at 0x7fa06d3572b0>, <Colors.Yellow object at 0x7fa06d3573d0>, <Colors.Blue object at 0x7fa06c660b50>]
print(A)  # [<Colors.Blue object at 0x7fa06d336d30>, <Colors.Red object at 0x7fa06d336d90>, <Colors.Yellow object at 0x7fa06d357070>]


"""Difference Between DCopy and SCopy"""

"""

Although When we do some Shallow Copy. We do create a new object.
As We can see that: At that time. We can change B without changing A
(In another words: B is not another alias for list)
But the elements in B are the alias for the same color instance in A

"""
