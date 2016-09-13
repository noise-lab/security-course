### 3/15/2016
### A totally hacked together script just to check if the RSA keys we gave to
### students can be cracked with weiner attack by performing the attack on them.
### The script use the solution from sol_1.2.2.py, which is not optimized, so
### it will take a while to run for each student. This is done to simulate an
### actual student solution.

### This really should not be necessary, but I'm paranoid. - Due


import sys
import sympy
sys.path.insert(0, '/Users/serifx/sp16-ece422/_class/_private/mp3/file_generator') # change this
import crypto_gen_tools
def make_continued_fraction(a, b):
    cf = []
    while a != 1:
        x = a/b
        y = a%b
        cf.append(x)
        a = b
        b = y
    return cf

def compute_convergent(lst, i):
    a = 1
    b = lst[i]
    while i > 0:
        i -= 1
        tmp = lst[i]*b+a
        a = b
        b = tmp
    return (b,a)

def make_convergent(lst):
    ret = []
    for i in range(len(lst)):
        ret.append(compute_convergent(lst,i))
    return ret

# ref: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m 
######################################################################### endref
def read_file(filename):
    with open(filename) as f:
        ret = f.read()
    return ret

def write_file(filename, content):
    with open(filename,'w') as f:
        f.write(content)

def main():

    c_path = '/Users/serifx/sp16-ece422/{}/mp3/3.2.2_ciphertext.hex' # change this
    e_path = '/Users/serifx/sp16-ece422/{}/mp3/3.2.2_public_key.hex' # change this
    n_path = '/Users/serifx/sp16-ece422/{}/mp3/3.2.2_modulo.hex' # change this

    with open('/Users/serifx/sp16-ece422/_rosters/students.txt') as f:  # change this
        students = f.readlines()

    for netid in students:
        netid = netid.strip()
        print 'processing '+netid
        c = int(read_file(c_path.format(netid)),16)
        e = int(read_file(e_path.format(netid)),16)
        n = int(read_file(n_path.format(netid)),16)
        expected_ans = int(crypto_gen_tools.get_bonus_num(netid, extra=crypto_gen_tools.RSA_WIENER_EXTRA))

        lst = make_continued_fraction(e, n)
        conv_lst = make_convergent(lst)

        x = sympy.Symbol('x')
        for k, d in conv_lst:
            if k == 0:
                continue
            tot = (e*d-1)/k
            roots = sympy.solvers.solve(x**2 - (n-tot+1)*x + n, x)
            if len(roots) == 2:
                p = int(roots[0]) % n
                q = int(roots[1]) % n
                tot = (p-1)*(q-1)
                d = modinv(e, tot)
                ans = pow(c,d,n)
                break
            print 'T T'
        if ans != expected_ans:
            print 'Problem with {}'.format(netid)
            break
        print ans
        print expected_ans

if __name__ == '__main__':
    main()