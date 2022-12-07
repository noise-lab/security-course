import re
import linecache
from Crypto.Hash import SHA256
import Crypto.Cipher.AES as AES
from hashlib import md5
import random
from ast import literal_eval
from string import whitespace

### UTILITIES ###

BASE_CODEWORD = 'forensicstudy'

# vm paths
suspect_l_vm_path = 'https://tinyurl.com/forensics-sp16-suspect-1'
suspect_w_vm_path = 'https://tinyurl.com/forensics-sp16-suspect-3'

# location codes
l_stadium   = 'S6HmmW'
l_isr       = 'DlGWvT'
l_eceb      = 'D0aaz1'
l_ncsa      = '21dUSV'
l_research  = '6q8OYH'

w_ikenberry = 'dsHs4I'
w_bookstore = 'zvJvOE'
w_morrow    = 'WumlKB'
w_siebel    = 'J7AkN4'
w_park      = 'b4Hu4g'

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

location_code = {0 : l_stadium,
                 2 : l_isr,
                 4 : l_eceb,
                 6 : l_ncsa,
                 8 : l_research,
                 1 : w_ikenberry,
                 3 : w_bookstore,
                 5 : w_morrow,
                 7 : w_siebel,
                 9 : w_park}

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

