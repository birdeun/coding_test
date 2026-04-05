# sol.1
def solution(s):
    for i in s:
        if i not in '0123456789':
            return False
        else:
            return True
        
# sol.2
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()