"""
    1、哈希表应用实例
    2、python中的ord表示将给定的字符转换为其对应的ASCII码
    3、
"""

MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
        "....","..",".---","-.-",".-..","--","-.",
        "---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."]

# leetcode官解
def uniqueMorseRepresentations(words):
    return len(set("".join(MORSE[ord(ch) - ord('a')] for ch in word) for word in words))


words = ["gin", "zen", "gig", "msg"]
result = uniqueMorseRepresentations(words)
print(result)
