
import java.math.BigInteger;

public class RSAKey {
    private BigInteger exponent;
    private BigInteger modulus;

    public RSAKey(BigInteger theExponent, BigInteger theModulus) {
        exponent = theExponent;
        modulus = theModulus;
    }

    public BigInteger getExponent() {
        return exponent;
    }

    public BigInteger getModulus() {
        return modulus;
    }

    /* Message Padding and OAEP Encoding
     * 
     * The next four methods are public to help us grade the assignment.
     * Implement these methods independent of each other, you should NOT call
     * addPadding/removePadding from within encodeOaep/decodeOaep (or vice-versa).
     * 
     * Encode an input:
     * 
     *     byte[] plaintext = 'Hello World'.getBytes();
     *     byte[] paddedPlaintext = addPadding(plaintext)
     *     byte[] paddedPlaintextOAEP = encodeOaep(paddedPlaintext, prgen);
     * 
     * Recover plaintext:
     * 
     *    byte[] unOAEP = decodeOaep(paddedPlaintextOAEP);
     *    byte[] recoveredPlaintext = removePadding(unOAEP);
     * 
     * In practice, these would be private methods and not part of the public API.
     */

    public byte[] encodeOaep(byte[] input, PRGen prgen) {
        return null; // IMPLEMENT THIS
     }
     
    public byte[] decodeOaep(byte[] input) {
        return null; // IMPLEMENT THIS
    }
     
    public byte[] addPadding(byte[] input) {
        return null; // IMPLEMENT THIS
    }
     
    public byte[] removePadding(byte[] input) {
        return null; // IMPLEMENT THIS
    }
    
    public int maxPlaintextLength() {
        // Return the largest N such that any plaintext of size N bytes
        //      can be encrypted with this key and padding/encoding.

        return 0; // IMPLEMENT THIS
    }
    
    /*
     * RSA Operations
     */
    
    public byte[] encrypt(byte[] plaintext, PRGen prgen) {
        if (plaintext == null)    throw new NullPointerException();
        return null; // IMPLEMENT THIS
    }

    public byte[] decrypt(byte[] ciphertext) {
        if (ciphertext == null)    throw new NullPointerException();
    
        return null; // IMPLEMENT THIS
    }

    public byte[] sign(byte[] message, PRGen prgen) {
        // Create a digital signature on <message>. The signature need
        //     not contain the contents of <message>--we will assume
        //     that a party who wants to verify the signature will already
        //     know which message this is (supposed to be) a signature on.
        if (message == null)    throw new NullPointerException();

        return null; // IMPLEMENT THIS
    }

    public boolean verifySignature(byte[] message, byte[] signature) {
        // Verify a digital signature. Returns true if  <signature> is
        //     a valid signature on <message>; returns false otherwise.
        //     A "valid" signature is one that was created by calling
        //     <sign> with the same message, using the other RSAKey that
        //     belongs to the same RSAKeyPair as this object.
        if ((message == null) || (signature == null))    throw new NullPointerException();

        return false; // IMPLEMENT THIS
    }
}
