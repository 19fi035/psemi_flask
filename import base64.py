import base64
​
Encoded_FLAG = 'BUk9IeElQSUpmNUVKSUlvVDFGRlR1WEh6Z2ZBU3hqSng1RlpINTFMemtGTEpXU29RRUNJS3V1SXhJSm55RUluUk1KRUlWMU1ScGtGMklkSXl5S296a2RNSmczcklia0RhTUdJSU1GSElJeEFTT0VDRzA9'
​
def _r_rot13(c):
    if 'A' <= c and c <= 'Z':
        return chr((ord(c) - ord('A') - 13) % 26 + ord('A'))
    if 'a' <= c and c <= 'z':
        return chr((ord(c) - ord('a') - 13) % 26 + ord('a'))
    return c
​
def reverse_rot13(s):
    encoded_str = ""
    for c in s:
        encoded_str += _r_rot13(c)
    return encoded_str
​
def base64_decode(s):
    return base64.b64decode(s)
​
def is_flag(s):
    if s[:6] == 'ctf4b{':
        return True
    else :
        return False
​
def solve(s):
    while not(is_flag(s)):
        if s[0] == 'R':
            s = reverse_rot13(s[1:])
        elif s[0] == 'B':
            s = base64_decode(s[1:]).decode('utf-8')
        else:
            break
    print(s)
if __name__ =='__main__':
     solve(Encoded_FLAG)