#!/usr/bin/env bash

PROGUARD="../../../proguard/proguard.jar"
CONFIG="@../../../proguard/libconfig.pro"

mkdir solution_jar
cp *.java solution_jar
cp ../starter-code/PRF.java solution_jar
cd solution_jar
javac *.java
jar cf hw1.jar *.class
java -jar $PROGUARD -injars hw1.jar -outjars ../hw1_obf.jar $CONFIG
cd ..
rm -R solution_jar
