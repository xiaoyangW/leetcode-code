from typing import List


def longestCommonPrefix(strs: List[str]) -> 'str':
    min_len = 0
    min_str = ''
    list_len = len(strs)
    for i in range(list_len):
        str_len = len(strs[i])
        if i == 0:
            min_len = str_len
        if min_len >= str_len:
            min_len = str_len
            min_str = strs[i]
    lenee = 0
    for i in range(min_len):
        for y in range(list_len):
            if min_str[i] != strs[y][i]:
                return min_str[0:lenee]
        lenee += 1
    return min_str[0:lenee]


def longestCommonPrefix2(strs: List[str]) -> 'str':
    min_len = 0
    list_len = len(strs)
    if list_len > 0:
        list1_len = len(strs[0])
        for i in range(list1_len):
            for y in range(list_len):
                print(i)
                if i > len(strs[y])-1 or strs[0][i] != strs[y][i]:
                    return strs[0][0:min_len]
            min_len += 1
        return strs[0][0:min_len]
    return ''
