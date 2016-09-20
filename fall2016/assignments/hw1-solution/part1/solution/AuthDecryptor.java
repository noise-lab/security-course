/**********************************************************************************/
/* AuthDecrytor.java                                                              */
/* ------------------------------------------------------------------------------ */
/* DESCRIPTION: Performs authenticated decryption of data encrypted using         */
/*              AuthEncryptor.java.                                               */
/* ------------------------------------------------------------------------------ */
/* YOUR TASK: Decrypt data encrypted by your implementation of AuthEncryptor.java */
/*            if provided with the appropriate key and nonce.  If the data has    */
/*            been tampered with, return null.                                    */
/*                                                                                */
/**********************************************************************************/
import java.util.Arrays;

public class AuthDecryptor {
    // Class constants.
    public static final int   KEY_SIZE_BYTES = AuthEncryptor.KEY_SIZE_BYTES;
    public static final int NONCE_SIZE_BYTES = AuthEncryptor.NONCE_SIZE_BYTES;

    // Instance variables.
    private byte[] decKey;
    private PRF    mac;

    public AuthDecryptor(byte[] key) {
        assert key.length == KEY_SIZE_BYTES;

        // Split the single key into encryption and mac keys.
        PRGen prg = new PRGen(key);
        decKey        = new byte[StreamCipher.KEY_SIZE_BYTES];
        byte[] macKey = new byte[StreamCipher.KEY_SIZE_BYTES];
        prg.nextBytes(decKey);
        prg.nextBytes(macKey);

        // Create a PRF for MAC purposes.
        mac = new PRF(macKey);
    }

    // Decrypts and authenticates the contents of <in>.  <in> should have been encrypted
    // using your implementation of AuthEncryptor.
    // The nonce has been included in <in>.
    // If the integrity of <in> cannot be verified, then returns null.  Otherwise,
    // returns a newly allocated byte[] containing the plaintext value that was
    // originally encrypted.
    public byte[] decrypt(byte[] in) {
        // Extract the nonce.

        byte[] nonce = new byte[NONCE_SIZE_BYTES];
        System.arraycopy(in, in.length - NONCE_SIZE_BYTES, nonce, 0, NONCE_SIZE_BYTES);

        // Call the overload of decrypt.
        return decrypt(Arrays.copyOf(in, in.length - NONCE_SIZE_BYTES), nonce);
    }

    // Decrypts and authenticates the contents of <in>.  <in> should have been encrypted
    // using your implementation of AuthEncryptor.
    // The nonce used to encrypt the data is provided in <nonce>.
    // If the integrity of <in> cannot be verified, then returns null.  Otherwise,
    // returns a newly allocated byte[] containing the plaintext value that was
    // originally encrypted.
    public byte[] decrypt(byte[] in, byte[] nonce) {
        assert nonce != null && nonce.length == NONCE_SIZE_BYTES;
        
        // Verify the integrity of the message.
        int macOffset = in.length - PRF.OUTPUT_SIZE_BYTES;
        mac.update(nonce);
        byte[] expectedMac = mac.eval(in, 0, macOffset);
        byte[]   actualMac = Arrays.copyOfRange(in, macOffset, in.length);
        if (!Arrays.equals(expectedMac, actualMac)) return null;

        // Decrypt the message.
        int outSize = macOffset;
        byte[] out = new byte[outSize];
        StreamCipher sc = new StreamCipher(decKey, nonce);
        sc.cryptBytes(in, 0, out, 0, outSize);
        
        return out;
    }
}
