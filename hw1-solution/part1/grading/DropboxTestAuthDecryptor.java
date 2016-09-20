public class DropboxTestAuthDecryptor {
	public static void main(String[] args)
	{
		int numTests = 1;
		int numPassed = 0;

        UtilCOS.printTotalNumChecks(numTests);

		System.out.printf("Dropbox Test 1: Ensuring that your AuthDecryptor returns null when run with an incorrect nonce\n");
		numPassed += TestAuthDecryptor.testDecryptorHandlesIncorrectNonce();
		if (numPassed == 1)
			System.out.println("==> passed");
		else
			System.out.println("==> FAILED");

		System.out.printf("\n");
        UtilCOS.printNumChecksPassed(numPassed, numTests);


	}
}
