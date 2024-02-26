def longestPalindrome(s: str) -> str:
    words = []
    length = 0
    while length < len(s):
        for i in range(len(s)):
            if s[length:len(s)-(i-1)] == s[length:-(i-1):-1]:
                words.append(s[length:len(s)-(i-1)])
                break
        length += 1
    longer = ''
    for i in words:
        print(i)
        if len(i) > len(longer) and i == i[::-1]:
            longer = i
    return longer


print(longestPalindrome('abbaad'))
