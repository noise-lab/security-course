
import java.math.BigInteger;


public class RSAKeyPair {
    private RSAKey publicKey;
    private RSAKey privateKey;
    private BigInteger p, q;

    public RSAKeyPair(PRGen rand, int numBits) {
	p = new BigInteger(numBits, 128, rand);
	q = new BigInteger(numBits, 128, rand);
	BigInteger n = p.multiply(q);

	BigInteger pm1 = p.subtract(BigInteger.ONE);
	BigInteger qm1 = q.subtract(BigInteger.ONE);
	BigInteger phi = pm1.multiply(qm1);

	BigInteger e;
	do {
	    e = new BigInteger(numBits-2, rand);
	} while( ! e.gcd(phi).equals(BigInteger.ONE));
	BigInteger d = e.modInverse(phi);

	publicKey = new RSAKey(e, n);
	privateKey = new RSAKey(d, n);
    }

    public RSAKey getPublicKey() {
	return publicKey;
    }

    public RSAKey getPrivateKey() {
	return privateKey;
    }

    public BigInteger[] getPrimes() {
	// Returns the two primes that were used in key generation.
	//   In real life we don't always keep the primes around.
	//   But including this helps us grade the assignment.
	BigInteger[] ret = new BigInteger[2];
	ret[0] = p;
	ret[1] = q;
	return ret;
    }
}