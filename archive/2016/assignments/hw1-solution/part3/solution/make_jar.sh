#!/usr/bin/env bash

PROGUARD="../../../proguard/proguard.jar"
CONFIG="@../../../proguard/libconfig.pro"

mkdir solution_jar

# HW1
cp ../../HW1/starter-code/PRF.java solution_jar
cp ../../HW1/solution/AuthEncryptor.java solution_jar
cp ../../HW1/solution/AuthDecryptor.java solution_jar
cp ../../HW1/solution/StreamCipher.java solution_jar

# HW2
cp ../../HW2/solution/*.java solution_jar

# HW3
cp SecureChannel.java solution_jar
cp ../starter-code/InsecureChannel.java solution_jar

# etc
cp ../../HW4/grading/PRGen.java solution_jar #faster prgen
cp ../../HW4/starter-code/LongUtils.java solution_jar #needed for prgen
cp ../../std/TrueRandomness.java solution_jar #needed?

cd solution_jar
javac *.java
jar cf hw3_tmp.jar *.class
java -jar $PROGUARD -injars hw3_tmp.jar -outjars ../hw3.jar $CONFIG
cd ..
rm -R solution_jar
