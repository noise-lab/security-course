import java.util.Random;
import java.util.Arrays;
import java.math.BigInteger;

public class TestRSAKey {
	
	public static byte[] getByteArray(int numBytes, boolean random) {
		byte[] out = new byte[numBytes];
		if (random) {
	      Random rng = new Random();
	      rng.nextBytes(out);
		} else {
			for (int i = 0; i < numBytes; i++) {
				out[i] = (byte) i;
			}
		}
		
		return out;
	}
	
    public static int canBeInstantiated()
    {
        try {
        System.out.printf("Test 1: Testing that creating an RSAKey object does not cause an exception or assertion failure.\n");   
        System.out.printf("  *  Creating RSAKey(new BigInteger(\"5\"), new BigInteger(\"137245\")\n");
        RSAKey rsa = new RSAKey(new BigInteger("5"), new BigInteger("137245"));

        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(true);
        if (passed == 0)
            System.out.printf("    If you're seeing an assertion failure on Dropbox, but not on your local system, make sure you're testing your code with the -ea flag enabled!\n");        
        return passed;
    }

    public static int canBeInstantiated(int numBits)
    {
        try {
        System.out.printf("Test 1: Testing that creating an RSAKey object does not cause an exception or assertion failure (test disabled).\n");   
        /*
        PRGen prg = Util432.getPRG(false);      
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey rsa = new RSAKey(new BigInteger("3"), new BigInteger("137245"));
        */
        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(true);
        return passed;
    }

    public static int maxPlaintextLengthSanityCheck()
    {
        try {
        System.out.printf("Test 2: Sanity checking that maxPlainTextLength() fails within reasonable bounds (not-shown). Does not guarantee correctness!\n");             
        //PRGen prg = Util432.getPRG(false);      
        PRGen prg = StrongPRGen.getPrGen();
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey privateKey = rsakp.getPrivateKey();
        RSAKey publicKey = rsakp.getPublicKey();

        BigInteger modulus = privateKey.getModulus();
        int upperBoundMaxPlaintextLength = (modulus.bitLength()/8) - 32;
        int lowerBoundMaxPlaintextLength = (modulus.bitLength()/16) - 64;

        int studentMaxPlaintextLength = privateKey.maxPlaintextLength();
        if ((studentMaxPlaintextLength > upperBoundMaxPlaintextLength) ||
            (studentMaxPlaintextLength < lowerBoundMaxPlaintextLength))
            {
              System.out.printf("==> FAILED, lowerBound: %d, upperBound: %d, student %d\n\n",
                                 lowerBoundMaxPlaintextLength, upperBoundMaxPlaintextLength, 
                                 studentMaxPlaintextLength);
              return 0;
            }
        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED\n");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(true);
        return passed;
    }

    public static int testEncryptionDecryptionAreSymmetric(RSAKey privateKey, RSAKey publicKey, byte[] plaintext, boolean quiet)
    {
        int passed;

        try {
        if (!quiet)
            System.out.printf("    -  Encrypting: ciphertext = publicKey.encrypt(plaintext)\n");
        byte[] ciphertext = publicKey.encrypt(plaintext, Util432.getPRG(true));

        if (!quiet)
            System.out.printf("    -  Decrypting: recovered = privateKey.decrypt(ciphertext)\n");
        byte[] recovered = privateKey.decrypt(ciphertext);

        if (!quiet)
            System.out.printf("    -  Testing that recovered = plaintext\n");
        passed = Util432.compareArraysAndPrint(recovered, plaintext, "recovered", "plaintext");
        }  
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }        
        return passed;
    }

    public static int encryptZerosAndDecryptAreSymmetric()
    {
        boolean passedBool = true;

        try {
        System.out.printf("Test 3: Testing that encrypt and decrypt are symmetric on all zeros-array of length maxPlaintextLength().\n");   

        System.out.printf("  *  Creating public RSAKey using 440 bit key\n");
        PRGen prg = Util432.getPRG(false);      
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey privateKey = rsakp.getPrivateKey();
        RSAKey publicKey = rsakp.getPublicKey();        

        System.out.printf("  *  public key maxPlaintextLength: %d, private key maxPlaintextLength: %d\n", 
                           publicKey.maxPlaintextLength(), privateKey.maxPlaintextLength());
        if (publicKey.maxPlaintextLength() != privateKey.maxPlaintextLength())
        {
            System.out.println("==> FAILED, maxPlaintextLengths do not match!");
            return 0;
        }

        byte [] plaintext = new byte[publicKey.maxPlaintextLength()];

        System.out.printf("  *  Performing symmetry testing\n");
        if (testEncryptionDecryptionAreSymmetric(privateKey, publicKey, plaintext, false) == 0)
          passedBool = false;

        System.out.printf("  *  Repeating symmetry test 10 more times with the same keys and messages\n     This ensures that your methods work for all outputs of any PRGens you may use.\n");
        for (int i  = 0; i < 10; i++)
        {
            if (testEncryptionDecryptionAreSymmetric(privateKey, publicKey, plaintext, true) == 0)
            {
                passedBool = false;
                System.out.printf("     Failure was on %dth trial\n", i);
                break;
            }
        }
    }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        if (passed == 0)
            System.out.printf("    If you're seeing an assertion failure on Dropbox, but not on your local system, make sure you're testing your code with the -ea flag enabled!\n");        
        return passed;
    }


    public static int encryptOnesAndDecryptAreSymmetric()
    {
        boolean passedBool = true;

        try {
        System.out.printf("Test 4: Testing that encrypt and decrypt are symmetric on all ones-array [0xFF 0xFF ... 0xFF] of length maxPlaintextLength().\n");   
        //System.out.printf("  *  Creating public RSAKey(new BigInteger(\"27449\"), new BigInteger(\"137245\")\n");
        //RSAKey publicKey = new RSAKey(new BigInteger("27449"), new BigInteger("137245"));
        //System.out.printf("  *  Creating private RSAKey(new BigInteger(\"5\"), new BigInteger(\"137245\")\n");
        //RSAKey privateKey = new RSAKey(new BigInteger("5"), new BigInteger("137245"));
        System.out.printf("  *  Creating public RSAKey using 440 bit key\n");
        PRGen prg = Util432.getPRG(false);      
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey privateKey = rsakp.getPrivateKey();
        RSAKey publicKey = rsakp.getPublicKey();        

        System.out.printf("  *  public key maxPlaintextLength: %d, private key maxPlaintextLength: %d\n", 
                           publicKey.maxPlaintextLength(), privateKey.maxPlaintextLength());
        if (publicKey.maxPlaintextLength() != privateKey.maxPlaintextLength())
        {
            System.out.println("==> FAILED, maxPlaintextLengths do not match!");
            return 0;
        }

        byte [] plaintext = new byte[publicKey.maxPlaintextLength()];
        for (int i = 0; i < plaintext.length; i++)
          plaintext[i] = -1;

        System.out.printf("  *  Performing symmetry testing\n");
        if (testEncryptionDecryptionAreSymmetric(privateKey, publicKey, plaintext, false) == 0)
          passedBool = false;

        System.out.printf("  *  Repeating symmetry test 10 more times with the same keys and messages\n     This ensures that your methods work for all outputs of any PRGens you may use.\n");
        for (int i  = 0; i < 10; i++)
        {
           if (testEncryptionDecryptionAreSymmetric(privateKey, publicKey, plaintext, true) == 0)
            {
                passedBool = false;
                System.out.printf("     Failure was on %dth trial\n", i);
                break;
            }
        }
        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        if (passed == 0)
            System.out.printf("    If you're seeing an assertion failure on Dropbox, but not on your local system, make sure you're testing your code with the -ea flag enabled!\n");        
        return passed;
    }
    
 public static int encryptRandomAndDecryptAreSymmetric()
    {
        boolean passedBool = true;
        int NUM_TRIALS = 64;

        try {
        System.out.printf("Test 5: Testing that encrypt and decrypt are symmetric on arrays of random value and random length\n");   

        PRGen prg = Util432.getPRG(false);      
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey privateKey = rsakp.getPrivateKey();
        RSAKey publicKey = rsakp.getPublicKey();        

        System.out.printf("  *  public key maxPlaintextLength: %d, private key maxPlaintextLength: %d\n", 
                           publicKey.maxPlaintextLength(), privateKey.maxPlaintextLength());

        int maxByteStreamLength = publicKey.maxPlaintextLength() / 2;
        System.out.printf("  *  Performing %d tests on plaintexts of lengths between 1 and %d\n", NUM_TRIALS, maxByteStreamLength);
        
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] randomBytes = Util432.randomByteArray(byteStreamLength, 0L);
            if (testEncryptionDecryptionAreSymmetric(privateKey, publicKey, randomBytes, true) == 0)
            {
                passedBool = false;
                System.out.printf("     Failure was on %dth trial\n", i);
                break;
            }
        }

        maxByteStreamLength = publicKey.maxPlaintextLength();
        System.out.printf("  *  Performing %d tests on plaintexts of lengths between 1 and %d\n", NUM_TRIALS, maxByteStreamLength);
        
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] randomBytes = Util432.randomByteArray(byteStreamLength, 0L);
            if (testEncryptionDecryptionAreSymmetric(privateKey, publicKey, randomBytes, true) == 0)
            {
                passedBool = false;
                System.out.printf("     Failure was on %dth trial\n", i);
                break;
            }
        }        

        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        
        return passed;        
    }    

