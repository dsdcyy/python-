
def whole(s, level=0):
    if level == len(s):
        print(''.join(s))
    for i in range(level, len(s)):
        s[level], s[i] = s[i], s[level]
        whole(s, level + 1)
        s[level], s[i] = s[i], s[level]


if __name__ == '__main__':
    s = list('1234')
    whole(s)
