
HW3_JAVAS= ChannelTest.java InsecureChannel.java SecureChannel.java
HW2_JAVAS= DHConstants.java KeyExchange.java RSAKey.java RSAKeyPair.java StrongPRGen.java HW2Util.java
HW1_JAVAS= AuthDecryptor.java AuthEncryptor.java PRF.java PRGen.java StreamCipher.java TrueRandomness.java
OLD_JAVAS= $(HW1_JAVAS) $(HW2_JAVAS)
JAVAS= $(HW3_JAVAS) $(OLD_JAVAS)

HW1_SOLN_DIR= ../HW1
HW2_SOLN_DIR= ../HW2

default: test

test: classes
	java -enableassertions ChannelTest

classes: $(JAVAS)
	javac -classpath "junit-4.8.2.jar" *.java

AuthDecryptor.java: $(HW1_SOLN_DIR)/AuthDecryptor.java
	cp $(HW1_SOLN_DIR)/AuthDecryptor.java .

AuthEncryptor.java: $(HW1_SOLN_DIR)/AuthEncryptor.java
	cp $(HW1_SOLN_DIR)/AuthEncryptor.java .

PRF.java: $(HW1_SOLN_DIR)/PRF.java
	cp $(HW1_SOLN_DIR)/PRF.java .

PRGen.java: $(HW1_SOLN_DIR)/PRGen.java
	cp $(HW1_SOLN_DIR)/PRGen.java .

StreamCipher.java: $(HW1_SOLN_DIR)/StreamCipher.java
	cp $(HW1_SOLN_DIR)/StreamCipher.java .

TrueRandomness.java: $(HW1_SOLN_DIR)/TrueRandomness.java
	cp $(HW1_SOLN_DIR)/TrueRandomness.java .

DHConstants.java: $(HW2_SOLN_DIR)/DHConstants.java
	cp $(HW2_SOLN_DIR)/DHConstants.java .

KeyExchange.java: $(HW2_SOLN_DIR)/KeyExchange.java
	cp $(HW2_SOLN_DIR)/KeyExchange.java .

RSAKey.java: $(HW2_SOLN_DIR)/RSAKey.java
	cp $(HW2_SOLN_DIR)/RSAKey.java .

RSAKeyPair.java: $(HW2_SOLN_DIR)/RSAKeyPair.java
	cp $(HW2_SOLN_DIR)/RSAKeyPair.java .

StrongPRGen.java: $(HW2_SOLN_DIR)/StrongPRGen.java
	cp $(HW2_SOLN_DIR)/StrongPRGen.java .

HW2Util.java: $(HW2_SOLN_DIR)/HW2Util.java
	cp $(HW2_SOLN_DIR)/HW2Util.java .

tidy:
	rm -rf *~

clean: tidy
	rm -rf *.class $(OLD_JAVAS)

spotless: clean

