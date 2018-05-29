"""
Given an array of distinct integers,
print all the pairs having positive value and negative value of a number that exists in the array.
Print all the required pairs in the increasing order of their absolute numbers.
"""


def pos_neg_pairs(a):
    pair_list = []
    for element in a:
        neg_element = int(-1 * element)
        if a.__contains__(neg_element):
            if not pair_list.__contains__(element):
                pair_list.append(element)
                pair_list.append(neg_element)
    if len(pair_list) == 0:
        return "0"
    else:
        return sorted(pair_list, key=abs)


if __name__ == "__main__":
    array = []
    array_size = int(input("Enter size of array:"))
    for i in range(0, array_size):
        array.append(int(input("Enter Integer element:")))
    print(pos_neg_pairs(array))
