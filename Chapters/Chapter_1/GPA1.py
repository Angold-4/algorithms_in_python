# Angold4_20200505
print('Welcome to the GPA Caculator.')
print('Please Enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')
# map from letter grade to point value
points = {'A+': 4.0, 'A': 3.90, 'A-': 3.67, 'B+': 3.33, 'B': 3.0,
          'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'F': 0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Unknown grade '{}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0:
    print('Your GPA is {0:.3}'.format(total_points / num_courses))

"""

1.'{}'.format()

    In [4]: "{} {}".format("hello", "world")
    Out[4]: 'hello world'

    In [5]: "{}".format("hello", "world")
    Out[5]: 'hello'

    In [6]: print("{:.2f}".format(3.1415926))
    3.14

2. diff between Dynamic language and Static language:

https://www.zhihu.com/question/316509027/answer/627889515
https://stackoverflow.com/questions/20563433/difference-between-static-and-dynamic-programming-languages
main:
Static: The object type must be declared when defining the object
Dynamic: Check and dynamically assign object types when using objects

"""
