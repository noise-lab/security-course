import java.io.InputStream;
import java.io.OutputStream;
import java.io.PipedInputStream;
import java.io.PipedOutputStream;
import java.io.IOException;
import java.util.Random;
import java.nio.ByteBuffer;


public class TestSecureChannel implements Runnable {
    // This program tests the implementation of channels.   It's not a 
    //    complete test -- if this works, you can't be certain that your
    //    channel implementation is good -- but it does provide a good 
    //    sanity check, and it might smoke out synchronization / deadlock
    //    problems.

  private InputStream     inStream;
  private OutputStream    outStream;
  private boolean         iAmServer;
  private PRGen       prgen;
  private RSAKey      rsaKey;
  private RunType rt;

  private static int messagesSent = 0;
  private static int messagesReceived = 0;

    private enum RunType {
      SERVER_ECHO, CLIENT_ECHO, SERVER_ECHO_CORRUPTED_BYTES, BOTH_SEND_RECIEVE, SENDS_ALL_THEN_ECHOS, REPLAY, FLIP_ORDER
    }

  public TestSecureChannel(InputStream inStr, OutputStream outStr, 
    boolean iAmServer, RSAKey rsaKey, RunType rt) {
    inStream = inStr;
    outStream = outStr;
    this.iAmServer = iAmServer;
    this.rsaKey = rsaKey;

    byte[] prgenKey = new byte[PRGen.KEY_SIZE_BYTES];
    Random random = new Random();
    random.nextBytes(prgenKey);

    prgen = new PRGen(prgenKey);
    this.rt = rt;

  } 

  private static RSAKeyPair generateRSAKeyPair(int numbits)
  {
    byte[] prgenKey = new byte[PRGen.KEY_SIZE_BYTES];
    Random random = new Random();
    random.nextBytes(prgenKey);

    PRGen prgen = new PRGen(prgenKey);

    RSAKeyPair rsakp = new RSAKeyPair(prgen, numbits);
    return rsakp;
  }

  public void sendMessageUnsafe(OutputStream outStream, byte[] message) throws IOException {
  // Send a discrete message (datagram) to the party on the other end of the 
  // channel. We assume that the party on the other end will make a matching 
  // call to receiveMessage.
    int messageLength = message.length;
    byte[] messageLengthBytes = ByteBuffer.allocate(4).putInt(messageLength).array();
    outStream.write(messageLengthBytes);
    for(int i=0; i<message.length; ++i) {
      outStream.write(message[i]);
    }
    outStream.flush();
  }

  public byte[] receiveMessageUnsafe(InputStream inStream) throws IOException {
  // Receive a discrete message (datagram) from the party on the other end of 
  // the channel. We assume that the party on the other end will make a 
  // matching call to sendMessage.
  // This will throw an EOFException if the stream has been closed.
    byte[] messageLengthBytes = new byte[4];
    inStream.read(messageLengthBytes);
    int len = ByteBuffer.wrap(messageLengthBytes).getInt();
    if(len < 0){
      // channel was closed, return null
      return null;
    }
    byte[] message = new byte[len];
    for(int i=0; i<message.length; ++i) {
      message[i] = (byte) inStream.read();
    }
    return message;
  }

  private static boolean sendMessageSafe(SecureChannel chan, String threadName, String channelName, byte[] message)
  {
    try {
      chan.sendMessage(message);
    }
    catch (IOException e)
    {
      String exceptionMessage = e.getMessage();
     if (e.toString().equals("java.io.EOFException"))
        System.out.printf("%s thread ending. %s channel indicates there will be no more data (EOF).\n", threadName, channelName);
      else
        if (exceptionMessage.equals("Pipe closed") || exceptionMessage.equals("Pipe broken"))
          System.out.printf("%s thread ending. %s channel is closed.\n", threadName, channelName);
        else
          if (exceptionMessage.equals("Write end dead") || exceptionMessage.equals("Read end dead"))
            System.out.printf("    %s thread ending. %s channel is closed.\n", threadName, channelName);
          else
        {
          System.out.printf("%s thread ending. Exception thrown!\n", threadName);
          e.printStackTrace();
        }
        return false;
      }

      messagesSent++;
      return true;
  }


