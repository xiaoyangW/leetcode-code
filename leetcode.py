import ListNode


def twoSum(nums: 'List[int]', target: 'int') -> 'List[int]':
    length = len(nums)
    if length > 1:
        for i in range(length - 1):
            for x in range(length - (i + 1)):
                diff = target - nums[i]
                if nums[x + i + 1] == diff:
                    return [i, x + i + 1]
    return None


def reverse(x: 'int') -> 'int':
    if x == 0:
        return x
    str_x = str(x)
    minus = ''
    if str_x[0] == '-':
        minus = '-'
        str_x = str_x[1:]
    str_x = str_x[-1::-1]
    i = int(minus + str_x)
    if -2 ** 32 < i < 2 ** 32 - 1:
        return i
    else:
        return 0


def isPalindrome(x: 'int') -> 'bool':
    str_x = str(x)
    length = len(str_x)
    if length == 1:
        return True
    elif x % 10 == 0 or x < 0:
        return False
    half = length / 2
    left = str_x[:int(half)]
    right = ''
    if (length % 2) == 0:
        right = str_x[int(half):]
    else:
        right = str_x[int(half) + 1:]
    right = right[-1::-1]
    if left == right:
        return True
    else:
        return False


def isPalindrome2(x: 'int') -> 'bool':
    if x < 0:
        return False
    elif x < 10:
        return True
    str_x = str(x)
    f = str_x[-1::-1]
    if f == str_x:
        return True
    else:
        return False


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    print(len(l1))
    return None


def romanToInt(s: 'str') -> int:
    x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #for i in range(len(s)):
    #    x = x.get(i)
    print(s[0])
    return None
