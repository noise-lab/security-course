import java.util.Arrays;
import java.util.Random;

public class TestAuthEncryptor {
  private static PRGen getPRG(boolean randomKey)
  {
   PRGen prg = new PRGen(getKey(randomKey, PRGen.KEY_SIZE_BYTES));
   return prg;
}

private static byte[] getKey(boolean randomKey, int bytes)
{
    if(randomKey)
    {
      Random rng = new Random();
      byte[] key = new byte[bytes];
      rng.nextBytes(key);
      return key;
    }
    else
    {
        byte[] fixedKey = new byte[bytes];
        for (int i = 0; i < bytes; i++)
         fixedKey[i] = (byte) bytes;

     return fixedKey;
 }
}

private static int countOnes(byte[] someBytes)
{
    int onesCount = 0;
    for (int    i = 0; i < someBytes.length; i++)
    {
       int thisByte = someBytes[i];
       if (thisByte < 0)
          thisByte = -thisByte + 127;

      onesCount += countOnes(thisByte);
  }
  return onesCount;
}


private static int countOnes(int someInt)
{
    int onesCount = 0;
    for (int    i = 0; i < 32; i++)
    {
        onesCount += someInt & 1;
        someInt = someInt >> 1;
    }
    return onesCount;
}

private static byte[] getNonce() {
	return new byte[AuthEncryptor.NONCE_SIZE_BYTES];
}

private static int testEncryptedDataDistribution()
{
    System.out.printf("Test 1: Testing distribution of the output of AuthEncryptor's .encrypt() method\n");  	
    try { 


        byte[] key = getKey(false, AuthEncryptor.KEY_SIZE_BYTES);
        //System.out.println("key is length: " + key.length +  ", and AuthEncryptor.KEY_SIZE_BYTES is " + AuthEncryptor.KEY_SIZE_BYTES);

        AuthEncryptor AuthEncryptor = new AuthEncryptor(key);


        int NUM_BYTES = 4096;
        int NUM_BITS = NUM_BYTES * 8;
        int MIN_EXPECTED_ONES = (int) (NUM_BITS * 0.4);
        int MAX_EXPECTED_ONES = (int) (NUM_BITS * 0.6);
        boolean passed = true;


        System.out.printf("  *  Testing that AuthEncryptor's encrypt() method generates an even distribution of 0s and 1s for an all 0 input\n");  	

        byte [] encryptedZeros = new byte[NUM_BYTES];
        byte [] zeroBitStream = new byte[NUM_BYTES];
        encryptedZeros = AuthEncryptor.encrypt(zeroBitStream, getNonce(), false);

        int oneCountEncryptedZeros = countOnes(encryptedZeros);
        double percentage = 100.0 * oneCountEncryptedZeros / NUM_BITS;
        if ((oneCountEncryptedZeros < MIN_EXPECTED_ONES) || (oneCountEncryptedZeros > MAX_EXPECTED_ONES))
        {
            System.out.printf("     FAILED: When encrypting a bit stream of %d zeros, output has %d ones (%.2f%%)\n", NUM_BITS, oneCountEncryptedZeros, percentage);    		
            passed = false;
        }


        System.out.printf("  *  Testing that AuthEncryptor's encrypt() method  generates an even distribution of 0s and 1s for an all 1 input\n");  	

        byte [] encryptedOnes = new byte[NUM_BYTES];
        byte [] oneBitStream = new byte[NUM_BYTES];
        encryptedOnes = AuthEncryptor.encrypt(oneBitStream, getNonce(), false);

        int oneCountEncryptedOnes = countOnes(encryptedOnes);
        percentage = 100.0 * oneCountEncryptedOnes / NUM_BITS;
        if ((oneCountEncryptedOnes < MIN_EXPECTED_ONES) || (oneCountEncryptedOnes > MAX_EXPECTED_ONES))
        {
            System.out.printf("     FAILED: When encrypting a bit stream of %d ones, output has %d ones (%.2f%%)\n", NUM_BITS, oneCountEncryptedOnes, percentage);    		
            passed = false;
        }


        System.out.printf("  *  Testing that AuthEncryptor's encrypt() method  generates an even distribution of 0s and 1s for a random bitstream input\n");  	

        byte [] randomBitStream = new byte[NUM_BYTES];

        Random rng = new Random();
        rng.nextBytes(randomBitStream);
        byte [] encryptedRandom = new byte[NUM_BYTES];
        encryptedRandom = AuthEncryptor.encrypt(randomBitStream, getNonce(), false);


        int oneCountEncryptedRandom = countOnes(encryptedRandom);
        percentage = 100.0 * oneCountEncryptedRandom / NUM_BITS;
        if ((oneCountEncryptedRandom < MIN_EXPECTED_ONES) || (oneCountEncryptedRandom > MAX_EXPECTED_ONES))
        {
            System.out.printf("     FAILED: When encrypting a random bit stream of %d bits, output has %d ones (%.2f%%)\n", NUM_BITS, oneCountEncryptedRandom, percentage);    		
            passed = false;
        }

        if (passed)
        {
           System.out.println("==> passed\n");
           return 1;
       }
       else
       {
           System.out.println("==> FAILED\n");
           return 0;    	
       }
   }
   catch (Throwable e) {
    UtilCOS.printError(e);
    return 0;
  }

}

private static int testThatLargerInputMakesLargerOutput()
{
    System.out.printf("Test 2: Ensuring that the output of your AuthEncryptor is larger when input is larger with same nonce\n");   

    try{

        int NUM_BYTES_1 = 163;
        int NUM_BYTES_2 = 200;

        byte [] randomBitStream_1 = new byte[NUM_BYTES_1];
        Random rng = new Random();
        rng.nextBytes(randomBitStream_1);

        byte [] randomBitStream_2 = new byte[NUM_BYTES_2];
        rng.nextBytes(randomBitStream_2);

        AuthEncryptor ae = new AuthEncryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));