    private static byte[] receiveMessageSafe(SecureChannel chan, String threadName, String channelName)
    {
      byte[] returnMsg;
      try {
        returnMsg = chan.receiveMessage();
      }
      catch (IOException e)
      {
        String exceptionMessage = e.getMessage();
        if (e.toString().equals("java.io.EOFException"))
          System.out.printf("    %s thread ending. %s channel indicates there will be no more data (EOF).\n", threadName, channelName);
        else
          if (exceptionMessage.equals("Pipe broken"))
            System.out.printf("    %s thread ending. %s channel is closed.\n", threadName, channelName);
          else
          if (exceptionMessage.equals("Write end dead") || exceptionMessage.equals("Read end dead"))
            System.out.printf("    %s thread ending. %s channel is closed.\n", threadName, channelName);
          else
          {
            System.out.printf("    %s thread ending. Exception thrown that should not have occurred (unless you specifically threw it).\n If you can't fix, post on Piazza. ", threadName);
            e.printStackTrace();
          }
          return null;
        }

        messagesReceived++;
        return returnMsg;
      }

      public void run() {

        try {
          SecureChannel chan;
          try {
	          chan = new SecureChannel(inStream, outStream, prgen,
	            iAmServer, rsaKey);
          } catch(java.lang.AssertionError e){
              System.out.println("    Assertion error in constructor");
              return;
          } catch(IOException e) {
        	  String exceptionMessage = e.getMessage();
        	  if (exceptionMessage.equals("Read end dead") || exceptionMessage.equals("Write end dead")) {
        		  System.out.println("    Connection dead");
        	  } else {
        		  e.printStackTrace();
        	  }
        	  return;
          }
          
          if (rt == RunType.BOTH_SEND_RECIEVE) {
            InsecureChannel.corruptionType = InsecureChannel.CorruptionType.NONE;
            byte[] messageToSend = new byte[73];
            byte[] messageToRecieve = new byte[73]; 

            for(int j=0; j < messageToSend.length; ++j){
              messageToSend[j] = (byte) (j);
            }

            for(int j=0; j < messageToRecieve.length; ++j){
              messageToRecieve[j] = (byte) (j+1);
            }

            if (iAmServer) {
              byte[] temp = messageToRecieve;
              messageToRecieve = messageToSend;
              messageToSend = temp;
            }

            boolean succeeded = sendMessageSafe(chan, "Echoer", "Echoer -> Starter", messageToSend);
            if (!succeeded)
              return;

            byte[] msg = receiveMessageSafe(chan, "Starter", "Echoer -> Starter");
            if (msg == null)
              return;

            assert msg.length == messageToRecieve.length;

            for(int j=0; j<messageToRecieve.length; ++j){
              assert messageToRecieve[j] == msg[j];
            }

            if (iAmServer) {
              succeeded = sendMessageSafe(chan, "Echoer", "Echoer -> Starter", msg);
              if (!succeeded)
                return;

              msg = receiveMessageSafe(chan, "Starter", "Echoer -> Starter");
              if (msg == null)
                return;
              chan.close();
            } else {
              msg = receiveMessageSafe(chan, "Starter", "Echoer -> Starter");
              if (msg == null)
                return;

              succeeded = sendMessageSafe(chan, "Echoer", "Echoer -> Starter", msg);
              if (!succeeded)
                return;
            }
            
          } else if (rt == RunType.REPLAY) {
            InsecureChannel.corruptionType = InsecureChannel.CorruptionType.NONE;
            byte[] messageToSend = new byte[73];
            for(int j=0; j < messageToSend.length; ++j){
              messageToSend[j] = (byte) (j);
            }

            if (iAmServer) {
              boolean succeeded = sendMessageSafe(chan, "Echoer", "Echoer -> Starter", messageToSend);
              if (!succeeded)
                return;

              byte[] msg = receiveMessageSafe(chan, "Starter", "Echoer -> Starter");
              if (msg == null) {
                return;
              }

              sendMessageSafe(chan, "Echoer", "Echoer -> Starter", messageToSend);

            } else {
              byte[] msg = receiveMessageUnsafe(inStream);
              sendMessageUnsafe(outStream, msg);
              msg = receiveMessageSafe(chan, "Starter", "Echoer -> Starter");
            }
            chan.close();
          } else if (rt == RunType.FLIP_ORDER) {
            InsecureChannel.corruptionType = InsecureChannel.CorruptionType.REORDER;
            byte[] firstMessage = new byte[73];
            byte[] secondMessage = new byte[73]; 

            for(int j=0; j < firstMessage.length; ++j){
              firstMessage[j] = (byte) (j);
            }

            for(int j=0; j < secondMessage.length; ++j){
              secondMessage[j] = (byte) (j+1);
            }

            if (iAmServer) {
              boolean succeeded = sendMessageSafe(chan, "Echoer", "Echoer -> Starter", firstMessage);
              if (!succeeded)
                return;
              succeeded = sendMessageSafe(chan, "Echoer", "Echoer -> Starter", secondMessage);
              if (!succeeded)
                return;
              byte[] msg = receiveMessageSafe(chan, "Starter", "Echoer -> Starter");
              if (msg == null)
                return;
            } else {
              byte[] msg = receiveMessageSafe(chan, "Starter", "Echoer -> Starter");
              if (msg == null) {
                return;
              }

              assert msg.length == secondMessage.length;

              for(int j=0; j<secondMessage.length; ++j){
                assert secondMessage[j] == msg[j];
              }

              msg = receiveMessageSafe(chan, "Starter", "Echoer -> Starter");
              if (msg == null) {
                return;
              }

              assert msg.length == firstMessage.length;

              for(int j=0; j<firstMessage.length; ++j){
                assert firstMessage[j] == msg[j];
              }

              InsecureChannel.corruptionType = InsecureChannel.CorruptionType.NONE;
              byte[] junk = {0};
              boolean succeeded = sendMessageSafe(chan, "Echoer", "Echoer -> Starter", junk);
              if (!succeeded)
                return;
            }

            chan.close();
          } else {

            boolean serverEchoes;
            if (rt == RunType.SERVER_ECHO || rt == RunType.SERVER_ECHO_CORRUPTED_BYTES)
              serverEchoes = true;
            else
              serverEchoes = false;
            

            boolean iAmEcho = serverEchoes ? iAmServer : !iAmServer;

        // server echoes back messages it received
            if(iAmEcho) {
              while(true) 
              {

                byte[] msg = receiveMessageSafe(chan, "Echoer", "Starter -> Echoer");
                if (msg == null)
                  return;

                
            //Example debug statement
            //String debugTag = String.format("server received: ");
            //String endDebugTag  = "\n";
            //Util432s.printTaggedByteArray(debugTag, msg, endDebugTag);

                boolean succeeded = sendMessageSafe(chan, "Echoer", "Echoer -> Starter", msg);
                if (!succeeded)
                  return;
            //chan.sendMessage(msg);
              }
            }

        // client sends message, receives it back, verifies equal
            else {

          //10 messages hard coded to be 73 bytes long
              byte[] buf = new byte[73];        
              for(int i=0; i < 10; ++i){

            //jth byte in message #i is i+j
                for(int j=0; j < buf.length; ++j){
                  buf[j] = (byte) (i+j);
                }

            if ((i == 0) & (rt == RunType.SERVER_ECHO_CORRUPTED_BYTES))
              InsecureChannel.corruptionType = InsecureChannel.CorruptionType.FLIP_ONE_BIT_PER_BYTE;
            else
              InsecureChannel.corruptionType = InsecureChannel.CorruptionType.NONE;

                boolean succeeded = sendMessageSafe(chan, "Starter", "Starter -> Echoer", buf);
                if (!succeeded)
                  return;

                byte[] echo = receiveMessageSafe(chan, "Starter", "Echoer -> Starter");
                if (echo == null)
                  return;


                assert echo.length == buf.length;
                for(int j=0; j<buf.length; ++j){
                  assert buf[j] == echo[j];
                }
              }
              chan.close();
            }
        
          }
        } catch(IOException x){
          x.printStackTrace(System.err);
        }
      }


