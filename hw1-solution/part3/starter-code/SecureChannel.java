
import java.io.InputStream;
import java.io.OutputStream;

import java.io.IOException;


public class SecureChannel extends InsecureChannel {
    // This is just like an InsecureChannel, except that it provides 
    //    authenticated encryption for the messages that pass
    //    over the channel.   It also guarantees that messages are delivered 
    //    on the receiving end in the same order they were sent (returning
    //    null otherwise).  Also, when the channel is first set up,
    //    the client authenticates the server's identity, and the necessary
    //    steps are taken to detect any man-in-the-middle (and to close the
    //    connection if a MITM is detected).
    //
    // The code provided here is not secure --- all it does is pass through
    //    calls to the underlying InsecureChannel.


    public SecureChannel(InputStream inStr, OutputStream outStr, 
            PRGen rand, boolean iAmServer,
            RSAKey serverKey) throws IOException {
        // if iAmServer==false, then serverKey is the server's *public* key
        // if iAmServer==true, then serverKey is the server's *private* key

        super(inStr, outStr);
        // IMPLEMENT THIS
    }

    public void sendMessage(byte[] message) throws IOException {
        super.sendMessage(message);    // IMPLEMENT THIS
    }

    public byte[] receiveMessage() throws IOException {
        return super.receiveMessage();   // IMPLEMENT THIS
    }
}
