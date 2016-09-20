/*
 * Conversations between BigInteger and byte[] are a hassle. This class should help.
 * 
 * There are two scenarios:
 * 		(1) Converting BigInteger -> byte[] -> BigInteger
 *			-> Use BigInteger.toByteArray() and BigInteger(byte[]) 
 *
 * 		(2) Converting byte[] -> BigInteger -> byte[]
 * 			-> Using the built in methods can lead to errors, instead, you should 
 *             use the following methods.
 * 			-> bigInt = HW2Util.bytesToBigInteger(byteArray)
 * 			   < BigInteger operations on bigInt > 
 * 			   byteArray = HW2Util.bigIntegertoBytes(bigInt, messageLength)
 * 			-> Note messageLength must be the exact length of byteArray
 * 			   so you will have to save that length or consider what constants 
 *             the length of byteArray is based on. 
 */
import java.math.BigInteger;

public class HW2Util {
    public static BigInteger bytesToBigInteger(byte[] buf) {
    	// convert a byte-array to a BigInteger
    	return new BigInteger(1, buf);
    }

    public static byte[] bigIntegerToBytes(BigInteger x, int outputSize) {
		// Convert the BigInteger x to a byte-array
		// x must be non-negative
		// outputSize is the expected size of the output array
		//     (you need to supply this because the code here can't tell how
		//      big an array the caller wants)
		//
		// This operation is the inverse of <bytesToBigInteger>.
	
		assert x.compareTo(BigInteger.ZERO) >= 0;
	
		byte[] rawByteArray = x.toByteArray();
		if(rawByteArray.length==outputSize)    return rawByteArray;
	
		byte[] ret = new byte[outputSize];
		if(rawByteArray.length > outputSize){
		    assert (rawByteArray.length == outputSize+1);
		    // a sign-extension byte got added; remove it
		    for(int i=0; i<outputSize; ++i){
			ret[i] = rawByteArray[i+1];
		    }
		}else{  // rawByteArray.length < outputSize
		    int diff = outputSize-rawByteArray.length;
		    for(int i=0; i<outputSize; ++i){
			ret[i] = (i<diff) ? 0 : rawByteArray[i-diff];
		    }
		}
		return ret;
    }

    public static void main(String[] argv) {  // do some basic tests
		BigInteger[] vals = { BigInteger.ZERO, BigInteger.ONE, BigInteger.TEN };
	
		for(int i=0; i<vals.length; ++i){
		    BigInteger result = bytesToBigInteger(bigIntegerToBytes(vals[i], 40));
		    if( ! vals[i].equals(result) ){
			System.out.println(vals[i].toString() + " " + result.toString());
		    }
		}

		System.out.println("OK");
    }
}