      public static int channelTest(RunType rt)
      {

  //should be chosen so that maxPlaintextLength is > 72
        int RSA_KEY_PAIR_BITS = 1024; 
        RSAKeyPair rsakp = generateRSAKeyPair(RSA_KEY_PAIR_BITS);
  //if this fails, you need to adjust KEY_PAIR_BITS!
        assert(rsakp.getPublicKey().maxPlaintextLength() > 72); 

        try {
        PipedOutputStream out1 = new PipedOutputStream();
        PipedInputStream in1 = new PipedInputStream(out1);
        PipedOutputStream out2 = new PipedOutputStream();
        PipedInputStream in2 = new PipedInputStream(out2);

        TestSecureChannel.messagesSent = 0;
        TestSecureChannel.messagesReceived = 0;

        TestSecureChannel cct = new TestSecureChannel(in1, out2, 
          false, rsakp.getPublicKey(), rt);
        TestSecureChannel sct = new TestSecureChannel(in2, out1, 
          true, rsakp.getPrivateKey(), rt);
        Thread clntThread = new Thread(cct);
        Thread servThread = new Thread(sct);
        servThread.setDaemon(true);

        servThread.start();
        clntThread.start();

        try {
          clntThread.join();
          servThread.join();
          //System.out.println("OK");
        }catch(InterruptedException x){
          x.printStackTrace(System.err);
        }

        if ((rt == RunType.SERVER_ECHO) | (rt == RunType.CLIENT_ECHO))
        {
          if ((messagesSent == 20) & (messagesSent == messagesReceived))
          {
            System.out.printf("==> passed\n\n");
            return 1;
          }        
          
          System.out.printf("==> FAILED, messages sent: %d, messages received: %d\n\n", 
                             messagesSent, messagesReceived);
          return 0;
        }
        else if (rt == RunType.BOTH_SEND_RECIEVE) {
          if (messagesSent == 4 && messagesSent == messagesReceived) {
            System.out.printf("==> passed\n\n");
            return 1;
          }

          System.out.printf("==> FAILED, well formed message rejected\n\n", 
                             messagesSent, messagesReceived);
          return 0;

        } else if (rt == RunType.REPLAY) {
          if (messagesSent == 1) {
            System.out.printf("==> passed\n\n");
            return 1;
          } else {
            System.out.printf("==> FAILED, accepted a reflected message\n\n");
            return 0;
          }
        } else if (rt == RunType.FLIP_ORDER) {
          if (messagesReceived == 1) {
            System.out.printf("==> passed\n\n");
            return 1;
          }

          System.out.printf("==> FAILED, accepted messages in reversed order\n\n", 
                             messagesSent, messagesReceived);
          return 0;
        }
        else
        {
          if ((messagesSent == 20) & (messagesSent == messagesReceived))
          {
            System.out.printf("==> FAILED, 20 messages sent and received\n\n");
            return 0;
          }        
          
          System.out.printf("==> passed, messages sent: %d, messages received: %d\n\n", 
                             messagesSent, messagesReceived);
          return 1;
        }


        }
        catch (Throwable e)
        {
          System.out.println("Something has gone really wrong.");
          e.printStackTrace();
          return 0;
        }

      }

