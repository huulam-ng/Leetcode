#https://leetcode.com/problems/length-of-last-word/
def length_of_last_word(s): 
    a = s.split()
    return len(a[-1])
    if len(a) < 1:
        return 0

print(length_of_last_word("hello world"))
