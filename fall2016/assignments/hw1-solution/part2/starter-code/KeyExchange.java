public class KeyExchange {
    public static final int OUTPUT_SIZE_BYTES = PRF.OUTPUT_SIZE_BYTES;
    public static final int OUTPUT_SIZE_BITS = 8 * OUTPUT_SIZE_BYTES;

    public KeyExchange(PRGen rand, boolean iAmServer) {
        // Prepares to do a key exchange.   <rand> is a secure pseudorandom generator
        //    that can be used by the implementation.   <iAmServer> is true iff we are
        //    playing the server role in this exchange.   Each exchange has two 
        //    participants; one of them plays the client role and the other plays the
        //    server role.
        //
        // Once the KeyExchange object is created, two things have to happen for the 
        //    key exchange process to be complete.
        // 1.  Call prepareOutMessage on this object, and send the result to the other
        //     participant.
        // 2.  Receive the result of the other participant's prepareOutMessage, and pass it in
        //     as the argument to a call on this object's processInMessage.  
        // These two things can happen in either order, or even concurrently (e.g., in 
        //     different threads).  This code must work correctly regardless of the order.
        //
        // The call to processInMessage should behave as follows:
        //     If passed a null value, then throw a NullPointerException.
        //     Otherwise, if passed a value that could not possibly have been generated
        //        by prepareOutMessage, then return null.
        //     Otherwise, return a "digest" (hash) with the property described below.
        //
        // This code must provide the following security guarantee: If the two 
        //    participants end up with the same non-null digest value, then this digest value
        //    is not known to anyone else.   This must be true even if third parties
        //    can observe and modify the messages sent between the participants.
        // This code is NOT required to check whether the two participants end up with
        //    the same digest value; the code calling this must verify that property.

        // IMPLEMENT THIS
    }

    public byte[] prepareOutMessage() {
        return null; // IMPLEMENT THIS
    }

    public byte[] processInMessage(byte[] inMessage) {
        // Output: Digest of size OUTPUT_SIZE_BYTES
        if (inMessage == null)    throw new NullPointerException();

        return null; // IMPLEMENT THIS
    }
}
