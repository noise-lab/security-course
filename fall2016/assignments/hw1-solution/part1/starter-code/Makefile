
JAVAS= AuthEncryptor.java AuthDecryptor.java PRF.java PRGen.java StreamCipher.java

default: test

test: classes
	java -enableassertions PRF

classes:
	javac -classpath "junit-4.8.2.jar" *.java

deploy: provided1.zip
	echo "Uploading provided Java code to course website"
	scp provided1.zip cos432@portal.cs.princeton.edu:/n/fs/csweb/courses/archive/fall15/cos432/homework/provided1.zip

provided1.zip: $(JAVAS)
	zip provided1.zip $(JAVAS)

tidy:
	rm -rf *~

clean: tidy
	rm -rf *.class

spotless: clean
	rm -rf provided1.zip

