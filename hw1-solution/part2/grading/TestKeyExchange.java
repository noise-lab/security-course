import java.util.Arrays;
import java.math.BigInteger;


public class TestKeyExchange {
	public static int canBeInstantiated()
	{
		try {
			PRGen prg = Util432.getPRG(false);
			System.out.printf("Test 1: Testing that creating a pair of KeyExchange objects does not cause an exception or assertion failure.\n");   

			KeyExchange server = new KeyExchange(prg, true);
			KeyExchange client = new KeyExchange(prg, false);

		}
		catch (Throwable e) {
			UtilCOS.printError(e);
			System.out.println("==> FAILED");
			return 0;
		}

		int passed = UtilCOS.printPassFail(true);
		return passed;	
	}

	public static int testNotNullOnRandomValue()
	{
		int NUM_TRIALS = 8;
		boolean passedBool = true;

		try {
			PRGen prg = Util432.getPRG(false);
			System.out.printf("Test 2a: Testing that output is not null for correctly prepared out message.\n");   

			KeyExchange server = new KeyExchange(prg, true);
			KeyExchange client = new KeyExchange(prg, false);

			for (int i = 0; i < NUM_TRIALS; i++)
			{

				byte[] d1;
				byte[] d2;

				if (i % 2 == 0)
				{
					d1 = client.processInMessage(server.prepareOutMessage());
					d2 = server.processInMessage(client.prepareOutMessage());
				}
				else
				{
					d2 = server.processInMessage(client.prepareOutMessage());
					d1 = client.processInMessage(server.prepareOutMessage());
				}

				boolean d1null = (d1 == null);
				boolean d2null = (d2 == null);


				if (d1null || d2null)
				{
					passedBool = false;
					System.out.printf("     d1==null: %b, d2==null: %b, failure was on %dth trial\n", d1null, d2null, i);
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


	public static int testCorrectDigest()
	{
		int NUM_TRIALS = 2;
		boolean passedBool = true;

		try {
			PRGen prg = Util432.getPRG(false);
			System.out.printf("Test 2b: Testing that server and client agree on digest value.\n");   

			KeyExchange server = new KeyExchange(prg, true);
			KeyExchange client = new KeyExchange(prg, false);

			for (int i = 0; i < NUM_TRIALS; i++)
			{

				byte[] d1;
				byte[] d2;

				if (i % 2 == 0)
				{
					d1 = client.processInMessage(server.prepareOutMessage());
					d2 = server.processInMessage(client.prepareOutMessage());
				}
				else
				{
					d2 = server.processInMessage(client.prepareOutMessage());
					d1 = client.processInMessage(server.prepareOutMessage());
				}

				if (!Arrays.equals(d1, d2))
				{
					passedBool = false;
					System.out.printf("     Failure was on %dth trial\n", i);
					break;
				}

				if (d1 == null)
				{
					passedBool = false;
					System.out.printf("     Digest value was null, failure was on %dth trial\n", i);
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

	public static int testCorrectOutputSize()
	{
		int NUM_TRIALS = 2;
		boolean passedBool = true;

		try {
			PRGen prg = Util432.getPRG(false);
			System.out.printf("Test 3: Testing that output size matches OUTPUT_SIZE_BYTES.\n");   

			for (int i = 0; i < NUM_TRIALS; i++)
			{
				KeyExchange server = new KeyExchange(prg, true);
				KeyExchange client = new KeyExchange(prg, false);

				byte[] d1 = client.processInMessage(server.prepareOutMessage());
				byte[] d2 = server.processInMessage(client.prepareOutMessage());

				int d1length = (d1 == null) ? 0 : d1.length;
				int d2length = (d2 == null) ? 0 : d2.length;

				if ((d1length != KeyExchange.OUTPUT_SIZE_BYTES) || (d2length != KeyExchange.OUTPUT_SIZE_BYTES))
				{
					passedBool = false;
					System.out.printf("     d1.length: %d, d2.length: %d, OUTPUT_SIZE_BYTES: %d\n", 
						d1length, d2length, KeyExchange.OUTPUT_SIZE_BYTES);
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

	public static int testNullOnBadInput()
	{
		int NUM_TRIALS = 2;
		boolean passedBool = true;

		try {
			PRGen prg = Util432.getPRG(false);
			System.out.printf("Test 4: Testing vulnerability to man in the middle attacks.\n");   

			for (int i = 0; i < NUM_TRIALS; i++)
			{
				KeyExchange server = new KeyExchange(prg, true);
				KeyExchange client = new KeyExchange(prg, false);

				byte[] d1 = client.processInMessage((BigInteger.ONE).toByteArray());
				byte[] d2 = client.processInMessage((DHConstants.p).subtract(BigInteger.ONE).toByteArray());
				byte[] d3 = server.processInMessage((BigInteger.ONE).toByteArray());
				byte[] d4 = server.processInMessage((DHConstants.p).subtract(BigInteger.ONE).toByteArray());

				if (d1 != null)
				{
					System.out.printf("     FAILED: client accepted 1 as valid message.\n");   
					passedBool = false;
				}

				if (d2 != null)
				{
					System.out.printf("     FAILED: client accepted p-1 as valid message.\n");   
					passedBool = false;
				}

				if (d3 != null)
				{
					System.out.printf("     FAILED: server accepted 1 as valid message.\n");   
					passedBool = false;
				}

				if (d4 != null)
				{
					System.out.printf("     FAILED: server accepted p-1 as valid message.\n");   
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

	public static int testRandomness()
	{
		int NUM_TRIALS = 2;
		boolean passedBool = true;

		try {
			PRGen prg = Util432.getPRG(false);
			System.out.printf("Test 5: Testing that processIn always generates same value for same message.\n");   

			for (int i = 0; i < NUM_TRIALS; i++)
			{
				KeyExchange server = new KeyExchange(prg, true);
				KeyExchange client = new KeyExchange(prg, false);        	
				byte[] m1 = client.prepareOutMessage();
				byte[] m2 = client.prepareOutMessage();

				byte[] di1 = server.processInMessage(m1);
				byte[] di2 = server.processInMessage(m1);

				if (!Arrays.equals(di1, di2))
				{
					System.out.printf("     FAILED: Different digest generate for same output message.\n");   
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



	public static void main(String[] args)
	{
		int numTests = 6;
		int numPassed = 0;
		UtilCOS.printTotalNumChecks(numTests);  

		numPassed += canBeInstantiated();
		numPassed += testNotNullOnRandomValue();
		numPassed += testCorrectDigest();
		numPassed += testCorrectOutputSize();
		numPassed += testNullOnBadInput();
		numPassed += testRandomness();

		UtilCOS.printNumChecksPassed(numPassed, numTests);


	}
}