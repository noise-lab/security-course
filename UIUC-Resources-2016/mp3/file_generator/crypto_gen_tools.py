import re
import linecache
import random
import Crypto.Hash.SHA256 as SHA256
import Crypto.Cipher.AES as AES
from hashlib import md5

from ast import literal_eval
from string import whitespace


### UTILITIES ###

BASE_CODEWORD = 'baileybeard'
PYTHON_EXERCISE_EXTRA = 'pythonexercise'
SUBSTITUTION_CIPHER_EXTRA = 'substitution'
DECRYPT_AES_EXTRA = 'decryptaes'
WEAK_AES_EXTRA = 'bfaes'
DECRYPT_RSA_EXTRA = 'rsa1'
AVALANCHE_EFFECT_EXTRA = 'avalanche'
WHA_EXTRA = 'wha'
RSA_WIENER_EXTRA = 'rsa2'

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

# 99991 is the largest prime number under 100000
def get_jeopardy_line(netid, extra='', modulo=99991, filename='jeopardy.txt'):  
    student_hash = get_student_hash(netid, extra=extra)
    line_number = int(student_hash[:8], 16) % modulo
    return linecache.getline(filename, line_number)

def uppercase_sanitize(text):
    '''
    Spaces and numbers are left as is.
    English letters are converetd to uppercase.
    All other characters are discarded.
    '''
    stripped_text = re.sub('[^A-Za-z0-9 ]', '', text)
    return stripped_text.upper()

def pad_text(text, pad_length=16):
    '''
    pad a piece of text until its length is a multiple of pad_length
    '''
    pad_needed = pad_length - len(text) % pad_length
    if pad_needed == pad_length:  # already a multiple of pad_length
        return text
    else:
        return text + ' ' * pad_needed

def generate_hex_string(number, min_length=64):
    hex_string = hex(number)[2:]
    pad_length = min_length - len(hex_string)
    if pad_length > 0:
        return '0' * pad_length + hex_string
    else:
        return hex_string

### TASK 1.1 ###
def generate_student_substitution_key(student_hash, extra='mp1task11'):
    '''
    Given a student hash, generate a substitution key for task 1.1.
    Returns the key as a string.
    '''
    alphabet = [chr(i+65) for i in range(26)]
    hasher = SHA256.new()
    hasher.update(student_hash + extra)
    secret_number = int(hasher.hexdigest()[:8], 16)

    key = ''
    for div in list(reversed(range(1, 27))):  # [26, 25, ..., 1]
        remainder = secret_number % div
        key += alphabet.pop(remainder)

    return key

def substitute_text(plaintext, substitution_key):
    '''
    Substitutes all letters in plaintext according to the key.
    Spaces are not substituted.
    Plaintext is uppercase_sanitize()'d before substitution.
    
    Returns the substituted text.
    '''

    plaintext = uppercase_sanitize(plaintext)
    # TODO: Validate Key. Assume key is valid here.
    for i in range(26):
        # using lower case as a marker to avoid substituting the same letter twice -- hacky. bad.
        plaintext = plaintext.replace(chr(i+65), substitution_key[i].lower())

    ciphertext = plaintext.upper()  # restore uppercase-ness
    return ciphertext

### TASK 1.2 ###
def generate_student_aes_key(student_hash):
    '''
    Given a student hash, generates a 256-bit key and returns its hex value as a string.
    '''
    hasher = SHA256.new()
    hasher.update(student_hash[:8] + 'mp1task12')
    return hasher.hexdigest()

def generate_student_aes_iv(student_hash):
    '''
    Given a student hash, generates a 128-bit IV and returns its hex value as a string.
    '''
    hasher = SHA256.new()
    hasher.update(student_hash[:8] + 'mp1task12iv')
    return hasher.hexdigest()[:32]

def aes_encrypt(key, iv, plaintext):
    '''
    Given a 256-bit key and a 128-bit IV as strings of hex value, 
    encrypts the plaintext using AES in CBC mode.
    Returns the ciphertext as a string of bytes.
    '''
    plaintext = uppercase_sanitize(plaintext)
    plaintext = pad_text(plaintext)
    key_bytes = key.decode('hex')
    iv_bytes = iv.decode('hex')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    return cipher.encrypt(plaintext)

### TASK 1.3 ###
def generate_student_weak_aes_key(student_hash, key_space=32):
    '''
    Given a student hash, generates a 256-bit key, in which first 251 bits are all zero.
    '''
    hasher = SHA256.new()
    hasher.update(student_hash[:8] + 'mp1task13')
    key_number = int(hasher.hexdigest()[:8], 16) % key_space
    return generate_hex_string(key_number)

