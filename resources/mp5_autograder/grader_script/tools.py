#!/usr/bin/python
import re

__author__ = 'SimonSK'


def read_solution(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if not line:
                continue
            if line == '':
                continue
            if line[0] == '#':
                continue
            if line[0] == '\n':
                continue
            line = line.strip()
            line = line.lower()
            # remove colons
            line = re.sub('[:-]', '', line)
            lines.append(line)
    return lines


def read_solution_asis(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if not line:
                continue
            if line == '':
                continue
            lines.append(line)
    return lines


def read_partners(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            if not line:
                continue
            if line == '':
                continue
            lines.extend(re.split(r'[:;,|\-\s]+', line.strip()))
    return lines
