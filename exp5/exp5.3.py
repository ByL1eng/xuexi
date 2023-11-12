def is_pangram(s):
    s = 'shkjh'
    s = s.lower()
    for char in 'qwertyuiopasdfghjklzxcvbnm':
        if char not in s:
            return False
    else:
        return True