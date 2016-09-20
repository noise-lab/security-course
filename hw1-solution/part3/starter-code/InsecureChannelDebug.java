import java.io.InputStream;
import java.io.OutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;

import java.io.IOException;
import java.util.Arrays;


public class InsecureChannel {
    // This implements a workable communication channel abstraction.   
    // But it offers no particular security guarantees.    You will extend this in a subclass
    //    to provide security.
    private DataInputStream inStream;
    private DataOutputStream outStream;

    private static int channelCount = 0;    
    private int channelID; //set at creation
    private static int sendCount = 0;
    private static int receiveCount = 0;

    //if true, messages will be echoed to screen
    private static final boolean echoToScreen = true;  
    
    //set echoType to ENTIRE_MSG if you want to echo entire messages
    private static final EchoType echoType = EchoType.FIRST_ECHO_NUM_BYTES; 
    private static final int ECHO_NUM = 12;
    private enum EchoType {
    	ENTIRE_MSG, FIRST_ECHO_NUM_BYTES
    }

    public InsecureChannel(InputStream inStr, OutputStream outStr) throws IOException {
	// Take a pair of streams, one incoming and one outgoing, and use them to build a 
	//     bi-directional channel.   By assumption, there is another program somewhere that
	//     is at the other end of each one of these streams, so that our inStream is hooked up 
	//     to their outStream, and vice versa.

    
    channelID = channelCount;
    channelCount++;
	inStream = new DataInputStream(inStr);
	outStream = new DataOutputStream(outStr);
    }

    public void sendMessage(byte[] message) throws IOException {
	// Send a discrete message (datagram) to the party on the other end of the channel.
	// We assume that the party on the other end will make a matching call to receiveMessage.

	outStream.writeInt(message.length);
	for (int i = 0; i < message.length; i++)	
		outStream.write(message[i]);		
	
	if (echoToScreen)
		if (echoType == EchoType.ENTIRE_MSG)
			Util432s.printTaggedByteArray(String.format("Written to channel %d: msg #%d [",  
				                          channelID, sendCount++), message, "]\n");
		else if (echoType == EchoType.FIRST_ECHO_NUM_BYTES)
		{
			byte[] firstFourBytes = Arrays.copyOf(message, ECHO_NUM);
			Util432s.printTaggedByteArray(String.format("Written to channel %d: msg #%d [",  
				                          channelID, sendCount++), firstFourBytes, "...]\n");
		}

	outStream.flush();
    }

    public byte[] receiveMessage() throws IOException {
	// Receive a discrete message (datagram) from the party on the other end of the channel.
	// We assume that the party on the other end will make a matching call to sendMessage.

	int len = inStream.readInt();
	byte[] message = new byte[len];
	for(int i=0; i < message.length; i++)
	    message[i] = inStream.readByte();

	if (echoToScreen)
		if (echoType == EchoType.ENTIRE_MSG)
			Util432s.printTaggedByteArray(String.format("Removed from channel %d: msg #%d [",  
				                          channelID, receiveCount++), message, "]\n");
		else if (echoType == EchoType.FIRST_ECHO_NUM_BYTES)
		{
			byte[] firstFourBytes = Arrays.copyOf(message, ECHO_NUM);
			Util432s.printTaggedByteArray(String.format("Removed from channel %d: msg #%d [",  
				                          channelID, receiveCount++), firstFourBytes, "...]\n");
		}

	return message;
    }

    public void close() throws IOException {
	// Close the channel

	outStream.close();
	inStream.close();
    }
}
