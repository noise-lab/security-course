/**********************************************************************************/
/* AuthEncryptor.java                                                             */
/* ------------------------------------------------------------------------------ */
/* DESCRIPTION: Performs authenticated encryption of data.                        */
/* ------------------------------------------------------------------------------ */
/* YOUR TASK: Implement authenticated encryption, ensuring:                       */
/*            (1) Confidentiality: the only way to recover encrypted data is to   */
/*                perform authenticated decryption with the same key and nonce    */
/*                used to encrypt the data.                                       */
/*            (2) Integrity: A party decrypting the data using the same key and   */
/*                nonce that were used to encrypt it can verify that the data has */
/*                not been modified since it was encrypted.                       */
/*                                                                                */
/**********************************************************************************/
public class AuthEncryptor {
    // Class constants.
    public static final int   KEY_SIZE_BYTES = StreamCipher.KEY_SIZE_BYTES;
    public static final int NONCE_SIZE_BYTES = StreamCipher.NONCE_SIZE_BYTES;

    // Instance variables.
    // IMPLEMENT THIS

    public AuthEncryptor(byte[] key) {
        assert key.length == KEY_SIZE_BYTES;

        // IMPLEMENT THIS
    }

    // Encrypts the contents of <in> so that its confidentiality and integrity are
    // protected against those who do not know the key and nonce.
    // If <nonceIncluded> is true, then the nonce is included in plaintext with the
    // output.
    // Returns a newly allocated byte[] containing the authenticated encryption of
    // the input.
    public byte[] encrypt(byte[] in, byte[] nonce, boolean includeNonce) {
        throw new RuntimeException("Unimplemented.");
        // IMPLEMENT THIS
    }
}
