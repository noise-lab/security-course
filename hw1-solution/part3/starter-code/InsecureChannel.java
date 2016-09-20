
import java.io.InputStream;
import java.io.OutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;

import java.io.IOException;


public class InsecureChannel {
    // This implements a workable communication channel abstraction.   
    // But it offers no particular security guarantees.    You will extend this in a subclass
    // to provide security.
	private DataInputStream inStream;
	private DataOutputStream outStream;

	public InsecureChannel(InputStream inStr, OutputStream outStr) 
		throws IOException {
	// Take a pair of streams, one incoming and one outgoing, and use them to 
	// build a bi-directional channel.   By assumption, there is another 
	// program somewhere that is at the other end of each one of these 
	// streams, so that our inStream is hooked up to their outStream, 
	// and vice versa.

		inStream = new DataInputStream(inStr);
		outStream = new DataOutputStream(outStr);
	}

	public void sendMessage(byte[] message) throws IOException {
	// Send a discrete message (datagram) to the party on the other end of the 
	// channel. We assume that the party on the other end will make a matching 
	// call to receiveMessage.

		outStream.writeInt(message.length);
		for(int i=0; i<message.length; ++i) {
			outStream.write(message[i]);
		}
		outStream.flush();
	}

	public byte[] receiveMessage() throws IOException {
	// Receive a discrete message (datagram) from the party on the other end of 
	// the channel. We assume that the party on the other end will make a 
	// matching call to sendMessage.
	// This will throw an EOFException if the stream has been closed.

		int len = inStream.readInt();
		if(len < 0){
	    // channel was closed, return null
			return null;
		}
		byte[] message = new byte[len];
		for(int i=0; i<message.length; ++i) {
	    message[i] = inStream.readByte();
	  }
		return message;
	}

	public void close() throws IOException {
	// Close the channel
		outStream.close();
		inStream.close();
	}
}