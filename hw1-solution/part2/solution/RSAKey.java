import java.math.BigInteger;
import java.util.Arrays;

public class RSAKey {
    private static final int K0_BIT_SIZE = 128;
    private static final int K1_BIT_SIZE = 128;
    private static final int K0_BYTE_SIZE = K0_BIT_SIZE/8;
    private static final int K1_BYTE_SIZE = K1_BIT_SIZE/8;
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

    public byte[] encrypt(byte[] plaintext, PRGen prgen) {
        if (plaintext == null)    throw new NullPointerException();
        assert plaintext.length <= maxPlaintextLength();
        
        //Pad the input message
        byte[] paddedPlaintext = addPadding(plaintext);
        
        //Pad with OAEP
        byte[] mOAEP = encodeOaep(paddedPlaintext, prgen);
        
        //Convert OAEP padded m into BigInteger
        BigInteger mBigInt = HW2Util.bytesToBigInteger(mOAEP);
        
        //Encrypt with key
        BigInteger mEncryptedBigInt = mBigInt.modPow(exponent, modulus);
        
        return mEncryptedBigInt.toByteArray();
    }

    public byte[] decrypt(byte[] ciphertext) {
        if (ciphertext == null)    throw new NullPointerException();
        
        //Decrypt with key
        BigInteger mEncryptedBigInt = new BigInteger(1, ciphertext);
        BigInteger mDecrypted = mEncryptedBigInt.modPow(exponent, modulus);
        
        // Recall what len the plaintext is
        int plaintextLen = maxPlaintextLength() + K0_BYTE_SIZE + K1_BYTE_SIZE + 1;
        
        //Convert back to byte array
        byte[] mOAEP = HW2Util.bigIntegerToBytes(mDecrypted, plaintextLen);
        
        //Remove OAEP Padding
        byte[] paddedPlaintext = decodeOaep(mOAEP);
        if (paddedPlaintext == null) {
        	return null;
        }
        
        //Remove message padding
        byte[] plaintext = removePadding(paddedPlaintext);

        return plaintext;
    }

    public byte[] sign(byte[] message, PRGen prgen) {
        // Create a digital signature on <message>. The signature need
        //     not contain the contents of <message>--we will assume
        //     that a party who wants to verify the signature will already
        //     know which message this is (supposed to be) a signature on.
        if (message == null)    throw new NullPointerException();
        
        //Hash function to reduce message
        byte[] seed = new byte[32]; //A hard coded seed is fine
        for (int i = 0; i < 32; i++) {
        	seed[i] = (byte) i;
        }
        PRF prf = new PRF(seed);
        
        //Hash message and encrypt hash
        byte[] hashedMessage = prf.eval(message);
        return encrypt(hashedMessage, prgen);
    }

    public boolean verifySignature(byte[] message, byte[] signature) {
        // Verify a digital signature. Returns true if  <signature> is
        //     a valid signature on <message>; returns false otherwise.
        //     A "valid" signature is one that was created by calling
        //     <sign> with the same message, using the other RSAKey that
        //     belongs to the same RSAKeyPair as this object.
        if ((message == null) || (signature == null))    throw new NullPointerException();

        //Hash function to reduce message
        byte[] seed = new byte[32]; //A hard coded seed is fine
        for (int i = 0; i < 32; i++) {
        	seed[i] = (byte) i;
        }
        PRF prf = new PRF(seed);
        byte[] hashedMessage = prf.eval(message);

        //Decrypt signature
        byte[] sigHash = decrypt(signature);
        
        //If hashes match, the message was not altered
        return Arrays.equals(hashedMessage, sigHash);
    }

    public int maxPlaintextLength() {
        // Return the largest N such that any plaintext of size N bytes
        //      can be encrypted with this key
        
    	//m = n - k0 - k1 - minimum padding - 1 bit
        //where n is the bitlength of the RSA modulus
        //minimum padding is 1 byte (since we assume messages are full bytes)
        //the extra 1 bit removes cases where X||Y can be larger than mod N
        int m = modulus.bitLength() - K0_BIT_SIZE - K1_BIT_SIZE - 8 - 1;
        return m / 8; //number of bytes
    }
       
    // The next four methods are public to help us grade the assignment. In real life, these would
    // be private methods as there's no need to expose these methods as part of the public API
    
