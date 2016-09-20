import java.io.InputStream;
import java.io.OutputStream;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

import java.io.IOException;

public class SecureChannel extends InsecureChannel {
    // This is just like an InsecureChannel, except that it provides confidentiality and integrity
    //    for the messages that passes over the channel.   Also, when the channel is first set up,
    //    the client authenticates the server's identity, and the necessary steps are taken to 
    //    detect any man-in-the-middle (and to close the connection if a MITM is detected).
    //
    // The code provided here is not secure --- all it does is pass through calls to the underlying
    //    InsecureChannel.

    private AuthEncryptor outEncryptor;
    private AuthDecryptor inDecryptor;

    private long outSequenceNum = 0;
    private long inSequenceNum = 0;

    public SecureChannel(InputStream inStr, OutputStream outStr, 
			 PRGen rand, boolean iAmServer,
             RSAKey serverKey) throws IOException {
	// if iAmServer==false, then serverKey is the server's *public* key
	// if iAmServer==true, then serverKey is the server's *private* key

	super(inStr, outStr);

	KeyExchange kex = new KeyExchange(rand, iAmServer);
	byte[] outMsg = kex.prepareOutMessage();
	byte[] inMsg;
	if(iAmServer){
	    super.sendMessage(outMsg);
	    inMsg = super.receiveMessage();
	}else{
	    inMsg = super.receiveMessage();
	    super.sendMessage(outMsg);
	}
	byte[] kexResult = kex.processInMessage(inMsg);
	assert (kexResult != null);
	PRGen prg = new PRGen(kexResult);
	if(iAmServer){
	    byte[] keySpace = new byte[AuthEncryptor.KEY_SIZE_BYTES];
	    prg.nextBytes(keySpace);
	    inDecryptor = new AuthDecryptor(keySpace);
	    prg.nextBytes(keySpace);
	    outEncryptor = new AuthEncryptor(keySpace);

	    // sign and send the key exchange result
	    byte[] sig = serverKey.sign(kexResult, prg);
	    sendMessage(sig);

	}else{
	    byte[] keySpace = new byte[AuthEncryptor.KEY_SIZE_BYTES];
	    prg.nextBytes(keySpace);
	    outEncryptor = new AuthEncryptor(keySpace);
	    prg.nextBytes(keySpace);
	    inDecryptor = new AuthDecryptor(keySpace);

	    // receive and verify signature on kexResult
	    byte[] sig = receiveMessage();
	    assert (sig != null);
	    boolean verified = serverKey.verifySignature(kexResult, sig);
	    if( ! verified){
		close();
	    }
	}
    }

    private static byte[] longToByteArray(long x) {
	return ByteBuffer.allocate(Long.SIZE/Byte.SIZE).order(ByteOrder.LITTLE_ENDIAN).putLong(x).array();
    }

    public void sendMessage(byte[] message) throws IOException {
	byte[] nonce = longToByteArray(outSequenceNum);
	++outSequenceNum;
	super.sendMessage(outEncryptor.encrypt(message, nonce, false));
    }

    public byte[] receiveMessage() throws IOException {
	byte[] nonce = longToByteArray(inSequenceNum);
	++inSequenceNum;
	return inDecryptor.decrypt(super.receiveMessage(), nonce);  
    }
}
