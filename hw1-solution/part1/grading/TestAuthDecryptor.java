import java.util.Arrays;
import java.util.Random;

public class TestAuthDecryptor {

  private static byte[][] randomBitStreams(int numStreams, int numBytes)
  {

  	byte [][] randomBitStreams = new byte[numStreams][numBytes];

  	for (int i = 0; i < numStreams; i++)
  		randomBitStreams[i] = randomBitStream(numBytes);

  	return randomBitStreams;
  }

  private static byte[] randomBitStream(int numBytes)
  {
	byte [] randomBitStream = new byte[numBytes];
	Random rng = new Random();
	rng.nextBytes(randomBitStream);

	return randomBitStream;
  }

  //private static byte[] getKey(boolean randomKey)
  //{
  //  if(randomKey)
  //  {
  //   TrueRandomness tr= new TrueRandomness();
  //   byte[] trs = tr.get();
  //   byte[] trl = new byte[32];
  //   System.arraycopy(trs, 0, trl, 0, 16); 
  //   System.arraycopy(trs, 0, trl, 16, 16); 

  //   return trl;
  //}
  //else
  //{
  //  byte[] fixedKey = new byte[32];
  //  for (int i = 0; i < 32; i++)
  //      fixedKey[i] = (byte) i;

  //  return fixedKey;
  //}
  //}

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
private static byte[] getNonce() {
	byte[] nonce = new byte[AuthEncryptor.NONCE_SIZE_BYTES];
	for (int i = 0; i < AuthEncryptor.NONCE_SIZE_BYTES; i++) {
		nonce[i] = (byte) i;
	}
	return nonce;
}
  
private static int testDecryptorWorks()
{
	System.out.printf("Test 1: Ensuring that your AuthDecryptor can correctly Decrypt a single message that was encrypted by your AuthEncryptor class\n");  	

	int NUM_BYTES = 4096;
	byte[] key = getKey(false, AuthEncryptor.KEY_SIZE_BYTES);

    byte [] randomBitStream = new byte[NUM_BYTES];
    Random rng = new Random();
    rng.nextBytes(randomBitStream);

	AuthEncryptor ae = new AuthEncryptor(key);
	AuthDecryptor ad = new AuthDecryptor(key);

	byte [] encrypted = ae.encrypt(randomBitStream, getNonce(), false);
	byte [] decrypted = ad.decrypt(encrypted, getNonce());

	boolean passed = Arrays.equals(randomBitStream, decrypted);

	if (passed)
	{
    	System.out.println("==> passed\n");		
		return 1;
	}
	else
	{
    	System.out.println("==> FAILED, the decrypted message differs from the input message.\n");		
		return 0;
	}	
}

private static int testDecryptorWorksMultiple()
{
	int NUM_STREAMS = 16;
	int NUM_BYTES = 4096;
	System.out.printf("Test 2: Ensuring that your AuthDecryptor can correctly Decrypt a sequence of %d messages created by your AuthEncryptor class\n", NUM_STREAMS);  	

    byte [][] randomBitStreams =randomBitStreams(NUM_STREAMS, NUM_BYTES);

	AuthEncryptor ae = new AuthEncryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));
	AuthDecryptor ad = new AuthDecryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));

	byte [][] encryptedBitStreams = new byte[NUM_STREAMS][];
	byte [][] decryptedBitStreams = new byte[NUM_STREAMS][];

	byte[] nonce = getNonce();
	for (int i = 0; i < randomBitStreams.length; i++)
	{
		encryptedBitStreams[i] = ae.encrypt(randomBitStreams[i], nonce, false);
		nonce[0] += 1;
	}

	nonce = getNonce();
	for (int i = 0; i < randomBitStreams.length; i++)
	{
		decryptedBitStreams[i] = ad.decrypt(encryptedBitStreams[i], nonce);
		nonce[0] += 1;
	}

	boolean passed = true;



	for (int i = 0; i < randomBitStreams.length; i++)
	{
		if (!Arrays.equals(randomBitStreams[i], decryptedBitStreams[i]))
		{
        	System.out.printf("==> FAILED: %dth decrypted message did not match the original message!\n", i);
        	passed = false;
        	return 0;
        }
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

private static int testDecryptorHandlesFaults()
{
	System.out.printf("Test 3: Ensuring that your AuthDecryptor returns null if something goes wrong\n");

	int numSubTests = 2;
	int numPassed = 0;

	numPassed += testDecryptorHandlesIncorrectKey();
	numPassed += testDecryptorHandlesIncorrectNonce();

	if (numPassed == numSubTests)
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

private static int testDecryptorHandlesIncorrectKey()
{
	System.out.printf("  *  Returns null if Decryptor has incorrect key\n");  	

	int NUM_BYTES = 4096;
	byte[] nonce = getNonce();
	byte[] sealerKey = getKey(false, AuthEncryptor.KEY_SIZE_BYTES);
	byte[] DecryptorKey = getKey(true, AuthEncryptor.KEY_SIZE_BYTES);

    byte [] randomBitStream = new byte[NUM_BYTES];
    Random rng = new Random();
    rng.nextBytes(randomBitStream);

	AuthEncryptor ae = new AuthEncryptor(sealerKey);
	AuthDecryptor ad = new AuthDecryptor(DecryptorKey);

	byte [] encrypted = ae.encrypt(randomBitStream, nonce, false);
	byte [] decrypted = ad.decrypt(encrypted, nonce);

	boolean passed = (decrypted == null);

	if (passed)
	{
		return 1;
	}
	else
	{
    	System.out.println("     FAILED, Decryptor had incorrect key, should have returned null\n");		
		return 0;
	}	

}

public static int testDecryptorHandlesIncorrectNonce()
{
	System.out.printf("  *  checking if decryption returns null when an incorrect Nonce is provided\n");

	int NUM_BYTES = 4096;

	byte [] randomBitStream = new byte[NUM_BYTES];
	Random rng = new Random();
	rng.nextBytes(randomBitStream);

	AuthEncryptor ae = new AuthEncryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));
	AuthDecryptor ad = new AuthDecryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));

	byte[] nonce = getNonce();
	byte[] encryptedBitStream = ae.encrypt(randomBitStream, nonce, false);

	for (int i = 0; i < nonce.length; i++) {
		nonce[i] += 1;
	}

	byte[] decryptedMessage = ad.decrypt(encryptedBitStream, nonce);		
	boolean textSame = (Arrays.equals(decryptedMessage,randomBitStream));

	if (Arrays.equals(decryptedMessage, null))
	{
		return 1;
	}
	else
	{
        if (textSame) {
		System.out.printf("     FAILED: Encrypting with one nonce and decrypting with another results in the correct plaintext.\n");
	}
	System.out.printf("     FAILED: Encrypting with one nonce and decrypting with another should return null, even if nonceincluded is false (which it is for this test).\n");
		return 0;
	}	

}

