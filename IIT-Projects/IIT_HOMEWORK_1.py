# WORKS
def isPalindrome(x: int) -> bool:
        palindrome = str(x) == str(x)[::-1]
        return palindrome

# WORKS
def removeDuplicates(nums: list[int]) -> int:
    res = []
    [res.append(x) for x in nums if x not in res]
    nums = res
    print(nums)

# WORKS
def multiples(n):
    sum = 0
    for i in range(n):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum

# WORKS
def number_of_words(words):
    return len(words.split())

# WORKS
def ascii_art(x:str):
    st = ""
    st_reverse = ""
    n = len(x)
    for i in range(0,n):
        temp1 = x[0:i+1]
        temp2 = x[i:0:-1]
        temp = ".".join(temp2 + temp1)
        temp = temp.center(4*n-3, ".")
        st += temp
        if i != n-1:
            st += "\n"
    for i in range(n-2,-1,-1):
        temp1 = x[0:i+1]
        temp2 = x[i:0:-1]
        temp = ".".join(temp2 + temp1)
        temp = temp.center(4*n-3, ".")
        st_reverse += temp
        if i != 0:
            st_reverse += "\n"
    return st + st_reverse