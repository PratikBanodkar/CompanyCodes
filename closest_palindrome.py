"""Given a number N. our task is to find the closest Palindrome number whose absolute difference with given number is
minimum. """


def closest_palindrome(num):
    low_palindrome = 0
    high_palindrome = pow(10,14)
    for i in range(num, 0, -1):
        if is_palindrome(i):
            low_palindrome = i
            break
    ld = abs(low_palindrome - num)
    for i in range(num, num+ld):
        if is_palindrome(i):
            high_palindrome = i
            break
    hd = abs(high_palindrome - num)
    if ld > hd:
        return high_palindrome
    else:
        return low_palindrome


def is_palindrome(number):
    return str(number) == str(number)[::-1]


if __name__ == "__main__":
    n = int(input("Enter value of N:"))
    print("Closest palindrome is:", closest_palindrome(n))

