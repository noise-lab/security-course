#!/usr/bin/env python

"""
Modifies extracted CTools bulk download zip to use grades created by
grading scripts
"""

import argparse
import tempfile
import shutil

from common_grading import *


def handle_p2_row(row):
    """Returns list of StudentGrade objects"""
    assert len(row) == 29

    names = extract_grading_uniqnames(row.pop(0))

    state = extract_grade_part(row, 'SQL Injection',
            [('sql_0.txt', 5), ('sql_1.txt', 5), ('*sql_2.txt', 0), ('*sql_3.txt', 0)])
    state = extract_grade_part(row, 'CSRF',
            [('csrf_0.html', 5), ('csrf_1.html', 5), ('*csrf_2.html', 0)],
            state)

    state = extract_grade_part(row, 'XSS',
            [('xss_payload.html', 1), ('xss_0.txt', 6), ('xss_1.txt', 2),
                ('xss_2.txt', 2), ('xss_3.txt', 2), ('*xss_4.txt', 0)],
            state)
    state = extract_final_grade(state, 10)
    state = apply_late_penalty(row, 10, state)

    assert len(row) == 0

    grade, max_grade, comment = state
    return [StudentGrade(name, grade, comment) for name in names]

def handle_p3_row(row):
    """Returns list of StudentGrade objects"""
    assert len(row) == 19 or len(row) == 21

    names = extract_grading_uniqnames(row.pop(0))

    state = extract_grade_part(row, 'Part 1', [('pcap.txt', 9)])
    state = extract_grade_part(row, 'Part 2 (attack.txt)',
            [('Q1', 3), ('Q2', 1), ('Q3', 1), ('Q4', 3), ('Q5', 1),
             ('Q6', 1), ('Q7', 1)], state)
    state = extract_grade_part(row, 'Part 3', [('detector.py', 3)], state)

    #if len(row) == 2: # This isn't needed for this one because I edited
    # it in LibreOffice and it made sure everything had this column
    state = extract_grade_part(row, "Format", [('format', 0)], state)
    state = extract_final_grade(state, 10)
    assert len(row) == 0

    grade, max_grade, comment = state
    return [StudentGrade(name, grade, comment) for name in names]

def handle_p4_row(row):
    """Returns list of StudentGrade objects"""
    assert len(row) == 21 or len(row) == 23

    names = extract_grading_uniqnames(row.pop(0))

    state = extract_grade_part(row, 'Targets',
            [('sol0.py', 7), ('sol1.py', 7), ('sol2.py', 7), ('sol3.py', 7), ('sol4.py', 7),
             ('sol5.py', 7), ('sol6.py', 7), ('sol7.py', 0), ('sol8.py', 0), ('sol9.py', 0)])
    if len(row) == 2:
        state = extract_grade_part(row, "Format", [('format', 0)], state)
    state = extract_final_grade(state, 10)
    assert len(row) == 0

    grade, max_grade, comment = state
    return [StudentGrade(name, grade, comment) for name in names]



def main():
    # Add new project handler
    project_handlers = {'p2': handle_p2_row, 'p3': handle_p3_row, 'p4': handle_p4_row}

    parser = argparse.ArgumentParser(description='Output grades for CTools upload')
    parser.add_argument('--ctools-zip', dest='download_zip', required=True,
                        help='location of CTools bulk download')
    parser.add_argument('--output-zip', dest='output_zip', required=True,
                        help='location output ZIP to upload')
    parser.add_argument('--grading-csv', dest='grading_csv', required=True,
                        help='Concatenated CSV with all grades')
    parser.add_argument('--project', dest='project', required=True,
                        choices=project_handlers.keys(),
                        help='project we are doing grades for')

    args = parser.parse_args()
    download_zip = args.download_zip
    output_zip = args.output_zip
    grading_csv = args.grading_csv
    project = args.project

    # Extract ZIP file
    tmp_dir = tempfile.mkdtemp(prefix='ctools-upload-')
    extracted_zip = extract_zip(download_zip, tmp_dir)

    # Read grading CSV
    grades = []
    with open(grading_csv, 'rb') as grading_csv_file:
        grading_reader = csv.reader(grading_csv_file)
        for row in grading_reader:
            grades.extend(project_handlers[project](row))  # Get grades

    # Write grades to output CSV
    set_grades(extracted_zip, grades)

    # Write comments to coment files
    set_comments(extracted_zip, grades)

    # Create output ZIP
    zip_directory(extracted_zip, output_zip)

    # Delete tmp dir
    shutil.rmtree(tmp_dir)

    print "== Upload to CTools and select 'Grade file' and 'Feedback comments' =="


if __name__ == '__main__':
    main()
