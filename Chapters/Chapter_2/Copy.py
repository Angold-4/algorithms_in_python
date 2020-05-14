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
print(B)  # [<__main__.Blue object at 0x10a47dca0>, <__main__.Red object at 0x10a50b8b0>, <__main__.Yellow object at 0x10a50b910>, <__main__.Blue object at 0x10a50b970>]
print(A)  # [<__main__.Blue object at 0x104eb7ca0>, <__main__.Red object at 0x104f458b0>, <__main__.Yellow object at 0x104f45910>]


"""Deep Copy"""
A = []
A.append(Colors.Blue('darkblue', 'DBlue'))
A.append(Colors.Red('orangered', 'ORed'))
A.append(Colors.Yellow('lightyellow', 'LYellow'))
B = copy.deepcopy(A)  # Make a Deepcopy
B.append(Colors.Blue('skyblue', 'SBlue'))
print(B)  # [<__main__.Blue object at 0x10bcf2b50>, <__main__.Red object at 0x10bcbd1c0>, <__main__.Yellow object at 0x10bd340a0>, <__main__.Blue object at 0x10bc64ca0>]
print(A)  # [<__main__.Blue object at 0x108d089d0>, <__main__.Red object at 0x108d08a30>, <__main__.Yellow object at 0x108d08a90>]


"""Difference Between DCopy and SCopy"""

"""

Although When we do some Shallow Copy. We do create a new object.
As We can see that: At that time. We can change B without changing A
(In another words: B is not another alias for list)
But the elements in B are the alias for the same color instance in A

"""
