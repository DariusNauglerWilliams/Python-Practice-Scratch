


def is_anagram(firstword, secondword):
    if len(firstword) != len(secondword):
        return False

    return sorted(firstword) == sorted(secondword)







print(is_anagram("eat", "tea"))
print(is_anagram("cat", "dog"))
print(is_anagram("listen", "silent"))
print(is_anagram("Snow", "owns"))
print(is_anagram("a", "aa"))
print(is_anagram("rail safety", "fairy tales"))
print(is_anagram("hello!", "olleh"))