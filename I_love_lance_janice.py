def solution(secret):
    cipher_dict = {
                    "a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s",
                    "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k",
                    "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c",
                    "y": "b", "z": "a"
                   }
    decrypted = list()
    for char in secret:
        if char in cipher_dict:
            decrypted.append(cipher_dict[char])
        else:
            decrypted.append(char)
    decrypted = ''.join(decrypted)
    print(decrypted)
