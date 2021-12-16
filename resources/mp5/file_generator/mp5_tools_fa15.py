import re
import linecache
from Crypto.Hash import SHA256
import Crypto.Cipher.AES as AES
from hashlib import md5
import random
from ast import literal_eval
from string import whitespace

### UTILITIES ###

BASE_CODEWORD = 'klapaucius'

# vm paths
suspect_l_vm_path = 'https://tinyurl.com/forensics-fa15-suspect-l'
suspect_w_vm_path = 'https://tinyurl.com/forensics-fa15-suspect-w'

# location codes
l_bookstore = 'srRnnY'
l_eceb = 'Y79Xwg'
l_powerplant = 'jggFYY'
l_siebel = '8HCqGD'
l_union = 'MPE5dH'

w_armory = 'gsH6jO'
w_hilton = 'nfBeK7'
w_isr = 'uZXNR9'
w_panda = 'LgYiLq'
w_terminal = '1TLwda'

vm_path = {0 : suspect_l_vm_path,
           2 : suspect_l_vm_path,
           4 : suspect_l_vm_path,
           6 : suspect_l_vm_path,
           8 : suspect_l_vm_path,
           1 : suspect_w_vm_path,
           3 : suspect_w_vm_path,
           5 : suspect_w_vm_path,
           7 : suspect_w_vm_path,
           9 : suspect_w_vm_path}

location_code = {0 : l_bookstore,
                 2 : l_eceb,
                 4 : l_powerplant,
                 6 : l_siebel,
                 8 : l_union,
                 1 : w_armory,
                 3 : w_hilton,
                 5 : w_isr,
                 7 : w_panda,
                 9 : w_terminal}

def to_hexstring(number):
    ret = hex(number)[2:]
    ret = ret.replace('L','')
    return ret

def get_student_hash(netid, base=BASE_CODEWORD, extra=''):
    '''
    Returns the hex digest of a student's secret code as a string.
    '''
    codeword = base + netid + extra
    hasher = SHA256.new()
    hasher.update(codeword)
    return hasher.hexdigest()

def uppercase_sanitize(text):
    '''
    Spaces and numbers are left as is.
    English letters are converetd to uppercase.
    All other characters are discarded.
    '''
    stripped_text = re.sub('[^A-Za-z0-9 ]', '', text)
    return stripped_text.upper()

def get_student_random_number(netid, extra='', modulo = 0):
    '''
    generate a random number from 0 to 0xffffffff based on student's hash
    '''
    student_hash = get_student_hash(netid, extra=extra)
    random_number = int(student_hash[:8], 16)
    if modulo != 0:
        return random_number % modulo
    else:
        return random_number

def assign_vm_link(netid):
    '''
    Given a student hash, assign suspect's vm path for checkpoint 2
    Returns vm path as a string.
    '''
    student_rem = get_student_random_number(netid, extra='mp5checkpoint2', modulo = 10)
    return vm_path[student_rem]

def assign_location_code(netid):
    '''
    Given a student hash, assign location code for checkpoint 2
    Returns the key as a string.
    '''
    student_rem = get_student_random_number(netid, extra='mp5checkpoint2', modulo = 10)
    return location_code[student_rem]

################################

# for grading
def read_student_solution(filepath):
    with open (filepath, "r") as myfile:
        data = ""
        for line in myfile:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue;
            data = data+line

        # remove whitespace    
        data = data.translate(None, whitespace)
        # remove space and change strings to uppercase
        data = uppercase_sanitize(data)

    return data

def read_student_wha_solution(filepath):
    with open (filepath, "r") as myfile:
        data = ""
        for line in myfile:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue;
            data = data+line

    return data

### TASK 1.1 SOLUTION ###
def unsubstitute_text(ciphertext, substitution_key):
    for i in range(26):
        ciphertext = ciphertext.replace(substitution_key[i], chr(i+65).lower())

    plaintext = ciphertext.upper()
    return plaintext

### Task 1.2 SOLUTION ###
def aes_decrypt(key, iv, ciphertext):
    '''
    Given a 256-bit key and a 128-bit IV as strings of hex value, 
    decrypts the ciphertext using AES in CBC mode.
    '''
    key_bytes = key.decode('hex')
    iv_bytes = iv.decode('hex')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    return cipher.decrypt(ciphertext)