    public byte[] encodeOaep(byte[] input, PRGen prgen) {
        
        //extend input with zeros for K1
        byte[] extendedInput = new byte[input.length + K1_BYTE_SIZE];
        System.arraycopy(input, 0, extendedInput, 0, input.length);
        
        //r = k0 random bits
        byte[] r = new byte[K0_BYTE_SIZE];
        for (int i = 0; i < K0_BYTE_SIZE; i++) {
        	r[i] = (byte) prgen.next(8);
        }
        
        //G - a PRGen to expand r
        //pad with zeros up to required prg key length
        byte[] rPadded = new byte[32];
        System.arraycopy(r, 0, rPadded, 0, r.length); //remaining defaults to 0
        PRGen G = new PRGen(rPadded);
        byte[] rExtended = new byte[extendedInput.length];
        for (int i = 0; i < rExtended.length; i++) {
        	rExtended[i] = (byte) G.next(8);
        }
        
        //X = m00..0 XOR G(r)
        byte[] X = new byte[extendedInput.length];
        for (int i = 0; i < extendedInput.length; i++) {
        	X[i] = (byte) (extendedInput[i] ^ rExtended[i]);
        }
        
        //H is used to reduce X
        byte[] seed = new byte[32]; //A hard coded seed is fine
        for (int i = 0; i < 32; i++) {
        	seed[i] = (byte) i;
        }
        PRF prf = new PRF(seed);
        byte[] hashedX = prf.eval(X);
        
        // Y = r XOR H(X)
        // we only use 128 bits of H(X) in this configuration
        byte[] Y = new byte[r.length];
        for (int i = 0; i < r.length; i++) {
        	Y[i] = (byte) (r[i] ^ hashedX[i]);
        }
        
        //Combine X || Y
        byte[] mOAEP = new byte[X.length + Y.length];
        System.arraycopy(X, 0, mOAEP, 0, X.length);
        System.arraycopy(Y, 0, mOAEP, X.length, Y.length);
        
        return mOAEP;
    }
    
    public byte[] decodeOaep(byte[] input) {
        //unOAEP
        byte[] X = new byte[maxPlaintextLength()+K1_BYTE_SIZE+1];
        System.arraycopy(input, 0, X, 0, X.length);
        byte[] Y = new byte[K0_BYTE_SIZE];
        System.arraycopy(input, X.length, Y, 0, Y.length);
        
        //H(X)
        byte[] seed = new byte[32]; //A hard coded seed is fine
        for (int i = 0; i < 32; i++) {
        	seed[i] = (byte) i;
        }
        PRF prf = new PRF(seed);
        byte[] hashedX = prf.eval(X);
        
        //r = H(X) XOR Y
        byte[] r = new byte[Y.length];
        for (int i = 0; i < Y.length; i++) {
        	r[i] = (byte) (hashedX[i] ^ Y[i]);
        }
        
        //G - a PRGen to expand r
        //pad with zeros up to required prg key length
        byte[] rPadded = new byte[32];
        System.arraycopy(r, 0, rPadded, 0, r.length); //remaining defaults to 0
        PRGen G = new PRGen(rPadded);
        byte[] rExtended = new byte[X.length];
        for (int i = 0; i < rExtended.length; i++) {
        	rExtended[i] = (byte) G.next(8);
        }
        
        //recover padded message
        //m00.0 = G(r) XOR X
        byte[] oaepPlaintext = new byte[X.length];
        for (int i = 0; i < X.length; i++) {
        	oaepPlaintext[i] = (byte) (rExtended[i] ^ X[i]);
        }

        //check that K1 is still zeros -- return null if not
        for (int i = oaepPlaintext.length - K1_BYTE_SIZE; i < oaepPlaintext.length; i++) {
            if (oaepPlaintext[i] != (byte) 0) {
                return null;
            }
        }        

        //remove K1 padding
        byte[] paddedPlaintext = new byte[oaepPlaintext.length - K1_BYTE_SIZE];
        System.arraycopy(oaepPlaintext, 0, paddedPlaintext, 0, paddedPlaintext.length);        
        
        return paddedPlaintext;
    }
    
    public byte[] addPadding(byte[] input) {
        //length = message length + minimum message padding
        byte[] paddedPlaintext = new byte[maxPlaintextLength() + 1];
        
        //Pad if not full length using the 10* method
        //There must always be at least one byte of padding so we 
        //know where the message ends under all input conditions
        System.arraycopy(input, 0, paddedPlaintext, 0, input.length);
        
        //byte arrays initialize to 0, so it is only necessary to write the 0xFF byte
        paddedPlaintext[input.length] = (byte) 0x80;
        return paddedPlaintext;
    }
    
    public byte[] removePadding(byte[] input) {
        //Determine how many padding bytes there are
        //Start where K1 000 padding ends, continue until we hit 0xFF
        int paddingIndex = 0;
        for (int i = (input.length - 1); i >= 0; i--) {
        	if (input[i] == (byte) 0x80) {
        		paddingIndex = i;
        		break;
        	}
        }
        
        //remove padding from message
        byte[] plaintext = new byte[paddingIndex];
        System.arraycopy(input, 0, plaintext, 0, paddingIndex);
        
        return plaintext;
    }
}
