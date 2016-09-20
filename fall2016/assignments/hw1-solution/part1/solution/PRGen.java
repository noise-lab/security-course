/**********************************************************************************/
/* PRGen.java                                                                     */
/* ------------------------------------------------------------------------------ */
/* DESCRIPTION: This class implements a backtracking-resistant pseudo-random      */
/*              generator.  It should produce a sequence of pseudo-random bits    */
/*              specified by a key of length <KEY_SIZE_BYTES>.                    */
/* ------------------------------------------------------------------------------ */
/* YOUR TASK: You must write a generator with the following properties:           */
/*            (1) It must be pseudo-random, meaning that there is no way to       */
/*                distinguish its output from that of a truly random generator    */
/*                unless you know the key.                                        */
/*            (2) It must be deterministic, meaning that, if two programs create  */
/*                generators with the same seed and make the same sequence of     */
/*                calls, they should receive the same sequence of bytes.          */
/*            (3) It must be backtracking-resistant, meaning that, even if an     */
/*                adversary observes the full state of the generator at time t,   */
/*                the adversary will not be able to determine the output of the   */
/*                generator at any time prior to t.                               */
/* ------------------------------------------------------------------------------ */
/* NOTE: This class extends java.util.Random, which means that, once implemented, */
/*       you have access to a number of useful utility methods for free.  We      */
/*       highly recommend that you look up the java.util.Random documentation to  */
/*       understand the full API of this class.  For example, you can write       */
/*           prg.nextBytes(outArray);                                             */
/*       instead of                                                               */
/*           for (int i = 0; i < outArray.length; i++) outArray[i] = prg.next();  */
/* ------------------------------------------------------------------------------ */
/* USAGE: Create a generator with a key k by calling the constructor:             */
/*            PRGen prg = new PRGen(k);                                           */
/*                                                                                */
/*        Retrieve pseudo-random bits from the sequence corresponding to key k by */
/*        calling next() (or any related method in the java.util.Random API):     */
/*            int r1 = prg.next(8);  // 8  pseudo-random bits                     */
/*            int r2 = prg.next(32); // 32 pseudo-random bits                     */
/*                                                                                */
/**********************************************************************************/

public class PRGen extends java.util.Random {
    // Class constants.
    public  static final int KEY_SIZE_BYTES = PRF.KEY_SIZE_BYTES;
    private static final byte[] OUT  = new byte[]{ 0 };
    private static final byte[] NEXT = new byte[]{ 1 };

    // Instance variables.
    private PRF prf;

    public PRGen(byte[] key) {
        super(); // Calls the parent class's constructor.  Leave this here.
        assert key.length == KEY_SIZE_BYTES;

        prf = new PRF(key);
    }

    // Returns an integer whose low-order <bits> bits are set pseudo-randomly. The
    // higher-order bits should be set to 0.
    protected int next(int bits) {
        assert 0 < bits && bits <= 32;

        // Generate the PRF output and update the state of the PRF.
        byte[] prfBytes = prf.eval(OUT);
        prf = new PRF(prf.eval(NEXT));

        // Convert the PRF output into an integer.
        int out = 0;
        for (int i = 0; i < bits; i++) {
            // There is a 1/2 probability that prfBytes[i] < 0.
            byte newBit = (prfBytes[i] < 0) ? (byte) 0x0 : (byte) 0x1;

            // Add the new bit onto the end of out.
            out = (out << 1) | newBit;
        }

        return out;
    }
}
