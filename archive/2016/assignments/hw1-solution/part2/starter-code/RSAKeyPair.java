import java.math.BigInteger;

public class RSAKeyPair {
    private RSAKey publicKey;
    private RSAKey privateKey;

    public RSAKeyPair(PRGen rand, int numBits) {
        // Create an RSA key pair.  rand is a PRGen that this code can use to get pseudorandom
        //     bits.  numBits is the size in bits of each of the primes that will be used.

        // IMPLEMENT THIS
    }

    public RSAKey getPublicKey() {
        return publicKey;
    }

    public RSAKey getPrivateKey() {
        return privateKey;
    }

    public BigInteger[] getPrimes() {
        // Returns an array containing the two primes that were used in key generation.
        //   In real life we don't always keep the primes around.
        //   But including this helps us grade the assignment.
        BigInteger[] ret = new BigInteger[2];
        ret[0] = BigInteger.ZERO; // IMPLEMENT THIS
        ret[1] = BigInteger.ZERO;
        return ret;
    }
}
