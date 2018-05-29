"""
Given an array of n integers(duplicates allowed). Print “Yes” if it is a set of contiguous integers else print “No”.
"""


def is_contiguous(a):
    b = []
    for elem in a:
        if not b.__contains__(elem):
            b.append(elem)
    a_sum = 0
    for j in range(min(a), max(a)+1):
        a_sum += j
    b_sum = sum(b)
    if a_sum == b_sum:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    array = []
    size = int(input("Enter size of array:"))
    for i in range(0, size):
        val = int(input("Enter element:"))
        array.append(val)
    print(is_contiguous(array))