    public static int signRandomAndVerifySymmetric()
    {
       boolean passedBool = true;
        int NUM_TRIALS = 64;

        try {
        System.out.printf("Test 6: Testing that sign and verify are symmetric on arrays of random value and random length\n");   

        PRGen prg = Util432.getPRG(false);      
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey privateKey = rsakp.getPrivateKey();
        RSAKey publicKey = rsakp.getPublicKey();        

        System.out.printf("  *  public key maxPlaintextLength: %d, private key maxPlaintextLength: %d\n", 
                           publicKey.maxPlaintextLength(), privateKey.maxPlaintextLength());

        int maxByteStreamLength = publicKey.maxPlaintextLength() / 2;
        System.out.printf("  *  Performing %d tests on plaintexts of lengths between 1 and %d\n", NUM_TRIALS, maxByteStreamLength);
        
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] randomBytes = Util432.randomByteArray(byteStreamLength, 0L);
            byte[] signature = privateKey.sign(randomBytes, prg);

            if (publicKey.verifySignature(randomBytes, signature) == false)
            {
                passedBool = false;
                System.out.printf("     Failure was on %dth trial\n", i);
                break;
            }
        }

        maxByteStreamLength = publicKey.maxPlaintextLength();
        System.out.printf("  *  Performing %d tests on plaintexts of lengths between 1 and %d\n", NUM_TRIALS, maxByteStreamLength);
        
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] randomBytes = Util432.randomByteArray(byteStreamLength, 0L);
            byte[] signature = privateKey.sign(randomBytes, prg);

            if (publicKey.verifySignature(randomBytes, signature) == false)
            {
                passedBool = false;
                System.out.printf("     Failure was on %dth trial\n", i);
                break;
            }
        }        

        int mptl = publicKey.maxPlaintextLength();
        maxByteStreamLength = mptl * 20;
        System.out.printf("  *  Performing %d tests on plaintexts of lengths between %d and %d\n", NUM_TRIALS, 
                                 mptl, maxByteStreamLength);
        
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int byteStreamLength = StdRandom.uniform(mptl, maxByteStreamLength);
            byte[] randomBytes = Util432.randomByteArray(byteStreamLength, 0L);
            byte[] signature = privateKey.sign(randomBytes, prg);

            if (publicKey.verifySignature(randomBytes, signature) == false)
            {
                passedBool = false;
                System.out.printf("     Failure was on %dth trial\n", i);
                break;
            }
        }        

        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        
        return passed;                
    }

    public static int testEncryptionProperties()
    {
        //can't really test padding or addition of OEAP bits since ... or COULD WE?

        System.out.printf("Test 7: Testing various properties of the output of encrypt\n");   
        boolean passedBool = true;
        int NUM_TRIALS = 64;

        try {


        PRGen prg = Util432.getPRG(false);      
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey privateKey = rsakp.getPrivateKey();
        RSAKey publicKey = rsakp.getPublicKey();  


        System.out.printf("  *  Testing that output.length is greater >= 2 when encrypting a 1 byte input\n");

        {
            byte[] oneByte = new byte[]{55};
            byte[] output = publicKey.encrypt(oneByte, prg);
            String passedString = "";
            if (output.length < 2)
            {
                passedString = "FAILED, ";
                passedBool = false;
            }
            System.out.printf("     %s, output.length was %d\n", passedString, output.length);
            System.out.printf("  *  Testing that output is different when encrypting same 1 byte input twice\n");

            byte[] output2 = publicKey.encrypt(oneByte, prg);
            if (Arrays.equals(output, output2))
            {
                passedBool = false;
                System.out.printf("     Failed, output of two consecutive calls was the same!\n");                
            }

        }

        System.out.printf("  *  Testing that output value is between 0 and modulus-1 for inputs of random length and content\n");

        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int maxByteStreamLength = publicKey.maxPlaintextLength();
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] randomBytes = Util432.randomByteArray(byteStreamLength, 0L);

            byte[] encrypted = publicKey.encrypt(randomBytes, prg);
            BigInteger encryptedInt = new BigInteger(1, encrypted);
            boolean lessThanZero = encryptedInt.compareTo(BigInteger.ZERO) < 0;
            boolean geqThanModulus = encryptedInt.compareTo(publicKey.getModulus()) >= 0;
            if (lessThanZero || geqThanModulus)
            {
                passedBool = false;
                System.out.printf("     Failure on %dth trial, less than zero: %b, geq than modulus: %b\n", i,
                                  lessThanZero, geqThanModulus);
                break;
            }
        }

        System.out.printf("  *  Testing that encrypt() gives different output for byte[]{0, 1} and byte[]{1}\n");

        {
            byte[] zeroOne = new byte[]{0, 1};
            byte[] justOne = new byte[]{1};
            byte[] outputZeroOne = publicKey.encrypt(zeroOne, prg);
            byte[] outputJustOne = publicKey.encrypt(justOne, prg);
            if (Arrays.equals(outputZeroOne, outputJustOne))
            {
                passedBool = false;
                System.out.printf("     Failed, output was the same!\n");
            }

        }

        System.out.printf("  *  Testing that encrypt() gives different output for byte[]{0, 0, 1} and byte[]{0, 1}\n");

        {
            byte[] zeroZeroOne = new byte[]{0, 0, 1};
            byte[] zeroOne = new byte[]{0, 1};
            byte[] outputZeroZeroOne = publicKey.encrypt(zeroZeroOne, prg);
            byte[] outputZeroOne = publicKey.encrypt(zeroOne, prg);
            if (Arrays.equals(outputZeroZeroOne, outputZeroOne))
            {
                passedBool = false;
                System.out.printf("     Failed, output was the same!\n");
            }

        }

        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        
        return passed; 
    }
    
    public static int testOAEPproperties()
    {
        boolean passedBool = true;
        int NUM_TRIALS = 64;

        System.out.printf("Test 8: Testing various properties of OAEP output. This test may not be meaningful unless you've passed the tests above.\n   More specific tests are included below\n");   
        try {


        PRGen prg = Util432.getPRG(false);      
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey privateKey = rsakp.getPrivateKey();
        RSAKey publicKey = rsakp.getPublicKey();  


        System.out.printf("  *  Testing that OAEP output is greater >= 33 when encrypting a 1 byte input\n");

        {
            byte[] oneByte = new byte[]{55};
            byte[] output = publicKey.encrypt(oneByte, prg);
            BigInteger encryptedBigInt = new BigInteger(1, output);
            BigInteger e = privateKey.getExponent();
            BigInteger N = privateKey.getModulus();

            BigInteger decryptedBigInt = encryptedBigInt.modPow(e, N);

            // approximateOAEPoutput is approximately the same as what the student
            // transformed into a big integer and then modpowed. The potential differences are:

            // 1. If the student's OAEPoutput had a leading byte greater than 0x7F,
            //    a sign extension byte would have been added.
            //
            // 2. If a student's OAEPoutput had leading zeros, all (or all but one)
            //    of these leading zeros would be lost

            // In the former case, we can easily remove this zero, assuming that the
            // student did not have a meaningful zero in that top position (unlikely)

            // In the latter case, such leading zeros are likely indicative of a bug
            // in their code!

            byte[] approximateOAEPoutput = decryptedBigInt.toByteArray();


            String passedString = "";
            if (approximateOAEPoutput.length < 33)
            {
                passedString = "FAILED, ";
                passedBool = false;
            }
            System.out.printf("     %sapproximateOAEPoutput.length was %d\n", passedString, approximateOAEPoutput.length);

            System.out.printf("  *  Testing that encrypted BigInt is different from decrypted BigInt for a 1 byte input\n");
            if (encryptedBigInt.equals(decryptedBigInt))
            {
                System.out.printf("     Failure, BigIntegers were equal!\n");
                passedBool = false;                
            }
        }

        System.out.printf("  *  Testing that OAEP output is different for byte[]{0, 1} and byte[]{1}\n");

        {
            byte[] zeroOne = new byte[]{0, 1};
            byte[] justOne = new byte[]{1};
            byte[] outputZeroOne = publicKey.encrypt(zeroOne, prg);
            byte[] outputJustOne = publicKey.encrypt(justOne, prg);

            BigInteger encZeroOneBigInt = new BigInteger(1, outputZeroOne);
            BigInteger encJustOneBigInt = new BigInteger(1, outputJustOne);

            BigInteger e = privateKey.getExponent();
            BigInteger N = privateKey.getModulus();

            BigInteger oaepZeroOne = encZeroOneBigInt.modPow(e, N);     
            BigInteger oaepJustOne = encJustOneBigInt.modPow(e, N);     

            if (oaepZeroOne.equals(oaepJustOne))
            {
                passedBool = false;
                System.out.printf("     Failed, OAEP output was the same!\n");
            }

        }

        System.out.printf("  *  Testing that OAEP output is >= input.length + 32 when encrypting random length inputs,\n" +
                          "     and that encrypted BigInt is different from decrypted BigInt for same random length inputs\n");

        for (int i = 0; i < NUM_TRIALS; i++)
        {

            int maxByteStreamLength = publicKey.maxPlaintextLength();
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] input = Util432.randomByteArray(byteStreamLength, 0L);

            byte[] encrypted = publicKey.encrypt(input, prg);
            BigInteger encryptedBigInt = new BigInteger(1, encrypted);
            BigInteger e = privateKey.getExponent();
            BigInteger N = privateKey.getModulus();

            BigInteger decryptedBigInt = encryptedBigInt.modPow(e, N);            
            byte[] approximateOAEPoutput = decryptedBigInt.toByteArray();
            if (approximateOAEPoutput.length < input.length + 32)
            {
                passedBool = false;
                System.out.printf("     FAILED, input.length was %d, approximateOAEPoutput.length was %d\n", 
                                        input.length, approximateOAEPoutput.length);
            }

            if (encryptedBigInt.equals(decryptedBigInt))
            {
                System.out.printf("     Failure, BigIntegers were equal!\n");
                passedBool = false;                
            }

            if (passedBool == false)
                break;
        }
        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        
        return passed;
    }


    public static int testSign()
    {
       boolean passedBool = true;
        int NUM_TRIALS = 64;

        System.out.printf("Test 9: Testing .sign().\n");   
        try {
        PRGen prg = Util432.getPRG(false);      
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey privateKey = rsakp.getPrivateKey();
        RSAKey publicKey = rsakp.getPublicKey();  
        
        System.out.printf("  *  Performing %d tests on plaintexts of lengths between 1 and %d\n", NUM_TRIALS, 
                                 publicKey.maxPlaintextLength());        
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int maxByteStreamLength = publicKey.maxPlaintextLength();
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] input = Util432.randomByteArray(byteStreamLength, 0L);
            byte[] signature = privateKey.sign(input, prg);
            if (signature.length > 256)
            {
                System.out.printf("     Signature is excessively long, length is %d bytes\n", signature.length);
                passedBool = false;
                break;
            }
        }

        System.out.printf("  *  Performing %d tests on plaintexts of lengths between 1 and %d\n", NUM_TRIALS, 
                                 publicKey.maxPlaintextLength() * 100);
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int maxByteStreamLength = publicKey.maxPlaintextLength() * 100;
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] input = Util432.randomByteArray(byteStreamLength, 0L);
            byte[] signature = privateKey.sign(input, prg);
            if (signature.length > 256)
            {
                System.out.printf("     Signature is excessively long, length is %d bytes\n", signature.length);
                passedBool = false;
                break;
            }            
        }


        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        
        return passed;    
    }


    public static int testSignAndVerifyAreSymmetric()
    {
       boolean passedBool = true;
        int NUM_TRIALS = 64;

        System.out.printf("Test 10: Testing .sign() and verify() are symmetric.\n");   
        try {
        PRGen prg = Util432.getPRG(false);      
        RSAKeyPair rsakp = new RSAKeyPair(prg, 440);
        RSAKey privateKey = rsakp.getPrivateKey();
        RSAKey publicKey = rsakp.getPublicKey();  
        
        System.out.printf("  *  Validating signatures, %d tests on plaintexts of lengths between 1 and %d\n", NUM_TRIALS, 
                                 publicKey.maxPlaintextLength());        
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int maxByteStreamLength = publicKey.maxPlaintextLength();
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] input = Util432.randomByteArray(byteStreamLength, 0L);
            byte[] signature = privateKey.sign(input, prg);
            boolean verified = publicKey.verifySignature(input, signature);

            if (!verified)
            {
                System.out.printf("     Correct signature was deemed invalid!\n", signature.length);
                passedBool = false;
                break;
            }
        }

        System.out.printf("  *  Validating signatures, Performing %d tests on plaintexts of lengths between 1 and %d\n", NUM_TRIALS, 
                                 publicKey.maxPlaintextLength() * 100);
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int maxByteStreamLength = publicKey.maxPlaintextLength() * 100;
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] input = Util432.randomByteArray(byteStreamLength, 0L);
            byte[] signature = privateKey.sign(input, prg);
            boolean verified = publicKey.verifySignature(input, signature);

            if (!verified)
            {
                System.out.printf("     Correct signature was deemed invalid!\n", signature.length);
                passedBool = false;
                break;
            }
        }

        System.out.printf("  *  Ensuring invalid signatures fail, %d tests on plaintexts of lengths between 1 and %d\n", NUM_TRIALS, 
                                 publicKey.maxPlaintextLength());        
        for (int i = 0; i < NUM_TRIALS; i++)
        {
            int maxByteStreamLength = publicKey.maxPlaintextLength();
            int byteStreamLength = StdRandom.uniform(1, maxByteStreamLength);
            byte[] input = Util432.randomByteArray(byteStreamLength, 0L);
            byte[] signature = privateKey.sign(input, prg);

            int corruptionIndex = StdRandom.uniform(signature.length);
            signature[corruptionIndex] = (byte) (signature[corruptionIndex] ^ 0x22);    

            boolean verified = publicKey.verifySignature(input, signature);

            if (verified)
            {
                System.out.printf("     Bad signature was deemed correct!\n", signature.length);
                passedBool = false;
                break;
            }
        }

        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        
        return passed;    
    }
    
    public static int testRealOAEPproperties()
    {
        boolean passedBool = true;

        System.out.printf("Test 11: Testing various properties of OAEP output using encodeOAEP and decodeOAEP\n    Note: This code assumes a minimum plaintext padding length of 1 during OAEP\n");   
        try {


        PRGen prg = Util432.getPRG(false);      
        BigInteger p1 = new BigInteger("1486551298321937725564994981881384887026305004276923596582906664804550702962879520392693992920554700305667118873491146407389163448147");
        BigInteger p2 = new BigInteger("1632936706145469108033582485008298528043417051401387824672706211153429649719177926249467183247861297547198911687010823345896754612361");
        RSAKey rsa = new RSAKey(p1, p2);
        byte[] msg = getByteArray(rsa.maxPlaintextLength() + 1, false);

        System.out.printf("  *  Testing that encodeOAEP and decodeOAEP are inverses\n");

        {
            byte[] encoded = rsa.encodeOaep(msg, prg);
            byte[] decoded = rsa.decodeOaep(encoded);

            if (!Arrays.equals(msg, decoded))
            {
                System.out.println("    FAILED: the decoded OAEP message is different than the input message");
                System.out.println("        Input Message:");
                System.out.println("        "+Arrays.toString(msg));
                System.out.println("        Decoded Message:");
                System.out.println("        "+Arrays.toString(decoded));
                passedBool = false;
            }
        }
        
        System.out.printf("  *  Testing that inverse property holds over 10 random inputs\n");
        
        for (int i = 0; i < 10; i++)
        {
        	byte[] new_msg = getByteArray(rsa.maxPlaintextLength() + 1, true);
            byte[] encoded = rsa.encodeOaep(new_msg, prg);
            byte[] decoded = rsa.decodeOaep(encoded);

            if (!Arrays.equals(new_msg, decoded))
            {
                System.out.printf("    FAILED: the decoded OAEP message is different than the input message on the %dth trial\n", i);
                System.out.println("        Input Message:");
                System.out.println("        "+Arrays.toString(new_msg));
                System.out.println("        Decoded Message:");
                System.out.println("        "+Arrays.toString(decoded));
                passedBool = false;
                break;
                
            }
        }

        System.out.printf("  *  Testing that encodeOAEP adds an acceptable amount of padding, i.e. [32, 64] bytes\n");

        {
            byte[] encoded = rsa.encodeOaep(msg, prg);
            
            if (encoded.length < 32 + msg.length || encoded.length > 64 + msg.length)
            {
                passedBool = false;
                System.out.printf("    FAILED: the encoded message is %d bytes longer than the input message\n",
                					   encoded.length - msg.length);
            }

        }

        System.out.printf("  *  Testing that output of encodeOAEP is different with different PRGens\n");
        {
        	PRGen prg1 = Util432.getPRG(true);
        	PRGen prg2 = Util432.getPRG(true);
        	byte[] encoded1 = rsa.encodeOaep(msg, prg1);
        	byte[] encoded2 = rsa.encodeOaep(msg, prg2);
            if (Arrays.equals(encoded1, encoded2))
            {
                passedBool = false;
                System.out.printf("     FAILED: output messages are the same\n");
            }
        }
        
        System.out.printf("  *  Testing that decodeOAEP checks for integrity constants after decoding\n");
        {
        	byte[] encoded = rsa.encodeOaep(msg, prg);
        	encoded[0] += 20;
        	encoded[1] += 5;
        	encoded[2] += 1;
        	byte[] decoded = new byte[1];
        	try {
        		decoded = rsa.decodeOaep(encoded);
        	} catch (Throwable e) {
                System.out.println("    ==> Exception or assertion thrown (acceptable)");
            }
        	
            if (!Arrays.equals(decoded, null))
            {
                passedBool = false;
                System.out.printf("     FAILED: decodeOAEP failed to return null or throw and error/assertion\n");
            }
        }
        
        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        
        return passed;
    }

    public static int testPaddingProperties()
    {
        boolean passedBool = true;

        System.out.printf("Test 12: Testing various properties of message padding using addPadding and removePadding\n");   
        try {
        	
        PRGen prg = Util432.getPRG(false);      
        BigInteger p1 = new BigInteger("1486551298321937725564994981881384887026305004276923596582906664804550702962879520392693992920554700305667118873491146407389163448147");
        BigInteger p2 = new BigInteger("1632936706145469108033582485008298528043417051401387824672706211153429649719177926249467183247861297547198911687010823345896754612361");
        RSAKey rsa = new RSAKey(p1, p2);

        System.out.printf("  *  Testing that addPadding and removePadding are inverses\n");

        {
        	byte[] msg = getByteArray(3, true);
            byte[] padded = rsa.addPadding(msg);
            byte[] unPadded = rsa.removePadding(padded);

            if (!Arrays.equals(msg, unPadded))
            {
                System.out.println("    FAILED: message is different after padding and unpadding");
                System.out.println("        Input Message:");
                System.out.println("        "+Arrays.toString(msg));
                System.out.println("        Padding Removed:");
                System.out.println("        "+Arrays.toString(unPadded));
                passedBool = false;
            }
        }

        System.out.printf("  *  Testing that inverse property holds for messages of all lengths\n");
        boolean firstFail = true;
        for (int i = 0; i <= rsa.maxPlaintextLength(); i++)
        {
        	byte[] msg = getByteArray(i, true);
            byte[] padded = rsa.addPadding(msg);
            byte[] unPadded = rsa.removePadding(padded);

            if (!Arrays.equals(msg, unPadded))
            {
              	if (firstFail) {
            		System.out.printf("    FAILED: message is different after add/remove padding for message of length:\n        ");
            	}
                System.out.printf("%d, ", i);
                passedBool = false;
                firstFail = false;
            }
        }
        if (!firstFail) {
        	System.out.printf("\n");
        }
        
        System.out.printf("  *  Testing that addPadding adds 1 byte when padding a message of len maxPlaintextLength\n");

        {
        	byte[] msg = getByteArray(rsa.maxPlaintextLength(), false);
            byte[] encoded = rsa.addPadding(msg);
            
            if (encoded.length != rsa.maxPlaintextLength() + 1)
            {
                passedBool = false;
                System.out.printf("    FAILED: maxPlaintextLength is %d, encoded message is %d\n",
                					   rsa.maxPlaintextLength(),encoded.length);
            }

        }
        
        System.out.printf("  *  Testing that padded message is always the expected length\n");
        System.out.printf("     --> Expected padded length is maxPlainTextLength() + 1\n");
        System.out.printf("     --> which is %d bytes in this case\n", rsa.maxPlaintextLength() + 1);
        firstFail = true;
        for (int i = 0; i <= rsa.maxPlaintextLength(); i++)
        {
        	byte[] msg = getByteArray(i, true);
            byte[] padded = rsa.addPadding(msg);

            if (padded.length != rsa.maxPlaintextLength()+1)
            {
            	if (firstFail) {
            		System.out.printf("    FAILED: for message len:\n        ");
            	}
            	System.out.printf("%d, ", padded.length);
                passedBool = false;
                firstFail = false;
            }
        }
        if (!firstFail) {
        	System.out.printf("\n");
        }
        
        System.out.printf("  *  Testing that padding works when message contains probable padding byte\n");

        {
        	byte[] msg = getByteArray(rsa.maxPlaintextLength(), false);
        	msg[msg.length-1] = (byte) 0x80;
            byte[] padded = rsa.addPadding(msg);
            byte[] unPadded = rsa.removePadding(padded);

            if (!Arrays.equals(msg, unPadded))
            {
                System.out.println("    FAILED: message is different after padding and unpadding");
                System.out.println("        Input Message:");
                System.out.println("        "+Arrays.toString(msg));
                System.out.println("        Padding Removed:");
                System.out.println("        "+Arrays.toString(unPadded));
                passedBool = false;
            }
        }
        }
        catch (Throwable e) {
          UtilCOS.printError(e);
          System.out.println("==> FAILED");          
          return 0;
        }

        int passed = UtilCOS.printPassFail(passedBool);
        
        return passed;
    }
    
	public static void main(String[] args)
	{

        int numTests = 12;
        int numPassed = 0;
        UtilCOS.printTotalNumChecks(numTests);  

        numPassed += canBeInstantiated(512);
        numPassed += maxPlaintextLengthSanityCheck();
        numPassed += encryptZerosAndDecryptAreSymmetric();
        numPassed += encryptOnesAndDecryptAreSymmetric();
        numPassed += encryptRandomAndDecryptAreSymmetric();
        numPassed += signRandomAndVerifySymmetric();
        numPassed += testEncryptionProperties();
        numPassed += testOAEPproperties();
        numPassed += testSign();
        numPassed += testSignAndVerifyAreSymmetric();
        numPassed += testRealOAEPproperties();
        numPassed += testPaddingProperties();

        UtilCOS.printNumChecksPassed(numPassed, numTests);

	}
}
