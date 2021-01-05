def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    s_sort_list = sorted(s)
    t_sort_list = sorted(t)
    if s_sort_list == t_sort_list:
        return True
    else:
        return False

s = "anagram"
t = "nagaram"


print(isAnagram(s, t))