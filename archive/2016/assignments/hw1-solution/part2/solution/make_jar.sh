#!/usr/bin/env bash

PROGUARD="../../../proguard/proguard.jar"
CONFIG="@../../../proguard/libconfig.pro"

mkdir solution_jar
cp *.java solution_jar
cp ../../HW1/solution/*.java solution_jar
cp ../../HW1/starter-code/PRF.java solution_jar
cp ../../std/TrueRandomness.java solution_jar
cd solution_jar
javac *.java
jar cf hw2_tmp.jar *.class
java -jar $PROGUARD -injars hw2_tmp.jar -outjars ../hw2.jar $CONFIG
cd ..
rm -R solution_jar