	    byte [] Encrypted1 = ae.encrypt(randomBitStream_1, getNonce(), false);
	    byte [] Encrypted2 = ae.encrypt(randomBitStream_2, getNonce(), false);
	    if (Encrypted2.length > Encrypted1.length)
	    {
	        System.out.printf("==> passed\n\n");
	        return 1;
	    }
	    else
	    {
	        System.out.printf("==> FAILED (output size 1: %d bytes, output size 2: %d bytes)\n\n", Encrypted2.length, Encrypted1.length);     
	        return 0;
	    }
	} catch (Throwable e) {
	    UtilCOS.printError(e);
	    return 0;
	}
}

private static int testRepeatedDataBehavior()
{
	System.out.printf("Test 3: Ensuring that two calls to .encrypt(inputData) with the same inputData and a different Nonce does not return the same output.\n");  	
    try {

        int NUM_BYTES = 4096;

        byte [] randomBitStream = new byte[NUM_BYTES];
        Random rng = new Random();
        rng.nextBytes(randomBitStream);

        AuthEncryptor ae = new AuthEncryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));
        byte[] aNonce = getNonce();
        byte [] Encrypted1 = ae.encrypt(randomBitStream, aNonce, false);
        aNonce[0] += 1;
        byte [] Encrypted2 = ae.encrypt(randomBitStream, aNonce, false);

        boolean passed = (!Arrays.equals(Encrypted1, Encrypted2));

        if (passed)
        {
           System.out.printf("==> passed\n\n");		
           return 1;
       }
       else
       {
           System.out.printf("==> FAILED, calls with different nonces resulted in equal data! You are vulnerable to duplication attacks by Mallory.\n\n");		
           return 0;
       }
   }
   catch (Throwable e) {
    UtilCOS.printError(e);
    return 0;
}
}

