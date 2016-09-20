import java.util.Random;
import java.math.BigInteger;

public class DropboxTestRSAKeyPair {

    public static void main(String[] args)
    {
        int numTests = 2;
        int numPassed = 0;
        UtilCOS.printTotalNumChecks(numTests);  

        numPassed += TestRSAKeyPair.canBeInstantiated(312);
        numPassed += TestRSAKeyPair.testPrimality(new int[]{312, 363});
        UtilCOS.printNumChecksPassed(numPassed, numTests);
    }
}
