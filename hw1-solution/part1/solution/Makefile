
default: test

deploySample: hw1Sample.jar
	scp hw1Sample.jar felten@portal.cs.princeton.edu:/n/fs/csweb/courses/archive/fall14/cos432/homework/hw1sample.jar

hw1Sample.jar: classes
	jar cf hw1Sample.jar *.class

test: classes
	java -enableassertions PRF
	java -enableassertions AuthEncryptor

classes:
	javac -classpath "junit-4.8.2.jar" *.java