def generate_student_weak_aes_key_int(student_hash, key_space=32):
    '''
    Given a student hash, generates a 256-bit key, in which first 251 bits are all zero.
    '''
    hasher = SHA256.new()
    hasher.update(student_hash[:8] + 'mp1task13')
    key_number = int(hasher.hexdigest()[:8], 16) % key_space
    return key_number

def weak_aes_encrypt(key, plaintext):
    '''
    same as aes_encrypt but iv is set to 0.
    '''
    return aes_encrypt(key, '0' * 32, plaintext)

### TASK 2.1 ###
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

def random_flip(netid, c):
	rc=chr(0)
	while ord(rc)<32 or ord(rc)==127:
		x=get_student_random_number(netid, extra='mp1task21', modulo = 3)
		x=1<<x
		rc=chr(ord(c)^x)
	return rc

def flip_a_bit(netid, s):
	position = get_student_random_number(netid, extra='mp1task21', modulo = len(s))
	while ord(s[position]) < 65 or ord(s[position]) > 90:
		position = (position + 1) % len(s)
	list_of_char = list(s)
	list_of_char[position] = random_flip(netid, list_of_char[position])
	return ''.join(list_of_char)

def generate_student_aes_key(student_hash):
    '''
    Given a student hash, generates a 256-bit key and returns its hex value as a string.
    '''
    hasher = SHA256.new()
    hasher.update(student_hash[:8] + 'mp1task21')
    return hasher.hexdigest()

def generate_student_aes_iv(student_hash):
    '''
    Given a student hash, generates a 128-bit IV and returns its hex value as a string.
    '''
    hasher = SHA256.new()
    hasher.update(student_hash[:8] + 'mp1task21iv')
    return hasher.hexdigest()[:32]

def aes_encrypt(key, iv, plaintext):
    '''
    Given a 256-bit key and a 128-bit IV as strings of hex value,
    encrypts the plaintext using AES in CBC mode.
    Returns the ciphertext as a string of bytes.
    '''
    plaintext = uppercase_sanitize(plaintext)
    plaintext = pad_text(plaintext)
    key_bytes = key.decode('hex')
    iv_bytes = iv.decode('hex')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    return cipher.encrypt(plaintext)

### TASK 2.2 ###
def weak_hash(s):
	h=0
	m=0x5FFFFFFFF
	for c in s:
		i=ord(c)
		i=(i<<24)^0xCC |(i<<16)^0x33 | ((i<<8)^0xAA) | (i^55)
		h=(h&m)+(i&m)
	return h

def generate_student_weak_aes_key(student_hash, key_space=32):
    '''
    Given a student hash, generates a 256-bit key, in which first 248 bits are all zero.
    '''
    hasher = SHA256.new()
    hasher.update(student_hash[:8] + 'mp1task22')
    key_number = int(hasher.hexdigest()[:8], 16) % key_space
    return generate_hex_string(key_number)

def weak_aes_encrypt(key, plaintext):
    '''
    same as aes_encrypt but iv is set to 0.
    '''
    return aes_encrypt(key, '0' * 32, plaintext)

### TASK 3.2 ###
def generate_student_password(student_hash):
    hasher = SHA256.new()
    hasher.update(student_hash[:8] + 'mp1task32')
    
    random.seed(hasher.hexdigest()) 
    password = ''
    for i in range (0, 8):	# length of the password = 8
        num = random.randint(33, 126)	# any symbol/number/character in ASCII
        password += chr(num)
    
    return password

def generate_token(input):
    token = md5(input)
    return token.hexdigest()

def get_prime(netid, extra='', modulo=49999, filename='prime_list.txt'): # 49999 is the largest prime under 50000
    student_hash = get_student_hash(netid, extra=extra)
    line_number= int(student_hash[:8], 16) % modulo
    return linecache.getline(filename, line_number)

def get_rsa_tuple(netid, extra='', modulo=9973, filename='small_e_rsa.txt'):
    student_hash = get_student_hash(netid, extra=extra)
    line_number = int(student_hash[:8],16) % modulo
    return literal_eval(linecache.getline(filename, line_number)) #(p,q,n,e,d)

def get_bonus_num(netid, extra='', modulo=89989, filename='bonus_numbers.txt'):
    student_hash = get_student_hash(netid, extra=extra)
    line_number = int(student_hash[:8], 16) % modulo
    return linecache.getline(filename, line_number) 


################################
# for grading
def is_empty(filepath):
    if read_student_solution(filepath, nowhitespace=False, uppercase_sanitized=False) == '':
        return True
    return False

def read_student_solution(filepath, nowhitespace=True, uppercase_sanitized=True, strip_L = False):
    with open (filepath, "r") as myfile:
        data = ""
        for line in myfile:
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue
            data = data+line

        if nowhitespace:
            data = data.translate(None, whitespace)

        if uppercase_sanitized:
            data = uppercase_sanitize(data)

        if strip_L:
            data = data.rstrip().rstrip('L')

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
