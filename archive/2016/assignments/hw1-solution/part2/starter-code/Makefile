
JAVAS= DHConstants.java KeyExchange.java RSAKey.java RSAKeyPair.java HW2Util.java

default: provided2.zip

#deploy: provided2.zip
#	echo "Uploading provided Java code to course website"
#	scp provided2.zip portal.cs.princeton.edu:/n/fs/csweb/courses/archive/fall14/cos432/homework/provided2.zip

provided2.zip: $(JAVAS)
	zip provided2.zip $(JAVAS)

tidy:
	rm -rf *~

clean: tidy
	rm -rf *.class

spotless: clean
	rm -rf provided2.zip