      public static void main(String[] argv) throws IOException {
        int numTests = 7;
        int numPassed = 0;
        UtilCOS.printTotalNumChecks(numTests);

        System.out.printf("Test 1: Client sends 20 messages, and server echoes them back.\n        Test will succeed if all 20 messages are successfully echoed.\n");
        numPassed += channelTest(RunType.SERVER_ECHO);
        System.out.printf("Test 2: Server sends 20 messages, and client echoes them back.\n        Test will succeed if all 20 messages are successfully echoed.\n");
        numPassed += channelTest(RunType.CLIENT_ECHO);
        System.out.printf("Test 3: Client and server both send 1 message simultaneously.\n");
        numPassed += channelTest(RunType.BOTH_SEND_RECIEVE);
        System.out.printf("Test 4: Server detects reflected message\n");
        numPassed += channelTest(RunType.REPLAY);
        System.out.printf("Test 5: Server's messages are sent out of order\n");
        numPassed += channelTest(RunType.FLIP_ORDER);
        InsecureChannel.corruptionType = InsecureChannel.CorruptionType.NONE;
        System.out.printf("Test 6: Client sends 20 messages, and server echoes them back. All bytes of first message are corrupted.\n        Test will succeed if all messages do NOT reach destination.\n");
        numPassed += channelTest(RunType.SERVER_ECHO_CORRUPTED_BYTES);
        System.out.printf("Test 7: Client sends 20 messages, and server echoes them back. Bytes are corrupted during channel creation.\n        Test will succeed if all messages do NOT reach destination.\n");
        numPassed += channelTest(RunType.SERVER_ECHO_CORRUPTED_BYTES);



        UtilCOS.printNumChecksPassed(numPassed, numTests);
      }
    }
