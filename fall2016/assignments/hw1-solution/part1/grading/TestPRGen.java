import java.util.Arrays;
import java.util.Random;

public class TestPRGen {

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

private static int generateLargestValue(int numBits)
{
  int returnValue = generateBitMask(numBits);

        returnValue = returnValue & 0x7FFFFFFF; //mask top bit, since that makes it negative
        return returnValue;
    }

    private static int generateBitMask(int numBits)
    {
        int returnValue = 0;

        for (int i = 0; i < numBits; i++)
        {
          returnValue <<= 1;
          returnValue += 1;
      }

      return returnValue;
  }

  private static int generateSmallestValue(int numBits)
  {
    if (numBits < 32)
      return 0;

  return 0x80000000;
}


public static int bitsAppearRandom(int numBitsAtOnce)
{
    System.out.printf("  *  Testing distribution of 0s and 1s with calls to next(%d)\n", numBitsAtOnce);
    try {

      PRGen prgen = getPRG(false);
      int NUM_BITS = (16384    / numBitsAtOnce) * numBitsAtOnce;
      int MIN_ALLOWABLE_ONES = (int) (NUM_BITS * 0.4);
      int MAX_ALLOWABLE_ONES = (int) (NUM_BITS * 0.6);

      int oneCount = 0;
      boolean outsideRangeWarning = false;

      for (int i = 0; i < NUM_BITS / numBitsAtOnce; i++)
      {
        int bits = prgen.next(numBitsAtOnce);
        int newBits = bits & generateBitMask(numBitsAtOnce);
        if (newBits != bits)
          outsideRangeWarning = true;
      oneCount += countOnes(newBits);
  }

  if (outsideRangeWarning)
    System.out.printf("     WARNING: At least one generated value was outside the allowed range. Extra bits were ignored.\n");

if ((oneCount > MAX_ALLOWABLE_ONES) || (oneCount < MIN_ALLOWABLE_ONES))
{
    System.out.printf("     FAILED: Out of %d generated bits, there were %d ones (%.2f%%).\n", NUM_BITS, oneCount, 100 * (double) oneCount / NUM_BITS);
    return 0;
}

return 1;
}
catch (Throwable e) {
  UtilCOS.printError(e);
  return 0;
}
}

public static int bitsFillAllowedRange(int numBitsAtOnce, double percentile)
{
    System.out.printf("  *  Testing range of values returned by next(%d)\n", numBitsAtOnce);

    try {

      PRGen prgen = getPRG(false);

        int NUM_TRIALS = 100000; //number of trials must be picked so that max and min values are observed! 16384

        int MIN_ALLOWABLE_VALUE = generateSmallestValue(numBitsAtOnce);
        int MAX_ALLOWABLE_VALUE = generateLargestValue(numBitsAtOnce);
        
        int MIN_EXPECTED_OBSERVABLE_VALUE = (int) (MIN_ALLOWABLE_VALUE * percentile);
        int MAX_EXPECTED_OBSERVABLE_VALUE = (int) (MAX_ALLOWABLE_VALUE * percentile);

        int minObserved = prgen.next(numBitsAtOnce);
        int maxObserved = minObserved;

        for (int i = 0; i < NUM_TRIALS; i++)
        {
          int nextValue = prgen.next(numBitsAtOnce);
          minObserved = Math.min(minObserved, nextValue);
          maxObserved = Math.max(maxObserved, nextValue);
      }

      if ((minObserved < MIN_ALLOWABLE_VALUE) || (maxObserved > MAX_ALLOWABLE_VALUE))
      {
          System.out.printf("     FAILED: Values observed are outside of the range of allowed values.\n" +
            "             Range of observed values: %d, %d [in hex: 0x%x, 0x%x]\n" +
            "             Range of possible values: %d, %d [in hex: 0x%x, 0x%x]\n", 
            minObserved, maxObserved, minObserved, maxObserved, 
            MIN_ALLOWABLE_VALUE, MAX_ALLOWABLE_VALUE, MIN_ALLOWABLE_VALUE, 
            MAX_ALLOWABLE_VALUE);
          return 0;
      }       

      if ((minObserved > MIN_EXPECTED_OBSERVABLE_VALUE) || (maxObserved < MAX_EXPECTED_OBSERVABLE_VALUE))
      {
          System.out.printf("     FAILED: Values observed do not fill the range of allowed values.\n" +
            "             Range of observed values: %d, %d [in hex: 0x%x, 0x%x]\n" +
            "             Range of possible values: %d, %d [in hex: 0x%x, 0x%x]\n", 
            minObserved, maxObserved, minObserved, maxObserved, 
            MIN_ALLOWABLE_VALUE, MAX_ALLOWABLE_VALUE, MIN_ALLOWABLE_VALUE, 
            MAX_ALLOWABLE_VALUE);            
          return 0;
      }

      return 1;
  }
  catch (Throwable e) {
    UtilCOS.printError(e);
    return 0;
}
}

public static int testDeterministic(int numBits) {
  System.out.printf("  *  Output of prg.next() is deterministic\n", numBits);   

  try {
    PRGen prg = getPRG(false);
    PRGen prg1 = getPRG(false);
    boolean passed = prg.next(numBits) == prg1.next(numBits);

    if (!passed)
    {
      System.out.printf("     Failed: Different %d-bit value returned by prg.next(%d) and prg1.next(%d), where PRGs have same keys\n", numBits, numBits, numBits);
      return 0;
  }
  return 1;
}
catch (Throwable e) {
    UtilCOS.printError(e);
    return 0;
}

}

private static int testDependsOnKey(int numBits) {
  System.out.printf("  *  Output of prg.next() depends on key passed to constructor\n", numBits);   
  try {
    PRGen prg = getPRG(false);
    PRGen prgRandom = getPRG(true);
    boolean passed = (prg.next(numBits) != prgRandom.next(numBits));

    if (!passed)
    {
      System.out.printf("     Failed: Same %d-bit value returned after one next(%d) call to two different PRGs with different keys\n", numBits, numBits);
      return 0;
  }
  return 1;
}
catch (Throwable e) {
    UtilCOS.printError(e);
    return 0;
}
}


private static int testNextNotEqual(int numBits) {
  System.out.printf("  *  Two consecutive calls to prg.next(%d) do not return the same value (2 << 2^%d)\n", numBits, numBits);
  try {
    PRGen prg = getPRG(false);
    boolean passed = (prg.next(numBits) != prg.next(numBits));

    if (!passed)
    {
      System.out.printf("     Failed: Using a single PRG, the same %d-bit value was returned by two consecutive calls to .next(%d)\n", numBits, numBits);
      return 0;
  }
  return 1;
}
catch (Throwable e) {
    UtilCOS.printError(e);
    return 0;
}
}

private static int testNextMultipleNotEqual(int numNextCalls, int numBits) {
  System.out.printf("  *  Out of %d calls to prg.next(%d), none return the same value (%d << 2^%d)\n", numNextCalls, numBits, numNextCalls, numBits);
  try{
    PRGen prg = getPRG(false);

    int [] bits = new int[numNextCalls];

    for (int i = 0; i < numNextCalls; i++)
      bits[i] = prg.next(numBits);

  boolean passed = true;

  Arrays.sort(bits);
  for (int i = 1; i < bits.length; i++)
      if (bits[i] == bits[i-1])
        passed = false;

    if (!passed)
    {
        System.out.printf("     Failed: Using a single PRG, the same %d-bit value was returned by two calls to next(%d)\n", numBits, numBits);
        return 0;
    }
    return 1;
}
catch (Throwable e) {
  UtilCOS.printError(e);
  return 0;
}

}

public static int testCoreProperties()
{
    int numPassed = 0;
    int numTests = 4;
    System.out.println("\nTest 1a-1d: Testing core properties of your PRG");

    numPassed += testDeterministic(32);
    numPassed += testDependsOnKey(32);
    numPassed += testNextNotEqual(32);
    numPassed += testNextMultipleNotEqual(10, 32);

    System.out.printf("==> %d/%d tests passed\n", numPassed, numTests);
    return numPassed;
}

private static int testStatisticalProperties()
{
    int numPassed = 0;
    int numTests = 4;

    System.out.println("\nTests 2a-2d: Testing statistical properties of the output of your PRG");

    numPassed += bitsAppearRandom(4);
    numPassed += bitsAppearRandom(32);
    numPassed += bitsFillAllowedRange(4, 1);
    numPassed += bitsFillAllowedRange(32, 0.999);


    System.out.printf("==> %d/%d tests passed\n", numPassed, numTests);
    return numPassed;
}

public static int probeEmptyBehavior()
{
  System.out.printf("\nProbe 1: Probing to see how your code reacts to weird inputs\n");

  try{
  System.out.printf("  *  Creating PRG with 0 byte key, then calling .next(32)\n");

  PRGen prg = new PRGen(new byte[0]);
  int output = prg.next(32);
  System.out.printf("     Output is %d\n", output);

}
   catch (Throwable e) {
    UtilCOS.printError(e);
  }

  PRGen prg2 = getPRG(false);
  System.out.printf("  *  Requesting 0 bits using .next(0)\n");

  try {
  int output = prg2.next(0);
  System.out.printf("     Output is %d\n", output);
  }
   catch (Throwable e) {
    UtilCOS.printError(e);
  }

  System.out.printf("  *  Requesting 33 bits using .next(33)\n");


  try {
  int output = prg2.next(33);
  System.out.printf("     Output is %d\n", output);
  }
   catch (Throwable e) {
    UtilCOS.printError(e);
  }

  System.out.printf("==> Probing completed (no-autograding of results)\n");

  return 0;   
}

public static void main(String[] args) {
    int numTests = 8;
    int numPassed = 0;
    UtilCOS.printTotalNumChecks(numTests);  

/*
        java.security.Security.addProvider(new sun.security.provider.Sun());
        java.security.Security.addProvider(new sun.security.rsa.SunRsaSign());
        java.security.Security.addProvider(new com.sun.net.ssl.internal.ssl.Provider());
        java.security.Security.addProvider(new com.sun.crypto.provider.SunJCE());
        java.security.Security.addProvider(new sun.security.jgss.SunProvider());
        java.security.Security.addProvider(new com.sun.security.sasl.Provider());
        java.security.Security.addProvider(new org.jcp.xml.dsig.internal.dom.XMLDSigRI());
        java.security.Security.addProvider(new sun.security.smartcardio.SunPCSC());

*/
        numPassed += testCoreProperties();
        numPassed += testStatisticalProperties();

        System.out.printf("\n");

        UtilCOS.printNumChecksPassed(numPassed, numTests);

        probeEmptyBehavior();

    }
}