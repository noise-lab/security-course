//TO DO: Add test for not using the offsets!

import java.util.Arrays;
import java.util.Random;

public class TestStreamCipher {

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
    	byte[] nonce = new byte[AuthEncryptor.NONCE_SIZE_BYTES];
    	for (int i = 0; i < AuthEncryptor.NONCE_SIZE_BYTES; i++) {
    		nonce[i] = (byte) i;
    	}
    	return nonce;
    }
    
    private static byte[] getOneNonce() {
    	byte[] nonce = new byte[AuthEncryptor.NONCE_SIZE_BYTES];
    	for (int i = 0; i < AuthEncryptor.NONCE_SIZE_BYTES; i++) {
    		nonce[i] = (byte) 1;
    	}
    	return nonce;
    }
    
    private static byte[] getZeroNonce() {
    	byte[] nonce = new byte[AuthEncryptor.NONCE_SIZE_BYTES];
    	for (int i = 0; i < AuthEncryptor.NONCE_SIZE_BYTES; i++) {
    		nonce[i] = (byte) 0;
    	}
    	return nonce;
    }

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

private static int testCryptByteEncryption()
{
    System.out.printf("Test 1: Testing distribution of the output of StreamCipher's .cryptByte() method\n");  	
    try { 

        byte[] key = getKey(false, StreamCipher.KEY_SIZE_BYTES);
        StreamCipher stEncryptor = new StreamCipher(key, getZeroNonce());

        int NUM_BYTES = 4096;
        int NUM_BITS = NUM_BYTES * 8;
        int MIN_EXPECTED_ONES = (int) (NUM_BITS * 0.4);
        int MAX_EXPECTED_ONES = (int) (NUM_BITS * 0.6);
        boolean passed = true;


        System.out.printf("  *  Testing that an encrypting StreamCipher generates an even distribution of 0s and 1s for an all 0 input\n");  	
        
        byte [] encryptedZeros = new byte[NUM_BYTES];
        for (int i = 0; i < NUM_BYTES; i++)
           encryptedZeros[i] = stEncryptor.cryptByte( (byte) 0);	

       int oneCountEncryptedZeros = countOnes(encryptedZeros);
       double percentage = 100.0 * oneCountEncryptedZeros / NUM_BITS;
       if ((oneCountEncryptedZeros < MIN_EXPECTED_ONES) || (oneCountEncryptedZeros > MAX_EXPECTED_ONES))
       {
        System.out.printf("     FAILED: When encrypting a bit stream of %d zeros, output has %d ones (%.2f%%)\n", NUM_BITS, oneCountEncryptedZeros, percentage);    		
        passed = false;
    }


    System.out.printf("  *  Testing that an encrypting StreamCipher generates an even distribution of 0s and 1s for an all 1 input\n");  	
    
    stEncryptor = new StreamCipher(key, getOneNonce());
    byte [] encryptedOnes = new byte[NUM_BYTES];
    for (int i = 0; i < NUM_BYTES; i++)
    	encryptedOnes[i] = stEncryptor.cryptByte( (byte) 1);

    int oneCountEncryptedOnes = countOnes(encryptedOnes);
    percentage = 100.0 * oneCountEncryptedOnes / NUM_BITS;
    if ((oneCountEncryptedOnes < MIN_EXPECTED_ONES) || (oneCountEncryptedOnes > MAX_EXPECTED_ONES))
    {
        System.out.printf("     FAILED: When encrypting a bit stream of %d ones, output has %d ones (%.2f%%)\n", NUM_BITS, oneCountEncryptedOnes, percentage);    		
        passed = false;
    }


    System.out.printf("  *  Testing that an encrypting StreamCipher generates an even distribution of 0s and 1s for a random bitstream input\n");  	

    stEncryptor = new StreamCipher(key, getNonce());
    byte [] randomBitStream = new byte[NUM_BYTES];
    
    Random rng = new Random();
    rng.nextBytes(randomBitStream);
    byte [] encryptedRandom = new byte[NUM_BYTES];
    for (int i = 0; i < NUM_BYTES; i++)
    	encryptedRandom[i] = stEncryptor.cryptByte(randomBitStream[i]);

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

private static int testCryptBytesEncryption()
{
    System.out.printf("Test 3: Testing distribution of the output of StreamCipher's .cryptBytes() method\n");  	
    try {

        byte[] key = getKey(false, StreamCipher.KEY_SIZE_BYTES);

        int NUM_BYTES = 4096;
        int NUM_BITS = NUM_BYTES * 8;
        int MIN_EXPECTED_ONES = (int) (NUM_BITS * 0.4);
        int MAX_EXPECTED_ONES = (int) (NUM_BITS * 0.6);
        boolean passed = true;

        System.out.printf("  *  Testing that an encrypting StreamCipher generates an even distribution of 0s and 1s for an all 0 input\n");  	

        StreamCipher stEncryptor = new StreamCipher(key, getZeroNonce());
        byte [] encryptedZeros = new byte[NUM_BYTES];
        byte [] zeroBitStream = new byte[NUM_BYTES];
        stEncryptor.cryptBytes(zeroBitStream, 0, encryptedZeros, 0, NUM_BYTES);	

        int oneCountEncryptedZeros = countOnes(encryptedZeros);
        double percentage = 100.0 * oneCountEncryptedZeros / NUM_BITS;
        if ((oneCountEncryptedZeros < MIN_EXPECTED_ONES) || (oneCountEncryptedZeros > MAX_EXPECTED_ONES))
        {
            System.out.printf("     FAILED: When encrypting a bit stream of %d zeros, output has %d ones (%.2f%%)\n", NUM_BITS, oneCountEncryptedZeros, percentage);    		
            passed = false;
        }


        System.out.printf("  *  Testing that an encrypting StreamCipher generates an even distribution of 0s and 1s for an all 1 input\n");  	

        stEncryptor = new StreamCipher(key, getOneNonce());
        byte [] encryptedOnes = new byte[NUM_BYTES];
        byte [] oneBitStream = new byte[NUM_BYTES];
        stEncryptor.cryptBytes(oneBitStream, 0, encryptedOnes, 0, NUM_BYTES);	

        int oneCountEncryptedOnes = countOnes(encryptedOnes);
        percentage = 100.0 * oneCountEncryptedOnes / NUM_BITS;
        if ((oneCountEncryptedOnes < MIN_EXPECTED_ONES) || (oneCountEncryptedOnes > MAX_EXPECTED_ONES))
        {
            System.out.printf("     FAILED: When encrypting a bit stream of %d ones, output has %d ones (%.2f%%)\n", NUM_BITS, oneCountEncryptedOnes, percentage);    		
            passed = false;
        }


        System.out.printf("  *  Testing that an encrypting StreamCipher generates an even distribution of 0s and 1s for a random bitstream input\n");  	

        stEncryptor = new StreamCipher(key, getNonce());
        byte [] randomBitStream = new byte[NUM_BYTES];
        
        Random rng = new Random();
        rng.nextBytes(randomBitStream);
        byte [] encryptedRandom = new byte[NUM_BYTES];
        stEncryptor.cryptBytes(randomBitStream, 0, encryptedRandom, 0, NUM_BYTES);	


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


private static int testCryptByteDecryption()
{
    System.out.printf("Test 2: Ensure that a decrypting StreamCipher can use .cryptByte() to correctly decrypt the output of an encrypting StreamCipher\n");  	

    try {
        byte[] key = getKey(false, StreamCipher.KEY_SIZE_BYTES);
        StreamCipher stEncryptor = new StreamCipher(key, getNonce());
        StreamCipher stDecryptor = new StreamCipher(key, getNonce());

        int NUM_BYTES = 128;

        byte [] bytesToBeEncrypted = new byte[NUM_BYTES];
        
        Random rng = new Random();
        rng.nextBytes(bytesToBeEncrypted);

        byte [] encryptedBytes = new byte[NUM_BYTES];
        byte [] decryptedBytes = new byte[NUM_BYTES];

        boolean passedDecryption = true;

        for (int i = 0; i < NUM_BYTES; i++)
        {
           encryptedBytes[i] = stEncryptor.cryptByte(bytesToBeEncrypted[i]);
           decryptedBytes[i] = stDecryptor.cryptByte(encryptedBytes[i]);
           if (decryptedBytes[i] != bytesToBeEncrypted[i])
           {
              passedDecryption = false;
              System.out.printf("     FAILED: Decrypted byte did not match encrypted byte.\n");    		
          }
      }

      if (passedDecryption)
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


private static int testCryptBytesDecryption()
{
    System.out.printf("Test 4: Ensure that a decrypting StreamCipher can use .cryptBytes() to correctly decrypt the output of an encrypting StreamCipher\n");  	
    try {
        byte[] key = getKey(false, StreamCipher.KEY_SIZE_BYTES);
        StreamCipher stEncryptor = new StreamCipher(key, getNonce());
        StreamCipher stDecryptor = new StreamCipher(key, getNonce());
        
        int NUM_BYTES = 128;

        byte [] bytesToBeEncrypted = new byte[NUM_BYTES];
        
        Random rng = new Random();
        rng.nextBytes(bytesToBeEncrypted);

        byte [] encryptedBytes = new byte[NUM_BYTES];
        byte [] decryptedBytes = new byte[NUM_BYTES];

        boolean passedDecryption = true;

        stEncryptor.cryptBytes(bytesToBeEncrypted, 0, encryptedBytes, 0, NUM_BYTES);
        stDecryptor.cryptBytes(encryptedBytes, 0, decryptedBytes, 0, NUM_BYTES);


        for (int i = 0; i < NUM_BYTES; i++)
        {
           if (decryptedBytes[i] != bytesToBeEncrypted[i])
           {
              passedDecryption = false;
              System.out.printf("     FAILED: Decrypted byte did not match encrypted byte.\n");    		
          }
      }

      if (passedDecryption)
      {
       System.out.printf("==> passed\n");
       return 1;
   }
   else
   {
      System.out.printf("==> FAILED\n");
      return 0;
  }
}
catch (Throwable e) {
    UtilCOS.printError(e);
    return 0;
}
}

private static int testNonce()
{
    System.out.printf("\nTest 5: Ensure that cryptBytes returns different values for different nonces\n");  	
    try {
        byte[] key = getKey(false, StreamCipher.KEY_SIZE_BYTES);
        StreamCipher stEncryptor1 = new StreamCipher(key, getNonce());
        StreamCipher stEncryptor2 = new StreamCipher(key, getOneNonce());
        
        int NUM_BYTES = 128;

        byte [] bytesToBeEncrypted = new byte[NUM_BYTES];
        Random rng = new Random();
        rng.nextBytes(bytesToBeEncrypted);

        byte [] encryptedBytes1 = new byte[NUM_BYTES];
        byte [] encryptedBytes2 = new byte[NUM_BYTES];

        stEncryptor1.cryptBytes(bytesToBeEncrypted, 0, encryptedBytes1, 0, NUM_BYTES);
        stEncryptor2.cryptBytes(bytesToBeEncrypted, 0, encryptedBytes2, 0, NUM_BYTES);

      if (!Arrays.equals(encryptedBytes1, encryptedBytes2))
      {
       System.out.printf("==> passed\n");
       return 1;
   }
   else
   {
      System.out.printf("==> FAILED\n");
      return 0;
  }
}
catch (Throwable e) {
    UtilCOS.printError(e);
    return 0;
}
}

private static int probeEmptyBehavior()
{
  System.out.printf("\nProbe 1: Testing how your code reacts to weird inputs\n");

 try{
  System.out.printf("  *  Creating StreamCipher with 0 byte key, then calling .cryptByte(127)\n");

  StreamCipher sc = new StreamCipher(new byte[0], getNonce());
  int output = sc.cryptByte((byte) 127);
  System.out.printf("     Output is %d\n", output);

}
   catch (Throwable e) {
    UtilCOS.printError(e);
  }  

 try{
  System.out.printf("  *  Creating StreamCipher with a good key, then calling .cryptBytes() with zero length inbuf and numBytes=1\n");

  StreamCipher sc = new StreamCipher(getKey(false, StreamCipher.KEY_SIZE_BYTES), getNonce());
  byte [] outputBuffer = new byte[10];
  sc.cryptBytes(new byte[0], 0, outputBuffer, 0, 1);
  System.out.printf("     outputBuffer[0] is %d\n", outputBuffer[0]);

}
   catch (Throwable e) {
    UtilCOS.printError(e);
  }  

  System.out.printf("==> Probing completed (no-autograding of results)\n");
  return 0;

}

public static void main(String[] args) {
		//all current tests use only one key!
  int numTests = 5;
  int numPassed = 0;

  UtilCOS.printTotalNumChecks(numTests); 	

  numPassed += testCryptByteEncryption();
  numPassed += testCryptByteDecryption();
  numPassed += testCryptBytesEncryption();
  numPassed += testCryptBytesDecryption();
  numPassed += testNonce();

  System.out.printf("\n");
  UtilCOS.printNumChecksPassed(numPassed, numTests);		

  probeEmptyBehavior();

}
}