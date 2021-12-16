
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PipedInputStream;
import java.io.PipedOutputStream;

import java.io.IOException;


public class ChannelTest implements Runnable {
    // This program tests the implementation of channels.   It's not a 
    //    complete test -- if this works, you can't be certain that your
    //    channel implementation is good -- but it does provide a good 
    //    sanity check, and it might smoke out synchronization / deadlock
    //    problems.

    private InputStream     inStream;
    private OutputStream    outStream;
    private boolean         serverMode;
    private RSAKey          key;

    public ChannelTest(InputStream inStr, OutputStream outStr, 
		       boolean iAmServer, RSAKey rsaKey) {
	inStream = inStr;
	outStream = outStr;
	serverMode = iAmServer;
	key = rsaKey;
    }

    public void run() {
	try {
	    // Communication happens through InsecureChannels.  Once you
	    //    get your SecureChannel code done, you'll probably want
	    //    to switch this over to use SecureChannels instead.
	    SecureChannel chan = new SecureChannel(inStream, outStream, StrongPRGen.getPrGen(), serverMode, key);
	    if(serverMode) {
		// server echoes back messages it received
		for(;;){
		    byte[] msg = chan.receiveMessage();
		    if(msg==null)    break;
		    chan.sendMessage(msg);
		}
	    }else{
		// client sends message, receives it back, verifies equal
		byte[] buf = new byte[73];
		for(int i=0; i<10; ++i){
		    for(int j=0; j<buf.length; ++j){
			buf[j] = (byte)(i+j);
		    }
		    chan.sendMessage(buf);
		    byte[] echo = chan.receiveMessage();
		    assert echo.length == buf.length;
		    for(int j=0; j<buf.length; ++j){
			assert buf[j] == echo[j];
		    }
		}
	    }
	}catch(IOException x){
	    x.printStackTrace(System.err);
	}
    }

    public static void main(String[] argv) throws IOException {
	PipedOutputStream out1 = new PipedOutputStream();
	PipedInputStream in1 = new PipedInputStream(out1);
	PipedOutputStream out2 = new PipedOutputStream();
	PipedInputStream in2 = new PipedInputStream(out2);

	RSAKeyPair keyPair = new RSAKeyPair(StrongPRGen.getPrGen(), 1024);

	ChannelTest cct = new ChannelTest(in1, out2, false, keyPair.getPublicKey());
	ChannelTest sct = new ChannelTest(in2, out1, true, keyPair.getPrivateKey());
	Thread clntThread = new Thread(cct);
	Thread servThread = new Thread(sct);
	servThread.setDaemon(true);

	servThread.start();
	clntThread.start();

	try {
	    clntThread.join();
	    System.out.println("OK");
	}catch(InterruptedException x){
	    x.printStackTrace(System.err);
	}
    }
}