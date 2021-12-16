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
    private byte[] encKey;
    private PRF    mac;

    public AuthEncryptor(byte[] key) {
        assert key.length == KEY_SIZE_BYTES;
        
        // Split the single key into encryption and mac keys.
        PRGen prg = new PRGen(key);
        encKey        = new byte[StreamCipher.KEY_SIZE_BYTES];
        byte[] macKey = new byte[StreamCipher.KEY_SIZE_BYTES];
        prg.nextBytes(encKey);
        prg.nextBytes(macKey);

        // Create a PRF for MAC purposes.
        mac = new PRF(macKey);
    }

    // Encrypts the contents of <in> so that its confidentiality and integrity are
    // protected against those who do not know the key and nonce.
    // If <nonceIncluded> is true, then the nonce is included in plaintext with the
    // output.
    // Returns a newly allocated byte[] containing the authenticated encryption of
    // the input.
    public byte[] encrypt(byte[] in, byte[] nonce, boolean includeNonce) {
        // Allocate an output array.
        int outSize = in.length + PRF.OUTPUT_SIZE_BYTES;
        if (includeNonce) outSize += NONCE_SIZE_BYTES;
        byte[] out = new byte[outSize];

        // Encrypt the contents of <in>.
        StreamCipher sc = new StreamCipher(encKey, nonce);
        sc.cryptBytes(in, 0, out, 0, in.length);

        // Add a MAC to the output, taking the nonce into account.
        mac.update(nonce);
        mac.eval(out, 0, in.length, out, in.length);

        // Add the nonce if necessary.
        if (includeNonce) {
            int nonceOffset = out.length - NONCE_SIZE_BYTES;
            System.arraycopy(nonce, 0, out, nonceOffset, NONCE_SIZE_BYTES);
        }

        return out;
    }
}