private static int testDecryptorHandlesNonce()
{
	System.out.printf("\nTest 4: Ensuring that your AuthDecryptor handles nonces correctly\n");

	int numSubTests = 1;
	int numPassed = 0;

	numPassed += testDecryptorSameWithNonceIncludedOrNot();
	//numPassed += testNonceNotUsedWhenIncludedInMessage();

	if (numPassed == numSubTests)
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


private static int testDecryptorSameWithNonceIncludedOrNot()
{
	System.out.printf(" * Same decryption value whether or not includeNonce is used\n");

	int NUM_BYTES = 4096;
	byte[] nonce = getNonce();

    byte [] randomBitStream = new byte[NUM_BYTES];
    Random rng = new Random();
    rng.nextBytes(randomBitStream);
	
	AuthEncryptor ae = new AuthEncryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));
	AuthDecryptor ad = new AuthDecryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));
	
	byte[] encr1 = ae.encrypt(randomBitStream, nonce, false);
	byte[] encr2 = ae.encrypt(randomBitStream, nonce, true);

	byte[] decr1 = ad.decrypt(encr1, nonce);
	byte[] decr2 = ad.decrypt(encr2);
	
	boolean passed = (Arrays.equals(decr1, decr2) && !Arrays.equals(decr1, null));

	if (passed)
	{
		return 1;
	}
	else
	{
        System.out.printf("		FAILED: Same inputMessage was encrypted with and without includeNonce. Decrypted messages should be the same, they are not.\n");    		
		return 0;
	}
}

/* NOT NEEDED DUE TO API CHANGE
private static int testNonceNotUsedWhenIncludedInMessage()
{
	System.out.printf(" * Nonce is not used when nonceIncluded set\n");  	

	int NUM_BYTES = 4096;
	byte[] nonce = getNonce();

    byte [] randomBitStream = new byte[NUM_BYTES];
    Random rng = new Random();
    rng.nextBytes(randomBitStream);
	
	AuthEncryptor ae = new AuthEncryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));
	AuthDecryptor ad = new AuthDecryptor(getKey(false, AuthEncryptor.KEY_SIZE_BYTES));
	
	byte[] encr = ae.encrypt(randomBitStream, nonce, true);

	for (int i = 0; i < nonce.length; i++) {
		nonce[i] += 1;
	}
	byte[] decr = ad.decrypt(encr); //when nonceIncluded, nonce argument should be ignored..so decr text should equal encr text

	if (Arrays.equals(randomBitStream, decr))
	{
		return 1;
	}
	else
	{
        System.out.printf("	FAILED: Decrypted text changes with different nonce arguments despite nonceIncluded being set.\n");    		
		return 0;
	}	

}
*/
	public static void main(String[] args)
	{
		int numTests = 4;
		int numPassed = 0;

        UtilCOS.printTotalNumChecks(numTests);

		numPassed += testDecryptorWorks();
		numPassed += testDecryptorWorksMultiple();
		numPassed += testDecryptorHandlesFaults();
		numPassed += testDecryptorHandlesNonce();

		System.out.printf("\n");
        UtilCOS.printNumChecksPassed(numPassed, numTests);


	}

}
