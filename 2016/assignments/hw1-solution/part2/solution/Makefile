
HW2_JAVAS= DHConstants.java KeyExchange.java RSAKey.java RSAKeyPair.java HW2Util.java
OLD_JAVAS= AuthEncryptor.java AuthDecryptor.java PRF.java PRGen.java StreamCipher.java TrueRandomness.java
JAVAS= $(HW2_JAVAS) $(OLD_JAVAS)

HW1_SOLN_DIR= ../HW1

default: test

test: classes
	java -enableassertions KeyExchange
	java -enableassertions RSAKey
	java -enableassertions HW2Util

classes: $(JAVAS)
	javac -classpath "junit-4.8.2.jar" *.java

PRGen.java: $(HW1_SOLN_DIR)/PRGen.java
	cp $(HW1_SOLN_DIR)/PRGen.java .

AuthEncryptor.java: $(HW1_SOLN_DIR)/AuthEncryptor.java
	cp $(HW1_SOLN_DIR)/AuthEncryptor.java .

AuthDecryptor.java: $(HW1_SOLN_DIR)/AuthDecryptor.java
	cp $(HW1_SOLN_DIR)/AuthDecryptor.java .

PRF.java: $(HW1_SOLN_DIR)/PRF.java
	cp $(HW1_SOLN_DIR)/PRF.java .

StreamCipher.java: $(HW1_SOLN_DIR)/StreamCipher.java
	cp $(HW1_SOLN_DIR)/StreamCipher.java .

TrueRandomness.java: $(HW1_SOLN_DIR)/TrueRandomness.java
	cp $(HW1_SOLN_DIR)/TrueRandomness.java .

tidy:
	rm -rf *~

clean: tidy
	rm -rf *.class $(OLD_JAVAS)

spotless: clean

