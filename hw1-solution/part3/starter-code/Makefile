
JAVAS= ChannelTest.java InsecureChannel.java InsecureChannelDebug.java SecureChannel.java SecureChannelTest.java Util432s.java


default: test

test: classes
	java -enableassertions PRF
	java -enableassertions ChannelTest

classes:
	javac -classpath "junit-4.8.2.jar" *.java

deploy: provided3.zip
	echo "Uploading provided Java code to course website"
	scp provided3.zip cos432@portal.cs.princeton.edu:/n/fs/csweb/courses/archive/fall15/cos432/homework/provided3.zip

provided3.zip: $(JAVAS)
	zip provided3.zip $(JAVAS)
