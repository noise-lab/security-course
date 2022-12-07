#!/bin/bash

mkdir -p grades
python team_separator.py > ./grades/separated_mp2.1_grades.csv
python grade_distributioner.py
