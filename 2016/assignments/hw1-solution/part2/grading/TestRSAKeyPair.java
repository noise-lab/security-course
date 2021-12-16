import java.util.Random;
import java.math.BigInteger;

public class TestRSAKeyPair {

    public static int canBeInstantiated(int numbits)
    {
        try {
            System.out.printf("Test 1: Testing that creating an RSAKeyPair object does not cause an exception or assertion failure.\n");   
            System.out.printf("  *  Instantiating a reference PRG [you should not submit your PRGen.java]\n");
            PRGen prg = Util432.getPRG(false);
            System.out.printf("  *  Creating RSAKeyPair(prg, %d)\n", numbits);
            RSAKeyPair rsakp = new RSAKeyPair(prg, numbits);
            System.out.printf("  *  Creating another RSAKeyPair(prg, %d)\n", numbits);
            RSAKeyPair rsakp2 = new RSAKeyPair(prg, numbits);
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

 public static int testPrimality(int [] numBits)
 {
    int NUM_TRIALS = 32;
    int numTests = numBits.length * NUM_TRIALS;
    int numPassed = 0;

    System.out.printf("Test 2: Testing that output of .getPrimes() are both prime\n");   
    try {

        for (int i = 0; i < numBits.length; i++)
        {
            System.out.printf("  *  Testing with %d bit primes\n", numBits[i]);


            for (int j = 0; j < NUM_TRIALS; j++)
            {
                int theseArePrime = testPrimality(numBits[i]);
                numPassed += theseArePrime;
                if (! (theseArePrime == 1) )
                {
                    System.out.printf("     At least one of your two .getPrimes() is not prime!");
                    break; 
                }
            }
        }

    }
    catch (Throwable e) {
      UtilCOS.printError(e);
      System.out.println("==> FAILED");
      return 0;
  }
  int passed = UtilCOS.printPassFail(numPassed == numTests);

  return passed;
}

public static int testPrimality(int numBits)
{
    PRGen prg = Util432.getPRG(false);
    RSAKeyPair rsakp = new RSAKeyPair(prg, numBits);
    BigInteger [] studentPrimes = rsakp.getPrimes();
        //isProbablePrime returns false ONLY if a number is definitely composite
    boolean firstIsProbablyPrime = studentPrimes[0].isProbablePrime(4);
    boolean secondIsProbablyPrime = studentPrimes[1].isProbablePrime(4);   

    if ( firstIsProbablyPrime & secondIsProbablyPrime )
        return 1;
    return 0;
}

 public static int testEandD(int [] numBits)
 {
    int NUM_TRIALS = 4;
    boolean passedBool = true;

    System.out.printf("Test 3: Testing e, d, and modulus\n");   
    try {

        for (int i = 0; i < numBits.length; i++)
        {
            System.out.printf("  *  Testing with %d bit primes\n", numBits[i]);


            for (int j = 0; j < NUM_TRIALS; j++)
            {
                
                PRGen prg = Util432.getPRG(false);
                RSAKeyPair rsakp = new RSAKeyPair(prg, numBits[i]);
                BigInteger [] studentPrimes = rsakp.getPrimes();
                BigInteger p = studentPrimes[0];
                BigInteger q = studentPrimes[1];
                BigInteger pm1 = studentPrimes[0].subtract(BigInteger.ONE);
                BigInteger qm1 = studentPrimes[1].subtract(BigInteger.ONE);
                BigInteger phi = pm1.multiply(qm1);

                BigInteger e = rsakp.getPublicKey().getExponent();
                BigInteger d = rsakp.getPrivateKey().getExponent();
                BigInteger m1 = rsakp.getPublicKey().getModulus();

                boolean modulusIsCorrect;
                boolean eIsRelativelyPrimeToPhi;
                boolean dIsTheModInverse;

                modulusIsCorrect = (m1.equals(p.multiply(q)));
                eIsRelativelyPrimeToPhi = e.gcd(phi).equals(BigInteger.ONE);
                dIsTheModInverse = d.equals(e.modInverse(phi)); 

                if (!modulusIsCorrect || !eIsRelativelyPrimeToPhi || !dIsTheModInverse)
                {
                    passedBool = false;
                    System.out.printf("     Failure: modulus Correct: %b, e relatively prime: %b, d is mod inverse: %b\n",
                                            modulusIsCorrect, eIsRelativelyPrimeToPhi, dIsTheModInverse);
                    break;

                }


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
    int numTests = 3;
    int numPassed = 0;
    UtilCOS.printTotalNumChecks(numTests);  

    numPassed += canBeInstantiated(512);
    numPassed += testPrimality(new int[]{512, 768, 1024});
    numPassed += testEandD(new int[]{512});


    UtilCOS.printNumChecksPassed(numPassed, numTests);
}
}
