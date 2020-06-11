#  Caculate disk usage  Angold4 20200611
import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        """path is dir then list all elements in it"""
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:<7}'.format(total), path)
    return total


if __name__ == "__main__":
    path = '/Users/Angold4/WorkSpace'
    print(disk_usage(path))

    """
    ......
    1945557640 /Users/Angold4/WorkSpace
    1945557640
    """
