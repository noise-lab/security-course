import os, sys
import crypto_gen_tools
from pathlib import Path

DIR_NAME = '/mp3/'
THIS_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
PYMD5_PATH = str(Path(THIS_SCRIPT_DIR)/'pymd5.py')

def svn_add(path):
    os.system('svn add ' + path)

def generate_files(netid):
    # return if netid is empty
    if not netid:
        return         

    basepath = netid + DIR_NAME
    if not os.path.isdir(basepath):
        os.mkdir(basepath)
    svn_add(basepath)

    student_hash = crypto_gen_tools.get_student_hash(netid)

    ### Python Tutorial ###
    python_exercise_value = crypto_gen_tools.get_student_random_number(netid, extra=crypto_gen_tools.PYTHON_EXERCISE_EXTRA)
    python_exercise_path = basepath + '3.1.1.2_value.hex'
    with open(python_exercise_path, 'w') as f:
        sub_key = crypto_gen_tools.generate_student_substitution_key(student_hash)
        f.write(hex(python_exercise_value)[2:])
    svn_add(python_exercise_path)

    ### Substitution Cipher ###
    sub_key_path = basepath + '3.1.2.1_sub_key.txt'
    with open(sub_key_path, 'w') as f:
        sub_key = crypto_gen_tools.generate_student_substitution_key(student_hash)
        f.write(sub_key)
    svn_add(sub_key_path)

    sub_ciphertext_path = basepath + '3.1.2.1_sub_ciphertext.txt'
    with open(sub_ciphertext_path, 'w') as f:
        plaintext = crypto_gen_tools.get_jeopardy_line(netid, extra=crypto_gen_tools.SUBSTITUTION_CIPHER_EXTRA)
        ciphertext = crypto_gen_tools.substitute_text(plaintext, sub_key)
        f.write(ciphertext)
    svn_add(sub_ciphertext_path)

    ### Decrypt AES ###

    aes_key_path = basepath + '3.1.2.2_aes_key.hex'
    with open(aes_key_path, 'w') as f:
        aes_key = crypto_gen_tools.generate_student_aes_key(student_hash)
        f.write(aes_key)
    svn_add(aes_key_path)

    aes_iv_path = basepath + '3.1.2.2_aes_iv.hex'
    with open(aes_iv_path, 'w') as f:
        aes_iv = crypto_gen_tools.generate_student_aes_iv(student_hash)
        f.write(aes_iv)
    svn_add(aes_iv_path)

    aes_ciphertext_path = basepath + '3.1.2.2_aes_ciphertext.hex'
    with open(aes_ciphertext_path, 'w') as f:
        plaintext = crypto_gen_tools.get_jeopardy_line(netid, extra=crypto_gen_tools.DECRYPT_AES_EXTRA)
        ciphertext = crypto_gen_tools.aes_encrypt(aes_key, aes_iv, plaintext)
        f.write(ciphertext.encode('hex'))
    svn_add(aes_ciphertext_path)

    ### Brute Force AES ###
    aes_weak_ciphertext_path = basepath + '3.1.2.3_aes_weak_ciphertext.hex'
    with open(aes_weak_ciphertext_path, 'w') as f:
        weak_aes_key = crypto_gen_tools.generate_student_weak_aes_key(student_hash)
        plaintext = crypto_gen_tools.get_jeopardy_line(netid, extra=crypto_gen_tools.WEAK_AES_EXTRA)
        ciphertext = crypto_gen_tools.weak_aes_encrypt(weak_aes_key, plaintext)
        f.write(ciphertext.encode('hex'))
    svn_add(aes_weak_ciphertext_path)


    ### Decrypt RSA ###
    (p,q,n,e,d) = crypto_gen_tools.get_rsa_tuple(netid, extra=crypto_gen_tools.DECRYPT_RSA_EXTRA)
    prime = int(crypto_gen_tools.get_prime(netid, extra=crypto_gen_tools.DECRYPT_RSA_EXTRA))

    #encrypt
    cipher_path = basepath + '3.1.2.4_RSA_ciphertext.hex'
    with open(cipher_path, 'w') as f:
        ciphertext = pow(prime,d,n)
        f.write(crypto_gen_tools.to_hexstring(ciphertext))
    svn_add(cipher_path)

    key_path = basepath + '3.1.2.4_RSA_private_key.hex'
    with open(key_path, 'w') as f:
        f.write(crypto_gen_tools.to_hexstring(e))
    svn_add(key_path)

    modulo_path = basepath + '3.1.2.4_RSA_modulo.hex'
    with open(modulo_path, 'w') as f:
        f.write(crypto_gen_tools.to_hexstring(n))
    svn_add(modulo_path)

    ### Avalanche Effect ###
    original_string_path = basepath + '3.1.3.1_input_string.txt'
    with open(original_string_path, 'w') as f:
        plaintext = crypto_gen_tools.get_jeopardy_line(netid, extra=crypto_gen_tools.AVALANCHE_EFFECT_EXTRA)
        f.write(crypto_gen_tools.uppercase_sanitize(plaintext))
    svn_add(original_string_path)

    perturbed_string_path = basepath + '3.1.3.1_perturbed_string.txt'
    with open(perturbed_string_path, 'w') as f:
        perturbed_string = crypto_gen_tools.flip_a_bit(netid, plaintext)
        f.write(crypto_gen_tools.uppercase_sanitize(perturbed_string))
    svn_add(perturbed_string_path)

    ### WHA ###
    input_string_path = basepath + '3.1.3.2_input_string.txt'
    with open(input_string_path, 'w') as f:
        input_string = crypto_gen_tools.get_jeopardy_line(netid, extra=crypto_gen_tools.WHA_EXTRA)
        f.write(crypto_gen_tools.uppercase_sanitize(input_string))
    svn_add(input_string_path)

    ### MD5 Length Extension ###
    query_path = basepath + '3.2.1.2_query.txt'
    with open(query_path, 'w') as f:
        password = crypto_gen_tools.generate_student_password(student_hash)
    	command_line = 'user=admin&command1=ListFiles&command2=NoOp'
    	token = crypto_gen_tools.generate_token(password + command_line)
    	query = 'token=' + token + '&' + command_line
        f.write(str(query))
    svn_add(query_path)
	
    command_path = basepath + '3.2.1.2_command3.txt'
    with open(command_path, 'w') as f:
        command = '&command3=DeleteAllFiles'
        f.write(str(command))
    svn_add(command_path)

    ### RSA Wiener ###
    (p,q,n,e,d) = crypto_gen_tools.get_rsa_tuple(netid, extra=crypto_gen_tools.RSA_WIENER_EXTRA, modulo=9973, filename='bonus_rsa.txt')
    plaintext = int(crypto_gen_tools.get_bonus_num(netid, extra=crypto_gen_tools.RSA_WIENER_EXTRA))

    # pycrypto only allow custom e, so this part will seems counter intuitive: 
    # they'll have to guess e
    cipher_path = basepath + '3.2.2_ciphertext.hex'
    with open(cipher_path, 'w') as f:
        ciphertext = pow(plaintext,d,n)
        f.write(crypto_gen_tools.to_hexstring(ciphertext))
    svn_add(cipher_path)

    key_path = basepath + '3.2.2_public_key.hex'
    with open(key_path, 'w') as f:
        f.write(crypto_gen_tools.to_hexstring(d))
    svn_add(key_path)

    modulo_path = basepath + '3.2.2_modulo.hex'
    with open(modulo_path, 'w') as f:
        f.write(crypto_gen_tools.to_hexstring(n))
    svn_add(modulo_path)

    ### Distribute pymd5 ###
    os.system('cp {} {}'.format(PYMD5_PATH, basepath+'pymd5.py'))
    svn_add(basepath+'pymd5.py')
    
    ### Generate Blank Files for submission ###
    # (filename, initial content)
    empty_files = [('partners.txt', ''),
                   ('sol_3.1.1.2_decimal.txt', ''),
                   ('sol_3.1.1.2_binary.txt', ''),
                   ('sol_3.1.2.1.py', ''),
                   ('sol_3.1.2.1.txt', ''),
                   ('sol_3.1.2.2.py', ''),
                   ('sol_3.1.2.2.txt', ''),
                   ('sol_3.1.2.3.hex', ''),
                   ('sol_3.1.2.4.py', ''),
                   ('sol_3.1.2.4.hex', ''),
                   ('sol_3.1.3.1.py', ''),
                   ('sol_3.1.3.1.hex', ''),
                   ('sol_3.1.3.2.py', ''),
                   ('sol_3.1.3.2.txt', ''),
                   ('sol_3.2.1.2.py', ''),
                   ('sol_3.2.1.2.txt', ''),
                   ('sol_3.2.2.py', ''),
                   ('sol_3.2.2.hex', ''),
                   ('sol_3.2.3_good.py', ''),
                   ('sol_3.2.3_evil.py', ''),
                   ('sol_3.2.4_hash.hex', ''),
                   ('sol_3.2.4.ps', '')]

    for filename, content in empty_files:
        filepath = basepath + filename
        with open(filepath, 'w') as f:
            f.write(content)
        svn_add(filepath)


def main():
    if (len(sys.argv) < 3):
        print 'usage svn_root roster_file (both in absolute path)'
        exit(0)

    local_svn_repo = sys.argv[1]
    roster = sys.argv[2]
    os.chdir(local_svn_repo)

    with open(roster) as f:
        for netid in f:
            netid = netid.strip()
            generate_files(netid)

if __name__ == '__main__':
    main()