private static int testThatOutputLargerThanInput()
{
    System.out.printf("Test 4: Ensuring that the output of your AuthEncryptor is larger than the input (as a proxy for existence of MAC)\n");   

    try{

        int NUM_BYTES = 16384;

        byte [] randomBitStream = new byte[NUM_BYTES];
        Random rng = new Random();
        rng.nextBytes(randomBitStream);

        AuthEncryptor ae = new AuthEncryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));

    byte [] Encrypted1 = ae.encrypt(randomBitStream, getNonce(), false); //should be larger than randomBitStream with almost certain probability
                                                //this assumption fails only if bit stream is compressible and student 
                                                //compresses
    if (Encrypted1.length >= randomBitStream.length + 8) //at a minimum 8 bytes are needed to provide 2^64 different MACs
    {
        System.out.printf("==> passed\n\n");
        return 1;
    }
    else
    {
        System.out.printf("==> FAILED (input bitStream size: %d bytes, output of AuthEncryptor: %d bytes)\n\n", randomBitStream.length, Encrypted1.length);     
        return 0;
    }
}
catch (Throwable e) {
    UtilCOS.printError(e);
    return 0;
}
}

private static int testThatOutputWithNonceLarger()
{
    System.out.printf("Test 5: Ensuring that the length of AuthEncryptor output with nonce == AuthEncryptor without nonce + nonce size\n");   

    try{

        int NUM_BYTES = 16384;

        byte [] randomBitStream = new byte[NUM_BYTES];
        Random rng = new Random();
        rng.nextBytes(randomBitStream);

        AuthEncryptor ae = new AuthEncryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));

	    byte [] Encrypted1 = ae.encrypt(randomBitStream, getNonce(), false);
	    byte [] Encrypted2 = ae.encrypt(randomBitStream, getNonce(), true);
	    if (Encrypted2.length == Encrypted1.length + AuthEncryptor.NONCE_SIZE_BYTES)
	    {
	        System.out.printf("==> passed\n\n");
	        return 1;
	    }
	    else
	    {
	        System.out.printf("==> FAILED (output size with nonce: %d bytes, output size without nonce: %d bytes, nonce size: %d bytes)\n\n", Encrypted2.length, Encrypted1.length, AuthEncryptor.NONCE_SIZE_BYTES);     
	        return 0;
	    }
	} catch (Throwable e) {
	    UtilCOS.printError(e);
	    return 0;
	}
}

private static int probeEmptyBehavior()
{
  System.out.printf("\nProbe 1: Probing to see how your code reacts to weird inputs\n");

 try{
  System.out.printf("  *  Creating AuthEncryptor with 0 byte key, then calling .encrypt(new byte[]{5, 6})\n");

  AuthEncryptor ae = new AuthEncryptor(new byte[0]);
  byte[] output = ae.encrypt(new byte[]{5, 6}, getNonce(), false);
  System.out.printf("     Output byte stream address is " + output + "\n");
  if (output != null)
  {
    System.out.printf("     Output byte stream length is %d\n", output.length);
    System.out.printf("     Output[0] is %d\n", output[0]);
  }
}
   catch (Throwable e) {
    UtilCOS.printError(e);
  }  

 try{
  System.out.printf("  *  Creating AuthEncryptor with a good key, then calling .encrypt() on an empty input stream\n");

  AuthEncryptor ae = new AuthEncryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));
  byte[] output = ae.encrypt(new byte[0], getNonce(), false);
  System.out.printf("     Output byte stream address is " + output + "\n");
  if (output != null)
  {
    System.out.printf("     Output byte stream length is %d\n", output.length);
    System.out.printf("     Output[0] is %d\n", output[0]);
  }
}
   catch (Throwable e) {
    UtilCOS.printError(e);
  }  

  System.out.printf("\n==> Probing completed (no-autograding of results)\n");
  return 0;

}


public static void main(String[] args)
{
	int numTests = 5;
	int numPassed = 0;

    UtilCOS.printTotalNumChecks(numTests); 	
    numPassed += testEncryptedDataDistribution();
    numPassed += testThatLargerInputMakesLargerOutput();
    numPassed += testRepeatedDataBehavior();
    numPassed += testThatOutputLargerThanInput();
    numPassed += testThatOutputWithNonceLarger();

    UtilCOS.printNumChecksPassed(numPassed, numTests);

    probeEmptyBehavior();


}

}