import sys
import sympy

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
    c = int(read_file(sys.argv[1]),16)
    e = int(read_file(sys.argv[2]),16)
    n = int(read_file(sys.argv[3]),16)
    o_path = sys.argv[4]

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
            ans = hex(pow(c,d,n))
            write_file(o_path, ans)
            break

if __name__ == '__main__':
    main()