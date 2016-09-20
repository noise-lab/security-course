public class DropboxTestRSAKey {

	public static void main(String[] args)
	{
        int numTests = 4;
        int numPassed = 0;
        UtilCOS.printTotalNumChecks(numTests);  

        numPassed += TestRSAKey.canBeInstantiated();
        numPassed += TestRSAKey.maxPlaintextLengthSanityCheck();        
        numPassed += TestRSAKey.encryptZerosAndDecryptAreSymmetric();
        numPassed += TestRSAKey.encryptOnesAndDecryptAreSymmetric();

        UtilCOS.printNumChecksPassed(numPassed, numTests);

	}
}
