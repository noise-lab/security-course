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
public class AuthDecryptor {
    // Class constants.
    public static final int   KEY_SIZE_BYTES = AuthEncryptor.KEY_SIZE_BYTES;
    public static final int NONCE_SIZE_BYTES = AuthEncryptor.NONCE_SIZE_BYTES;

    // Instance variables.
    // IMPLEMENT THIS

    public AuthDecryptor(byte[] key) {
        assert key.length == KEY_SIZE_BYTES;
        // IMPLEMENT THIS
    }

    // Decrypts and authenticates the contents of <in>.  <in> should have been encrypted
    // using your implementation of AuthEncryptor.
    // The nonce has been included in <in>.
    // If the integrity of <in> cannot be verified, then returns null.  Otherwise,
    // returns a newly allocated byte[] containing the plaintext value that was
    // originally encrypted.
    public byte[] decrypt(byte[] in) {
        throw new RuntimeException("Unimplemented.");
        // IMPLEMENT THIS
    }

    // Decrypts and authenticates the contents of <in>.  <in> should have been encrypted
    // using your implementation of AuthEncryptor.
    // The nonce used to encrypt the data is provided in <nonce>.
    // If the integrity of <in> cannot be verified, then returns null.  Otherwise,
    // returns a newly allocated byte[] containing the plaintext value that was
    // originally encrypted.
    public byte[] decrypt(byte[] in, byte[] nonce) {
        assert nonce != null && nonce.length == NONCE_SIZE_BYTES;
        throw new RuntimeException("Unimplemented.");
        // IMPLEMENT THIS
    }
}
