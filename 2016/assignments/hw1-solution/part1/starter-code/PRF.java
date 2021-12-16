/**********************************************************************************/
/* PRF.java                                                                       */
/* ------------------------------------------------------------------------------ */
/* DESCRIPTION: This class implements a pseudorandom function.                    */
/* ------------------------------------------------------------------------------ */
/* NOTE: This is the only crypto code you are allowed to use for our assignment.  */
/*       You will not receive credit if you use any other crypto libraries.       */
/* ------------------------------------------------------------------------------ */
/* USAGE: To create a pseudo-random function with key k of length KEY_SIZE_BYTES: */
/*            PRF prf = new PRF(k);                                               */
/*                                                                                */
/*        A PRF object maintains a buffer of content on which it will eventually  */
/*        evaluate the pseudo-random function.  To add content to the buffer:     */
/*            prf.update(content);                                                */
/*        There are several overloads of update() that give you several different */
/*        ways of providing input to the PRF.                                     */
/*                                                                                */
/*        To evaluate the pseudo-random function on the contents of the buffer,   */
/*        call the eval() function:                                               */
/*            byte[] out = PRF.eval();                                            */
/*        <out> is the result of calling the pseudo-random function with key k    */
/*        on the concatenation of all content provided via calls via update()     */
/*        since the last call to eval(). <out> is of length OUTPUT_SIZE_BYTES.    */
/*                                                                                */
/*        Certain overloads of eval() take an argument:                           */
/*            PRF.eval(content)      ==      PRF.update(content); PRF.eval()      */
/*                                                                                */
/*        After a call to eval(), the buffer resets.                              */
/* ------------------------------------------------------------------------------ */
/* EXAMPLE:  PRF prf = new PRF(k);                                                */
/*           prf.update(s1);                                                      */
/*           prf.update(s2);                                                      */
/*           byte[] out1 = prf.eval(s3);                                          */
/*           prf.update(s4);                                                      */
/*           prf.update(s5);                                                      */
/*           byte[] out2 = prf.eval();                                            */
/*                                                                                */
/*     In cryptographic terms, this set of calls is equivalent to:                */
/*           out1 = PRF(k, s1 || s2 || s3);                                       */
/*           out2 = PRF(k, s4 || s5)                                              */
/*                                                                                */
/**********************************************************************************/
import java.security.Key;
import java.security.SecureRandom;
import javax.crypto.KeyGenerator;
import javax.crypto.Mac;

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

public class PRF {
    // Class constants.
    public static final int KEY_SIZE_BYTES    = 32;
    public static final int OUTPUT_SIZE_BYTES = 32;
    private static final String ALGORITHM_NAME = "HmacSHA256";

    // Instance variables.
    private Mac mac;

    // Creates a new PRF with key <prfKey>.
    public PRF(byte[] prfKey) {
        assert prfKey.length == KEY_SIZE_BYTES;
        
        try {
            mac = Mac.getInstance(ALGORITHM_NAME);
            KeyGenerator keygen = KeyGenerator.getInstance(ALGORITHM_NAME);
            SecureRandom secRand = SecureRandom.getInstance("SHA1PRNG");
            secRand.setSeed(prfKey);
            keygen.init(KEY_SIZE_BYTES * 8, secRand);
            Key key = keygen.generateKey();
            mac.init(key);
        } catch (NoSuchAlgorithmException x) {
            x.printStackTrace(System.err);
        } catch (InvalidKeyException x) {
            x.printStackTrace(System.err);
        }
    }

    // Adds input to buffer. Uses inBuf[inOffset] through inBuf[inOffset + nbytes - 1].
    public synchronized void update(byte[] inBuf, int inOffset, int numBytes) {
        mac.update(inBuf, inOffset, numBytes);
    }

    // Adds input to buffer. Uses the entirety of inBuf.
    public synchronized void update(byte[] inBuf) {
        update(inBuf, 0, inBuf.length);
    }

    // Adds input to buffer and evaluates the PRF on the contents of the buffer.
    // Uses inBuf[inOffset] through inBuf[inOffset + nbytes - 1] as additional input.
    // Throws an IndexOutOfBoundsException if either buffer is too small.
    public synchronized void eval(byte[]  inBuf, int  inOffset, int numBytes,
                                  byte[] outBuf, int outOffset) {
        try {
            mac.update(inBuf, inOffset, numBytes);
            mac.doFinal(outBuf, outOffset);
        } catch (javax.crypto.ShortBufferException e) {
            throw new IndexOutOfBoundsException();
        }
    }

    // Adds input to buffer and evaluates the PRF on the contents of the buffer.
    // Uses inBuf[inOffset] through inBuf[inOffset + nbytes - 1] as additional input.
    // Returns the result as a byte array of length OUTPUT_SIZE_BYTES.
    public synchronized byte[] eval(byte[] inBuf, int inOffset, int numBytes) {
        try {
            byte[] ret = new byte[OUTPUT_SIZE_BYTES];
            eval(inBuf, inOffset, numBytes, ret, 0);
            return ret;
        } catch (IndexOutOfBoundsException x) {
            // Should never happen - we allocated a big enough buffer.
            throw new RuntimeException("Should never get here.");
        }
    }

    // Evaluates the PRF on the contents of the buffer.
    // Returns the result as a byte array of length OUTPUT_SIZE_BYTES.
    public byte[] eval(byte[] val) {
        return eval(val, 0, val.length);
    }
 }
