
import java.math.BigInteger;


public class KeyExchange {
	public static final int OUTPUT_SIZE_BYTES = PRF.OUTPUT_SIZE_BYTES;
	public static final int OUTPUT_SIZE_BITS = 8*OUTPUT_SIZE_BYTES;

	private static final BigInteger g = DHConstants.g;
	private static final BigInteger p = DHConstants.p;
	private static final BigInteger pMinusOne = p.subtract(BigInteger.ONE);

	private BigInteger x;
	private BigInteger gx;

    private byte[] prfKeyForHash = new byte[PRF.KEY_SIZE_BYTES];   // will be filled with zeroes
    private PRF    prfForHash = new PRF(prfKeyForHash);

    public KeyExchange(PRGen rand, boolean iAmServer) {
	// Prepares to do a key exchange.   <rand> is a secure pseudorandom generator
	//    that can be used by the implementation.   <iAmServer> is true iff we are
	//    playing the server role in this exchange.   Each exchange has two 
	//    participants; one of them plays the client role and the other plays the
	//    server role.
	//
	// Once the KeyExchange object is created, two things have to happen for the 
	//    key exchange process to be complete.
	// 1.  Call prepareOutMessage on this object, and send the result to the other
        //     participant.
        // 2.  Receive the result of the other participant's prepareOutMessage, and pass it in
        //     as the argument to a call on this object's processInMessage.  
	// These two things can happen in either order, or even concurrently (e.g., in 
        //     different threads).  This code must work correctly regardless of the order.
        //
	// The call to processInMessage should behave as follows:
        //     If passed a null value, then throw a NullPointerException.
        //     Otherwise, if passed a value that could not possibly have been generated
        //        by prepareOutMessage, then return null.
        //     Otherwise, return a "digest" value with the property described below.
	//
	// This code must provide the following security guarantee: If the two 
	//    participants end up with the same non-null digest value, then this digest value
	//    is not known to anyone else.   This must be true even if third parties
	//    can observe and modify the messages sent between the participants.
	// This code is NOT required to check whether the two participants end up with
	//    the same digest value; the code calling this must verify that property.

    	do {
    		x = new BigInteger(p.bitLength()-1, 128, rand);
    		gx = g.modPow(x, p);
    	} while(gx.equals(BigInteger.ONE) || gx.equals(pMinusOne));
    }

    public byte[] prepareOutMessage() {
    	return gx.toByteArray();
    }

    public byte[] processInMessage(byte[] inMessage) {
    	if(inMessage == null)    throw new NullPointerException();

    	BigInteger gy = new BigInteger(inMessage);

    	if(gy.compareTo(BigInteger.ONE) <= 0)    return null;
    	if(gy.compareTo(pMinusOne) >= 0)    return null;

    	BigInteger gxy = gy.modPow(x, p);
    	return prfForHash.eval(gxy.toByteArray());
    }

    public static void main(String[] argv) {
    	byte[] prgSeed = new byte[PRGen.KEY_SIZE_BYTES];
    	byte[] randBytes = TrueRandomness.get();
    	for(int i=0; i<TrueRandomness.NumBytes; ++i) {
    		prgSeed[i] = randBytes[i];
    	}
    	PRGen prg = new PRGen(prgSeed);

    	for(int j=0; j<42; ++j){
    		KeyExchange ke1 = new KeyExchange(prg, true);
    		KeyExchange ke2 = new KeyExchange(prg, false);
    		byte[] dig1 = ke1.processInMessage(ke2.prepareOutMessage());
    		byte[] dig2 = ke2.processInMessage(ke1.prepareOutMessage());
    		assert dig1.length == dig2.length;
    		for(int i=0; i<dig1.length; ++i){
    			assert dig1[i] == dig2[i];
    		}
    	}
    }
  }
