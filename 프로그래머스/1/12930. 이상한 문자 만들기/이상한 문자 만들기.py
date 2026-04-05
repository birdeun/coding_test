# sol.1
def solution(s):
    word = list(s)
    idx = 0
    
    for i in range(len(word)):
        if word[i] == ' ':
            idx = 0
        else:
            if idx % 2 == 0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
            idx += 1
    return ''.join(word)
            
# sol.2 using ASCII
def solution(s):
    word = list(s)
    idx = 0

    for i in range(len(word)):
        if word[i] == ' ':
            idx = 0
        else:
            if idx % 2 == 0:
                if 'a' <= word[i] <= 'z':
                    word[i] = chr(ord(word[i]) - 32)
            else:
                if 'A' <= word[i] <= 'Z':
                    word[i] = chr(ord(word[i]) + 32)
            idx += 1

    return ''.join(word)