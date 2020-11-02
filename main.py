#!/usr/bin/env python3

import sys

A = 26


def encrypt(msg, key):
    temp_string = ""
    for i in range(len(msg)):
        temp_a = (ord(msg[i]) - ord('a'))
        temp_b = (ord(key[i % len(key)]) - ord('a'))
        char = chr(((temp_a + temp_b) % A) + ord('a'))

        temp_string += msg[i] if ord(msg[i]) == ord(' ') or ord(msg[i]) == ord('\n') else char
    return temp_string
    pass


def decrypt(msg, key):
    temp_string = ""
    for i in range(len(msg)):
        temp_a = (ord(msg[i]) - ord('a'))
        temp_b = (ord(key[i % len(key)]) - ord('a'))
        char = chr(((temp_a - temp_b + A) % A) + ord('a'))
        temp_string += msg[i] if ord(msg[i]) == ord(' ') or ord(msg[i]) == ord('\n') else char
    return temp_string
    pass


text_r = ""
key_r = ""

if len(sys.argv) == 2 and (sys.argv[1] == 'e' or sys.argv[1] == 'd'):
    print("'" + sys.argv[1] + "'" + ' mode running!')
else:
    print("Use 'e' for run program in encryption mode")
    print("Use 'd' for run program in decryption mode")
    raise SystemExit(0)

msg_file = input("Input your message file:\n")
try:
    text_r = open(msg_file, "r").read()
except FileNotFoundError or FileExistsError:
    print("File with message don't exist. Try again.")
    raise SystemExit(1)

key_file = input("Input your key file:\n")
try:
    key_r = open(key_file, "r").read()
except FileNotFoundError or FileExistsError:
    print("File with key don't exist. Try again.")
    raise SystemExit(1)

if sys.argv[1] == 'e':

    with open('encryption_' + msg_file, 'w') as f:
        encrypt_txt = encrypt(text_r, key_r)
        f.write(encrypt_txt)
        print('Preview encrypted text:\n' + encrypt_txt)

elif sys.argv[1] == 'd':

    with open('decryption_' + msg_file, 'w') as f:
        decrypt_txt = decrypt(text_r, key_r)
        f.write(decrypt_txt)
        print('Preview decrypted text:\n' + decrypt_txt)
else:
    print("Use 'e' for run program in encryption mode")
    print("Use 'd' for run program in decryption mode")
    raise SystemExit(0)
